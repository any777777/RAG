from __future__ import annotations

import json
import os
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

from dotenv import load_dotenv


APP_NAME = "Markdown RAG Chat"
APP_SLUG = "MarkdownRAGChat"
COLLECTION_NAME = "markdown_rag_chunks"
EMBEDDING_MODEL = "gemini-embedding-001"
CHAT_MODEL = "gemini-2.5-flash"


@dataclass
class AppSettings:
    selected_markdown: str = ""
    chunk_size: int = 350
    chunk_overlap: int = 60
    top_k: int = 5


def project_root() -> Path:
    return Path(__file__).resolve().parent.parent


def runtime_base_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return project_root()


def app_data_dir() -> Path:
    if os.name == "nt":
        base = Path(os.environ.get("LOCALAPPDATA", project_root()))
    else:
        base = Path.home()
    path = base / APP_SLUG
    path.mkdir(parents=True, exist_ok=True)
    return path


def chroma_dir() -> Path:
    path = app_data_dir() / "chroma"
    path.mkdir(parents=True, exist_ok=True)
    return path


def settings_path() -> Path:
    return app_data_dir() / "settings.json"


def manifest_path() -> Path:
    return app_data_dir() / "manifest.json"


def load_environment() -> None:
    seen: set[Path] = set()
    for base in (runtime_base_dir(), project_root(), Path.cwd()):
        env_path = base / ".env"
        if env_path not in seen and env_path.exists():
            load_dotenv(env_path, override=False)
            seen.add(env_path)

    api_key = os.getenv("API_KEY")
    if api_key:
        os.environ.setdefault("GEMINI_API_KEY", api_key)


def load_settings() -> AppSettings:
    path = settings_path()
    if not path.exists():
        return AppSettings()

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError, TypeError):
        return AppSettings()

    try:
        return AppSettings(**data)
    except TypeError:
        return AppSettings()


def save_settings(settings: AppSettings) -> None:
    settings_path().write_text(
        json.dumps(asdict(settings), indent=2),
        encoding="utf-8",
    )
