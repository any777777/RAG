from __future__ import annotations

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SLIDES_OUTPUT_DIR = PROJECT_ROOT / "Slides" / "Output"
LOCAL_DATA_CHUNKS_DIR = PROJECT_ROOT / "data" / "rag-chunks"
SLIDES_RAG_CHUNKS_DIR = SLIDES_OUTPUT_DIR / "rag-chunks"
RAG_CHUNKS_DIR = LOCAL_DATA_CHUNKS_DIR if LOCAL_DATA_CHUNKS_DIR.exists() else SLIDES_RAG_CHUNKS_DIR

APP_DIR = PROJECT_ROOT / "rag_app"
CHROMA_DIR = APP_DIR / ".chroma"
MANIFEST_PATH = APP_DIR / ".index_manifest.json"

COLLECTION_NAME = "slides_chunks_v1"
EMBEDDING_MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
OLLAMA_MODEL = "qwen3:1.7b"
DEFAULT_TOP_K = 8

TOPIC_OPTIONS = [
    "All",
    "Machine Learning",
    "Satellite Communications",
    "Exams and Questions",
    "Lecturer Notes and Photos",
    "References and Textbooks",
    "Unclassified",
]
