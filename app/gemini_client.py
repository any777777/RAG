from __future__ import annotations

import json
import math
import os
import re
import time
from dataclasses import dataclass
from typing import Any, Callable, Sequence, TypeVar

from google import genai
from google.genai import errors as genai_errors

from app.config import CHAT_MODEL, EMBEDDING_MODEL, load_environment

EMBED_BATCH_SIZE = 20
EMBED_MIN_REQUEST_INTERVAL_SECONDS = 0.75
MAX_API_RETRIES = 6

T = TypeVar("T")


@dataclass
class ModelAnswer:
    supported: bool
    answer: str
    citation_ids: list[str]


class GeminiService:
    def __init__(
        self,
        api_key: str | None = None,
        embedding_model: str = EMBEDDING_MODEL,
        chat_model: str = CHAT_MODEL,
    ) -> None:
        load_environment()
        resolved_key = (
            api_key
            or os.getenv("GEMINI_API_KEY")
            or os.getenv("GOOGLE_API_KEY")
            or os.getenv("API_KEY")
        )
        if not resolved_key:
            raise ValueError("Gemini API key not found. Set API_KEY in the .env file.")

        self.client = genai.Client(api_key=resolved_key)
        self.embedding_model = embedding_model
        self.chat_model = chat_model
        self._last_embed_request_at = 0.0

    def embed_texts(self, texts: Sequence[str], task_type: str) -> list[list[float]]:
        embeddings: list[list[float]] = []

        for start in range(0, len(texts), EMBED_BATCH_SIZE):
            batch = list(texts[start : start + EMBED_BATCH_SIZE])
            response = self._call_with_retry(
                lambda batch=batch, task_type=task_type: self.client.models.embed_content(
                    model=self.embedding_model,
                    contents=batch,
                    config={"task_type": task_type},
                ),
                operation="embedding generation",
                throttle_embeddings=True,
            )
            embeddings.extend(self._extract_embedding_values(response))

        if len(embeddings) != len(texts):
            raise RuntimeError("Gemini returned an unexpected number of embeddings.")

        return embeddings

    def embed_query(self, text: str) -> list[float]:
        response = self._call_with_retry(
            lambda: self.client.models.embed_content(
                model=self.embedding_model,
                contents=text,
                config={"task_type": "RETRIEVAL_QUERY"},
            ),
            operation="query embedding",
            throttle_embeddings=True,
        )
        values = self._extract_embedding_values(response)
        if not values:
            raise RuntimeError("Gemini did not return a query embedding.")
        return values[0]

    def generate_grounded_answer(
        self,
        question: str,
        context: str,
        chat_history: str,
    ) -> ModelAnswer:
        system_instruction = (
            "You answer questions only from the supplied Markdown context chunks. "
            "Do not use outside knowledge. "
            "If the answer is not explicitly supported by the supplied chunks, return "
            'supported=false and answer exactly "The information is not available in the source." '
            "Only cite chunk IDs that appear in the context."
        )
        prompt = (
            "Return strict JSON with this shape only:\n"
            '{"supported": true, "answer": "text", "citations": ["chunk-0001"]}\n\n'
            f"Recent chat history:\n{chat_history or 'None'}\n\n"
            f"User question:\n{question}\n\n"
            f"Context chunks:\n{context}"
        )

        response = self._call_with_retry(
            lambda: self.client.models.generate_content(
                model=self.chat_model,
                contents=prompt,
                config={
                    "temperature": 0,
                    "response_mime_type": "application/json",
                    "system_instruction": system_instruction,
                },
            ),
            operation="answer generation",
        )

        return self._parse_answer(response.text or "")

    def _call_with_retry(
        self,
        func: Callable[[], T],
        operation: str,
        throttle_embeddings: bool = False,
    ) -> T:
        backoff_seconds = 2.0

        for attempt in range(MAX_API_RETRIES):
            if throttle_embeddings:
                self._wait_for_embedding_slot()

            try:
                result = func()
                if throttle_embeddings:
                    self._last_embed_request_at = time.monotonic()
                return result
            except (genai_errors.ClientError, genai_errors.ServerError) as exc:
                if throttle_embeddings:
                    self._last_embed_request_at = time.monotonic()

                retry_delay = self._extract_retry_delay_seconds(exc)
                if attempt < MAX_API_RETRIES - 1 and self._is_retryable(exc):
                    time.sleep(retry_delay if retry_delay is not None else backoff_seconds)
                    backoff_seconds = min(backoff_seconds * 2, 30.0)
                    continue

                raise RuntimeError(self._format_api_error(exc, operation)) from exc

    def _wait_for_embedding_slot(self) -> None:
        elapsed = time.monotonic() - self._last_embed_request_at
        remaining = EMBED_MIN_REQUEST_INTERVAL_SECONDS - elapsed
        if remaining > 0:
            time.sleep(remaining)

    @staticmethod
    def _is_retryable(error: genai_errors.APIError) -> bool:
        code = int(getattr(error, "code", 0) or 0)
        status = str(getattr(error, "status", "") or "").upper()
        return code in {408, 429, 500, 502, 503, 504} or status in {
            "RESOURCE_EXHAUSTED",
            "UNAVAILABLE",
            "DEADLINE_EXCEEDED",
            "INTERNAL",
        }

    @classmethod
    def _format_api_error(cls, error: genai_errors.APIError, operation: str) -> str:
        code = int(getattr(error, "code", 0) or 0)
        status = str(getattr(error, "status", "") or "").upper()
        retry_delay = cls._extract_retry_delay_seconds(error)

        if code == 429 or status == "RESOURCE_EXHAUSTED":
            retry_hint = (
                f" Wait about {retry_delay} seconds and try again."
                if retry_delay is not None
                else " Wait a short time and try again."
            )
            return (
                f"Gemini rate limit reached during {operation}.{retry_hint} "
                "If this happens repeatedly, reduce rebuild frequency or enable billing "
                "for higher Gemini API limits in Google AI Studio."
            )

        message = str(getattr(error, "message", "") or "").strip()
        if message:
            return f"Gemini API error during {operation}: {message}"

        return f"Gemini API error during {operation}: {error}"

    @classmethod
    def _extract_retry_delay_seconds(cls, error: genai_errors.APIError) -> int | None:
        for candidate in cls._iter_retry_delay_values(getattr(error, "details", None)):
            parsed = cls._parse_duration_seconds(candidate)
            if parsed is not None:
                return parsed

        message = str(getattr(error, "message", "") or "")
        if message:
            parsed = cls._parse_duration_seconds(message)
            if parsed is not None:
                return parsed

        parsed = cls._parse_duration_seconds(str(error))
        return parsed

    @classmethod
    def _iter_retry_delay_values(cls, value: Any) -> list[str]:
        found: list[str] = []

        if isinstance(value, dict):
            for key, item in value.items():
                if key == "retryDelay":
                    found.append(str(item))
                else:
                    found.extend(cls._iter_retry_delay_values(item))
        elif isinstance(value, list):
            for item in value:
                found.extend(cls._iter_retry_delay_values(item))

        return found

    @staticmethod
    def _parse_duration_seconds(value: str) -> int | None:
        match = re.search(r"(\d+(?:\.\d+)?)\s*s", value)
        if not match:
            return None
        return max(1, math.ceil(float(match.group(1))))

    @staticmethod
    def _extract_embedding_values(response: object) -> list[list[float]]:
        if hasattr(response, "embeddings") and getattr(response, "embeddings"):
            return [list(item.values) for item in response.embeddings]
        if hasattr(response, "embedding") and getattr(response, "embedding"):
            return [list(response.embedding.values)]

        if isinstance(response, dict):
            if response.get("embeddings"):
                return [list(item["values"]) for item in response["embeddings"]]
            if response.get("embedding"):
                return [list(response["embedding"]["values"])]

        raise RuntimeError("Unable to extract embedding vectors from Gemini response.")

    @staticmethod
    def _parse_answer(text: str) -> ModelAnswer:
        candidate = text.strip()
        if candidate.startswith("```"):
            candidate = candidate.strip("`")
            candidate = candidate.replace("json", "", 1).strip()

        try:
            data = json.loads(candidate)
        except json.JSONDecodeError:
            unsupported = "The information is not available in the source." in candidate
            answer = (
                "The information is not available in the source."
                if unsupported
                else candidate.strip() or "The information is not available in the source."
            )
            return ModelAnswer(supported=not unsupported, answer=answer, citation_ids=[])

        supported = bool(data.get("supported"))
        answer = str(data.get("answer") or "").strip()
        citation_ids = [str(item) for item in data.get("citations", []) if str(item).strip()]

        if not supported or not answer:
            return ModelAnswer(
                supported=False,
                answer="The information is not available in the source.",
                citation_ids=[],
            )

        return ModelAnswer(supported=True, answer=answer, citation_ids=citation_ids)
