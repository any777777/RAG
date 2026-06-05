from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import chromadb

from chunks import RagChunk, iter_chunks
from config import CHROMA_DIR, COLLECTION_NAME, MANIFEST_PATH, RAG_CHUNKS_DIR
from embeddings import embed_texts


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for block in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def build_manifest(chunks: list[RagChunk]) -> dict[str, object]:
    files = []
    for chunk in chunks:
        files.append(
            {
                "chunk_id": chunk.chunk_id,
                "path": str(chunk.path.relative_to(RAG_CHUNKS_DIR)).replace("\\", "/"),
                "sha256": sha256_file(chunk.path),
            }
        )
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "chunk_count": len(chunks),
        "files": files,
    }


def load_manifest() -> dict[str, object] | None:
    if not MANIFEST_PATH.exists():
        return None
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def manifest_matches(current: dict[str, object], previous: dict[str, object] | None) -> bool:
    if not previous:
        return False
    return current.get("chunk_count") == previous.get("chunk_count") and current.get("files") == previous.get("files")


def get_collection():
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    return client.get_or_create_collection(name=COLLECTION_NAME, metadata={"hnsw:space": "cosine"})


def reset_collection():
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass
    return client.get_or_create_collection(name=COLLECTION_NAME, metadata={"hnsw:space": "cosine"})


def build_index(force: bool = False) -> dict[str, object]:
    if not RAG_CHUNKS_DIR.exists():
        raise FileNotFoundError(f"RAG chunks folder not found: {RAG_CHUNKS_DIR}")

    chunks = iter_chunks(RAG_CHUNKS_DIR)
    current_manifest = build_manifest(chunks)
    previous_manifest = load_manifest()

    if not force and manifest_matches(current_manifest, previous_manifest):
        collection = get_collection()
        if collection.count() == current_manifest["chunk_count"]:
            return {
                "status": "unchanged",
                "chunk_count": current_manifest["chunk_count"],
                "indexed_count": collection.count(),
                "collection": COLLECTION_NAME,
            }

    collection = reset_collection()
    batch_size = 64
    for start in range(0, len(chunks), batch_size):
        batch = chunks[start : start + batch_size]
        documents = [chunk.text for chunk in batch]
        embeddings = embed_texts(documents)
        collection.add(
            ids=[chunk.chunk_id for chunk in batch],
            documents=documents,
            metadatas=[chunk.metadata for chunk in batch],
            embeddings=embeddings,
        )

    MANIFEST_PATH.write_text(json.dumps(current_manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return {
        "status": "rebuilt",
        "chunk_count": current_manifest["chunk_count"],
        "indexed_count": collection.count(),
        "collection": COLLECTION_NAME,
    }


def index_status() -> dict[str, object]:
    collection = get_collection()
    manifest = load_manifest()
    return {
        "collection": COLLECTION_NAME,
        "indexed_count": collection.count(),
        "manifest_chunk_count": manifest.get("chunk_count") if manifest else None,
        "manifest_exists": manifest is not None,
        "chroma_dir": str(CHROMA_DIR),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Build or inspect the local Slides RAG index.")
    parser.add_argument("--build", action="store_true", help="Build the Chroma index when needed.")
    parser.add_argument("--force", action="store_true", help="Force rebuilding the Chroma index.")
    parser.add_argument("--status", action="store_true", help="Show index status.")
    args = parser.parse_args()

    if args.build:
        print(json.dumps(build_index(force=args.force), ensure_ascii=False, indent=2))
    elif args.status:
        print(json.dumps(index_status(), ensure_ascii=False, indent=2))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
