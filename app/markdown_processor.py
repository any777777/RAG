from __future__ import annotations

import re
from pathlib import Path

from app.models import ChunkRecord, Paragraph


FENCE_RE = re.compile(r"^\s*(```|~~~)")
HEADING_RE = re.compile(r"^\s{0,3}(#{1,6})\s+(.*)$")
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\([^)]+\)")
LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
HTML_RE = re.compile(r"<[^>]+>")
ORDERED_LIST_RE = re.compile(r"^\s*\d+[.)]\s+")
UNORDERED_LIST_RE = re.compile(r"^\s*[-*+]\s+")


def _count_words(text: str) -> int:
    return len(text.split())


def _clean_heading_text(text: str) -> str:
    text = LINK_RE.sub(r"\1", text)
    text = text.replace("`", "").replace("*", "").replace("_", "")
    text = text.replace("#", "").strip()
    return re.sub(r"\s+", " ", text)


def _clean_markdown_line(text: str, in_code_block: bool) -> str:
    raw = text.rstrip("\n").rstrip("\r")
    if in_code_block:
        return raw.rstrip()

    cleaned = IMAGE_RE.sub(r"\1", raw)
    cleaned = LINK_RE.sub(r"\1", cleaned)
    cleaned = HTML_RE.sub(" ", cleaned)
    cleaned = re.sub(r"^\s{0,3}>\s?", "", cleaned)
    cleaned = ORDERED_LIST_RE.sub("", cleaned)
    cleaned = UNORDERED_LIST_RE.sub("", cleaned)
    cleaned = cleaned.replace("`", "")
    cleaned = cleaned.replace("**", "").replace("__", "").replace("~~", "")
    cleaned = cleaned.replace("|", " ")
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned.strip()


def _strip_front_matter(lines: list[str]) -> list[str]:
    if not lines or lines[0].strip() != "---":
        return lines

    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return lines[index + 1 :]
    return lines


def parse_markdown(markdown_path: str | Path) -> list[Paragraph]:
    path = Path(markdown_path).expanduser().resolve()
    raw_text = path.read_text(encoding="utf-8", errors="ignore")
    lines = _strip_front_matter(raw_text.splitlines())

    paragraphs: list[Paragraph] = []
    heading_stack: list[str] = ["Document Intro"]
    paragraph_lines: list[str] = []
    paragraph_start: int | None = None
    paragraph_mode = "text"
    in_code_block = False

    def flush(end_line: int) -> None:
        nonlocal paragraph_lines, paragraph_start, paragraph_mode
        if paragraph_start is None or not paragraph_lines:
            paragraph_lines = []
            paragraph_start = None
            paragraph_mode = "text"
            return

        if paragraph_mode == "code":
            text = "\n".join(paragraph_lines).strip()
        else:
            text = " ".join(paragraph_lines).strip()

        if text:
            paragraphs.append(
                Paragraph(
                    text=text,
                    heading_path=tuple(heading_stack),
                    start_line=paragraph_start,
                    end_line=end_line,
                )
            )

        paragraph_lines = []
        paragraph_start = None
        paragraph_mode = "text"

    for line_number, line in enumerate(lines, start=1):
        if FENCE_RE.match(line):
            if in_code_block:
                flush(line_number - 1)
                in_code_block = False
            else:
                flush(line_number - 1)
                in_code_block = True
                paragraph_mode = "code"
            continue

        if in_code_block:
            if paragraph_start is None:
                paragraph_start = line_number
            paragraph_lines.append(line.rstrip("\n").rstrip("\r"))
            continue

        heading_match = HEADING_RE.match(line)
        if heading_match:
            flush(line_number - 1)
            level = len(heading_match.group(1))
            title = _clean_heading_text(heading_match.group(2))
            while len(heading_stack) >= level:
                heading_stack.pop()
            heading_stack.append(title or f"Heading {level}")
            continue

        cleaned = _clean_markdown_line(line, in_code_block=False)
        if not cleaned:
            flush(line_number - 1)
            continue

        if paragraph_start is None:
            paragraph_start = line_number
        paragraph_mode = "text"
        paragraph_lines.append(cleaned)

    flush(len(lines))

    if not paragraphs:
        raise ValueError("The selected Markdown file does not contain extractable text.")

    return paragraphs


def build_chunks(
    paragraphs: list[Paragraph],
    source_path: str | Path,
    chunk_size: int,
    chunk_overlap: int,
) -> list[ChunkRecord]:
    if chunk_size < 50:
        raise ValueError("Chunk size must be at least 50 words.")
    if chunk_overlap < 0:
        raise ValueError("Chunk overlap cannot be negative.")
    if chunk_overlap >= chunk_size:
        raise ValueError("Chunk overlap must be smaller than chunk size.")

    source = Path(source_path).expanduser().resolve()
    source_name = source.name
    groups: list[list[Paragraph]] = []
    current_group: list[Paragraph] = []
    current_heading: tuple[str, ...] | None = None

    for paragraph in paragraphs:
        if current_heading != paragraph.heading_path and current_group:
            groups.append(current_group)
            current_group = []
        current_heading = paragraph.heading_path
        current_group.append(paragraph)

    if current_group:
        groups.append(current_group)

    chunks: list[ChunkRecord] = []
    chunk_index = 0

    for group in groups:
        group_heading = " > ".join(group[0].heading_path)
        start = 0
        while start < len(group):
            total_words = 0
            end = start
            selected: list[Paragraph] = []

            while end < len(group):
                paragraph = group[end]
                paragraph_words = _count_words(paragraph.text)
                if selected and total_words + paragraph_words > chunk_size and total_words >= int(
                    chunk_size * 0.65
                ):
                    break
                selected.append(paragraph)
                total_words += paragraph_words
                end += 1
                if total_words >= chunk_size:
                    break

            if not selected:
                selected.append(group[start])
                end = start + 1
                total_words = _count_words(group[start].text)

            body = "\n\n".join(paragraph.text for paragraph in selected)
            content = (
                f"Chunk ID: chunk-{chunk_index + 1:04d}\n"
                f"Section: {group_heading}\n"
                f"Source file: {source_name}\n"
                f"Line range: {selected[0].start_line}-{selected[-1].end_line}\n\n"
                f"{body}"
            )

            chunk = ChunkRecord(
                chunk_id=f"chunk-{chunk_index + 1:04d}",
                chunk_index=chunk_index,
                content=content,
                source_path=str(source),
                source_name=source_name,
                heading_path=group_heading,
                start_line=selected[0].start_line,
                end_line=selected[-1].end_line,
                word_count=total_words,
            )
            chunks.append(chunk)
            chunk_index += 1

            if end >= len(group):
                break

            backtrack_words = 0
            new_start = end
            while new_start > start and backtrack_words < chunk_overlap:
                new_start -= 1
                backtrack_words += _count_words(group[new_start].text)

            start = new_start if new_start > start else min(start + 1, len(group) - 1)

    if not chunks:
        raise ValueError("No chunks were generated from the Markdown file.")

    return chunks
