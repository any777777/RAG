from __future__ import annotations

from pathlib import Path
from typing import Sequence

import chromadb
from chromadb.config import Settings

from app.models import ChunkRecord, QueryResult


class ChromaStore:
    def __init__(self, storage_path: str | Path, collection_name: str) -> None:
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)
        self.collection_name = collection_name
        self.client = chromadb.PersistentClient(
            path=str(self.storage_path),
            settings=Settings(anonymized_telemetry=False),
        )

    def recreate_collection(self) -> None:
        try:
            self.client.delete_collection(self.collection_name)
        except Exception:
            pass

        self.client.get_or_create_collection(
            name=self.collection_name,
            metadata={"hnsw:space": "cosine"},
        )

    def has_collection_data(self) -> bool:
        try:
            collection = self.client.get_collection(self.collection_name)
        except Exception:
            return False
        return collection.count() > 0

    def add_chunks(
        self,
        chunks: Sequence[ChunkRecord],
        embeddings: Sequence[Sequence[float]],
    ) -> None:
        if len(chunks) != len(embeddings):
            raise ValueError("Chunk and embedding counts do not match.")

        collection = self.client.get_collection(self.collection_name)
        batch_size = 100

        for start in range(0, len(chunks), batch_size):
            batch_chunks = chunks[start : start + batch_size]
            batch_embeddings = embeddings[start : start + batch_size]
            collection.add(
                ids=[chunk.chunk_id for chunk in batch_chunks],
                documents=[chunk.content for chunk in batch_chunks],
                metadatas=[chunk.to_metadata() for chunk in batch_chunks],
                embeddings=[list(vector) for vector in batch_embeddings],
            )

    def query(self, query_embedding: Sequence[float], top_k: int) -> list[QueryResult]:
        collection = self.client.get_collection(self.collection_name)
        results = collection.query(
            query_embeddings=[list(query_embedding)],
            n_results=top_k,
            include=["documents", "metadatas", "distances"],
        )

        ids = results.get("ids", [[]])[0]
        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]

        query_results: list[QueryResult] = []
        for chunk_id, document, metadata, distance in zip(ids, documents, metadatas, distances):
            query_results.append(
                QueryResult(
                    chunk_id=str(chunk_id),
                    content=str(document),
                    source_path=str(metadata.get("source_path", "")),
                    source_name=str(metadata.get("source_name", "")),
                    heading_path=str(metadata.get("heading_path", "")),
                    start_line=int(metadata.get("start_line", 0)),
                    end_line=int(metadata.get("end_line", 0)),
                    distance=float(distance) if distance is not None else None,
                )
            )

        return query_results
