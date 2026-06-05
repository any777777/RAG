from __future__ import annotations

import argparse
import sys

from config import COLLECTION_NAME, DEFAULT_TOP_K, OLLAMA_MODEL
from generator import OllamaUnavailable, answer_question
from indexer import index_status
from retriever import search


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def check_index() -> dict[str, object]:
    status = index_status()
    require(status["indexed_count"] == 3101, f"Expected 3101 indexed chunks, got {status['indexed_count']}")
    require(status["manifest_chunk_count"] == 3101, f"Expected manifest count 3101, got {status['manifest_chunk_count']}")
    require(status["collection"] == COLLECTION_NAME, f"Unexpected collection: {status['collection']}")
    return status


def check_retrieval() -> dict[str, list[str]]:
    cases = [
        ("What is backpropagation?", "Machine Learning"),
        ("اشرح free space path loss", "Satellite Communications"),
        ("What are satellite communication services?", "Satellite Communications"),
    ]
    summary: dict[str, list[str]] = {}
    for query, topic in cases:
        results = search(query, top_k=DEFAULT_TOP_K, topic=topic)
        require(results, f"No retrieval results for query={query!r}, topic={topic!r}")
        require(
            any(topic in str(result.metadata.get("topics", "")) for result in results),
            f"No result matched requested topic={topic!r}",
        )
        summary[f"{topic}: {query}"] = [result.chunk_id for result in results[:3]]
    return summary


def check_ollama_generation() -> str:
    results = search("What is backpropagation? Answer briefly.", top_k=3, topic="Machine Learning")
    answer = answer_question("What is backpropagation? Answer briefly.", results, model=OLLAMA_MODEL)
    require(len(answer) > 80, "Ollama answer is unexpectedly short")
    require("Source" in answer or "source" in answer or "المصادر" in answer, "Answer did not cite sources")
    return answer[:500]


def main() -> int:
    parser = argparse.ArgumentParser(description="Smoke-test the local Slides RAG app.")
    parser.add_argument("--with-ollama", action="store_true", help="Also test answer generation through Ollama.")
    args = parser.parse_args()

    try:
        status = check_index()
        retrieval = check_retrieval()
        print("INDEX_OK", status)
        print("RETRIEVAL_OK", retrieval)
        if args.with_ollama:
            try:
                answer_preview = check_ollama_generation()
            except OllamaUnavailable as exc:
                raise AssertionError(str(exc)) from exc
            print("OLLAMA_OK", answer_preview)
        print("SMOKE_OK")
        return 0
    except Exception as exc:
        print(f"SMOKE_FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

