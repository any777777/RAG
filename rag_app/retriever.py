from __future__ import annotations

import re
from dataclasses import dataclass
from functools import lru_cache

from config import DEFAULT_TOP_K
from chunks import topic_key
from chunks import iter_chunks
from config import RAG_CHUNKS_DIR
from embeddings import embed_texts
from indexer import get_collection


@dataclass(frozen=True)
class SearchResult:
    chunk_id: str
    text: str
    metadata: dict
    distance: float
    score: float


def tokenize(text: str) -> set[str]:
    return {token.lower() for token in re.findall(r"[\w\u0600-\u06FF]+", text) if len(token) > 2}


def expand_query(query: str) -> str:
    lowered = query.lower()
    additions: list[str] = []
    if "free space" in lowered or "free-space" in lowered or "path loss" in lowered or "fsl" in lowered:
        additions.extend(["free-space path loss", "free-space loss", "path loss", "FSL"])
    if "backprop" in lowered or "back propagation" in lowered or "back-propagation" in lowered:
        additions.extend(["backpropagation", "back propagation", "delta rule", "multilayer perceptron"])
    return " ".join([query, *additions])


def lexical_bonus(query: str, document: str) -> float:
    expanded = expand_query(query)
    query_tokens = tokenize(expanded)
    if not query_tokens:
        return 0.0
    doc_tokens = tokenize(document)
    overlap = len(query_tokens & doc_tokens)
    token_score = min(overlap / max(len(query_tokens), 1), 1.0)
    phrase_score = 0.0
    lowered_doc = document.lower()
    for phrase in ["free-space path loss", "free-space loss", "path loss", "fsl", "backpropagation", "delta rule"]:
        if phrase in expanded.lower() and phrase in lowered_doc:
            phrase_score += 0.2
    return min((token_score * 0.2) + phrase_score, 0.7)


@lru_cache(maxsize=1)
def local_chunks():
    return iter_chunks(RAG_CHUNKS_DIR)


def search(query: str, top_k: int = DEFAULT_TOP_K, topic: str = "All") -> list[SearchResult]:
    collection = get_collection()
    where = None
    if topic and topic != "All":
        where = {topic_key(topic): True}

    expanded_query = expand_query(query)
    query_embedding = embed_texts([expanded_query])[0]
    raw = collection.query(
        query_embeddings=[query_embedding],
        n_results=max(top_k * 3, top_k),
        where=where,
        include=["documents", "metadatas", "distances"],
    )

    merged: dict[str, SearchResult] = {}
    ids = raw.get("ids", [[]])[0]
    documents = raw.get("documents", [[]])[0]
    metadatas = raw.get("metadatas", [[]])[0]
    distances = raw.get("distances", [[]])[0]

    for chunk_id, document, metadata, distance in zip(ids, documents, metadatas, distances):
        base_score = 1.0 - float(distance)
        score = base_score + lexical_bonus(query, document)
        merged[chunk_id] = SearchResult(
            chunk_id=chunk_id,
            text=document,
            metadata=metadata or {},
            distance=float(distance),
            score=score,
        )

    lexical_candidates: list[SearchResult] = []
    topic_flag = topic_key(topic) if topic and topic != "All" else None
    for chunk in local_chunks():
        if topic_flag and chunk.metadata.get(topic_flag) is not True:
            continue
        bonus = lexical_bonus(query, chunk.text)
        if bonus <= 0:
            continue
        lexical_candidates.append(
            SearchResult(
                chunk_id=chunk.chunk_id,
                text=chunk.text,
                metadata=chunk.metadata,
                distance=1.0 - bonus,
                score=bonus,
            )
        )

    for candidate in sorted(lexical_candidates, key=lambda item: item.score, reverse=True)[: top_k * 3]:
        existing = merged.get(candidate.chunk_id)
        if existing is None or candidate.score > existing.score:
            merged[candidate.chunk_id] = candidate

    return sorted(merged.values(), key=lambda item: item.score, reverse=True)[:top_k]
