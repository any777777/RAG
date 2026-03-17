from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from app.config import (
    COLLECTION_NAME,
    AppSettings,
    chroma_dir,
    load_settings,
    manifest_path,
    save_settings,
)
from app.gemini_client import GeminiService
from app.markdown_processor import build_chunks, parse_markdown
from app.models import AnswerResult, BuildResult, ChatTurn, QueryResult, SourceManifest
from app.vector_store import ChromaStore


class RagService:
    def __init__(self) -> None:
        self.settings = load_settings()
        self.store = ChromaStore(chroma_dir(), COLLECTION_NAME)
        self._gemini: GeminiService | None = None

    @property
    def gemini(self) -> GeminiService:
        if self._gemini is None:
            self._gemini = GeminiService()
        return self._gemini

    def rebuild_database(self, markdown_path: str, chunk_size: int, chunk_overlap: int) -> BuildResult:
        source = Path(markdown_path).expanduser().resolve()
        if source.suffix.lower() not in {".md", ".markdown"}:
            raise ValueError("Please select a Markdown file with a .md or .markdown extension.")
        if not source.exists():
            raise FileNotFoundError("The selected Markdown file was not found.")

        paragraphs = parse_markdown(source)
        chunks = build_chunks(paragraphs, source, chunk_size, chunk_overlap)
        embeddings = self.gemini.embed_texts(
            [chunk.content for chunk in chunks],
            task_type="RETRIEVAL_DOCUMENT",
        )

        self.store.recreate_collection()
        self.store.add_chunks(chunks, embeddings)

        manifest = SourceManifest(
            source_path=str(source),
            source_name=source.name,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            chunk_count=len(chunks),
            collection_name=COLLECTION_NAME,
            built_at=datetime.now(timezone.utc).isoformat(),
        )
        self.save_manifest(manifest)

        self.settings = AppSettings(
            selected_markdown=str(source),
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            top_k=self.settings.top_k,
        )
        save_settings(self.settings)

        return BuildResult(manifest=manifest)

    def answer_question(
        self,
        question: str,
        top_k: int,
        history: list[ChatTurn] | None = None,
    ) -> AnswerResult:
        if not question.strip():
            raise ValueError("Enter a question before sending.")

        manifest = self.load_manifest()
        if manifest is None or not self.store.has_collection_data():
            raise RuntimeError("Build the vector database from a Markdown file before chatting.")

        query_embedding = self.gemini.embed_query(question)
        retrieved = self.store.query(query_embedding, top_k=max(1, top_k))

        if not retrieved:
            return AnswerResult(
                answer="The information is not available in the source.",
                citations=[],
                unsupported=True,
            )

        model_answer = self.gemini.generate_grounded_answer(
            question=question,
            context=self._format_context(retrieved),
            chat_history=self._format_history(history or []),
        )

        valid_ids = {item.chunk_id for item in retrieved}
        filtered_ids = [item for item in model_answer.citation_ids if item in valid_ids]
        citations = self._resolve_citations(filtered_ids, retrieved)

        if not model_answer.supported:
            return AnswerResult(
                answer="The information is not available in the source.",
                citations=[],
                unsupported=True,
            )

        if not citations:
            citations = retrieved[: min(2, len(retrieved))]

        return AnswerResult(
            answer=model_answer.answer,
            citations=citations,
            unsupported=False,
        )

    def update_top_k(self, top_k: int) -> None:
        self.settings.top_k = top_k
        save_settings(self.settings)

    @staticmethod
    def load_manifest() -> SourceManifest | None:
        path = manifest_path()
        if not path.exists():
            return None

        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            return SourceManifest(**data)
        except (OSError, TypeError, ValueError):
            return None

    @staticmethod
    def save_manifest(manifest: SourceManifest) -> None:
        manifest_path().write_text(
            json.dumps(manifest.as_dict(), indent=2),
            encoding="utf-8",
        )

    @staticmethod
    def _resolve_citations(ids: list[str], retrieved: list[QueryResult]) -> list[QueryResult]:
        lookup = {item.chunk_id: item for item in retrieved}
        return [lookup[item] for item in ids if item in lookup]

    @staticmethod
    def _format_history(history: list[ChatTurn]) -> str:
        if not history:
            return ""
        trimmed = history[-6:]
        return "\n".join(f"{turn.role.upper()}: {turn.content}" for turn in trimmed)

    @staticmethod
    def _format_context(results: list[QueryResult]) -> str:
        sections: list[str] = []
        for item in results:
            sections.append(
                f"[{item.chunk_id}]\n"
                f"Section: {item.heading_path}\n"
                f"Source file: {item.source_name}\n"
                f"Line range: {item.start_line}-{item.end_line}\n"
                f"Content:\n{item.content}"
            )
        return "\n\n".join(sections)
