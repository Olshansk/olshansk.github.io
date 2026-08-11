"""Shared deterministic Markdown insertion helpers for quote and TIX captures."""

from __future__ import annotations

import os
import re
import tempfile
import unicodedata
from datetime import date
from pathlib import Path

CAPTURE_MARKER = "<!-- captures:start -->"
CAPTURE_END_MARKER = "<!-- captures:end -->"
DATE_HEADER_RE = re.compile(
    r'<div class="year-header">\n\s*<h2 class="year-title">([^<]+)</h2>\n</div>'
)


class CaptureError(ValueError):
    """Raised when a capture cannot be inserted safely."""


def parse_capture_date(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise CaptureError(f"DATE must be a valid ISO date (YYYY-MM-DD): {value!r}") from exc


def normalize_for_duplicate(value: str) -> str:
    value = unicodedata.normalize("NFKC", value)
    value = value.translate(str.maketrans({"“": '"', "”": '"', "‘": "'", "’": "'"}))
    value = re.sub(r"<br\s*/?>", "", value, flags=re.IGNORECASE)
    value = re.sub(r"[*_>#]", "", value)
    value = value.strip().strip('"').strip()
    return " ".join(value.casefold().split())


def _is_duplicate(original: str, duplicate: str) -> bool:
    """Match whole Markdown blocks, with substring matching only for long captures."""
    blocks = re.split(r"\n\s*\n", original)
    if any(normalize_for_duplicate(block) == duplicate for block in blocks):
        return True
    return len(duplicate) >= 50 and duplicate in normalize_for_duplicate(original)


def _dated_sections(text: str, marker_end: int, managed_end: int) -> list[tuple[re.Match[str], date]]:
    sections: list[tuple[re.Match[str], date]] = []
    for match in DATE_HEADER_RE.finditer(text, marker_end, managed_end):
        try:
            month, day, year = (int(part) for part in match.group(1).split("/"))
            parsed = date(year, month, day)
        except (ValueError, TypeError):
            continue
        sections.append((match, parsed))
    return sections


def _atomic_write(path: Path, text: str) -> None:
    stat = path.stat()
    fd, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
        os.chmod(temporary_name, stat.st_mode)
        os.replace(temporary_name, path)
    except BaseException:
        try:
            os.unlink(temporary_name)
        except FileNotFoundError:
            pass
        raise


def insert_dated_entry(
    path: Path,
    capture_date: date,
    entry: str,
    duplicate_text: str,
) -> None:
    """Insert an entry into an existing or new reverse-chronological date group."""
    original = path.read_text(encoding="utf-8")
    marker_index = original.find(CAPTURE_MARKER)
    if marker_index < 0:
        raise CaptureError(f"Capture marker missing from {path}")

    duplicate = normalize_for_duplicate(duplicate_text)
    if not duplicate:
        raise CaptureError("Capture text cannot be empty")
    if _is_duplicate(original, duplicate):
        raise CaptureError(f"Possible duplicate found in {path}; no changes made")

    marker_end = marker_index + len(CAPTURE_MARKER)
    end_marker_index = original.find(CAPTURE_END_MARKER, marker_end)
    managed_end = end_marker_index if end_marker_index >= 0 else len(original)
    sections = _dated_sections(original, marker_end, managed_end)
    date_header = (
        '<div class="year-header">\n'
        f'  <h2 class="year-title">{capture_date.strftime("%m/%d/%Y")}</h2>\n'
        "</div>"
    )
    clean_entry = entry.strip()

    for index, (match, section_date) in enumerate(sections):
        if section_date == capture_date:
            next_header = DATE_HEADER_RE.search(original, match.end(), managed_end)
            section_end = next_header.start() if next_header else managed_end
            prefix = original[:section_end].rstrip()
            suffix = original[section_end:].lstrip("\n")
            updated = f"{prefix}\n\n{clean_entry}\n"
            if suffix:
                updated += f"\n{suffix}"
            _atomic_write(path, updated)
            return

    insertion_point = marker_end
    for match, section_date in sections:
        if section_date < capture_date:
            insertion_point = match.start()
            break
        insertion_point = match.end()
    else:
        if sections:
            insertion_point = managed_end

    if sections and all(section_date > capture_date for _, section_date in sections):
        # Insert after the final dated section but before any non-date legacy heading/content.
        last_match = sections[-1][0]
        trailing_header = DATE_HEADER_RE.search(original, last_match.end(), managed_end)
        insertion_point = trailing_header.start() if trailing_header else managed_end

    prefix = original[:insertion_point].rstrip()
    suffix = original[insertion_point:].lstrip("\n")
    block = f"{date_header}\n\n{clean_entry}"
    updated = f"{prefix}\n\n{block}\n"
    if suffix:
        updated += f"\n{suffix}"
    _atomic_write(path, updated)
