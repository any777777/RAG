from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass
class Paragraph:
    text: str
    heading_path: tuple[str, ...]
    start_line: int
    end_line: int


@dataclass
class ChunkRecord:
    chunk_id: str
    chunk_index: int
    content: str
    source_path: str
    source_name: str
    heading_path: str
    start_line: int
    end_line: int
    word_count: int

    def to_metadata(self) -> dict[str, int | str]:
        return {
            "chunk_id": self.chunk_id,
            "chunk_index": self.chunk_index,
            "source_path": self.source_path,
            "source_name": self.source_name,
            "heading_path": self.heading_path,
            "start_line": self.start_line,
            "end_line": self.end_line,
            "word_count": self.word_count,
        }


@dataclass
class QueryResult:
    chunk_id: str
    content: str
    source_path: str
    source_name: str
    heading_path: str
    start_line: int
    end_line: int
    distance: float | None = None

    def citation_label(self) -> str:
        return (
            f"[{self.chunk_id}] {self.heading_path} "
            f"({self.source_name}, lines {self.start_line}-{self.end_line})"
        )


@dataclass
class SourceManifest:
    source_path: str
    source_name: str
    chunk_size: int
    chunk_overlap: int
    chunk_count: int
    collection_name: str
    built_at: str

    def as_dict(self) -> dict[str, int | str]:
        return asdict(self)


@dataclass
class BuildResult:
    manifest: SourceManifest


@dataclass
class AnswerResult:
    answer: str
    citations: list[QueryResult]
    unsupported: bool


@dataclass
class ChatTurn:
    role: str
    content: str
