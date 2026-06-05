from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any
import re

import yaml


@dataclass(frozen=True)
class RagChunk:
    chunk_id: str
    text: str
    metadata: dict[str, Any]
    path: Path


def split_frontmatter(raw: str) -> tuple[dict[str, Any], str]:
    if not raw.startswith("---"):
        return {}, raw.strip()

    parts = raw.split("---", 2)
    if len(parts) < 3:
        return {}, raw.strip()

    metadata = yaml.safe_load(parts[1]) or {}
    body = parts[2].strip()
    return metadata, body


def normalize_metadata(value: Any) -> str | int | float | bool:
    if value is None:
        return ""
    if isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, list):
        return " | ".join(str(item) for item in value)
    return str(value)


def clean_extracted_text(text: str) -> str:
    replacements = {
        "â€¢": "-",
        "â€“": "-",
        "â€”": "-",
        "â€˜": "'",
        "â€™": "'",
        "â€œ": '"',
        "â€": '"',
        "Â·": "·",
        "Â": "",
        "Ì¸=": "!=",
        "": "-",
        "": "=",
        "": "-",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = re.sub(r"[\x00-\x08\x0B\x0C\x0E-\x1F]", " ", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def topic_key(topic: str) -> str:
    return "topic_" + "".join(char.lower() if char.isalnum() else "_" for char in topic).strip("_")


def read_chunk(path: Path, root: Path) -> RagChunk:
    raw = path.read_text(encoding="utf-8", errors="replace")
    metadata, body = split_frontmatter(raw)
    body = clean_extracted_text(body)
    chunk_id = str(metadata.get("chunk_id") or path.stem)

    normalized = {key: normalize_metadata(value) for key, value in metadata.items()}
    for topic in metadata.get("topics") or []:
        normalized[topic_key(str(topic))] = True
    normalized["chunk_id"] = chunk_id
    normalized["relative_path"] = str(path.relative_to(root.parent)).replace("\\", "/")

    return RagChunk(chunk_id=chunk_id, text=body, metadata=normalized, path=path)


def iter_chunks(root: Path) -> list[RagChunk]:
    return [read_chunk(path, root) for path in sorted(root.rglob("*.md"))]
