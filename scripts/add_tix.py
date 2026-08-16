#!/usr/bin/env python3
"""Add a dated, already-organized entry to content/ideas.md (/tix/)."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from capture_markdown import CaptureError, insert_dated_entry, parse_capture_date

DEFAULT_PATH = Path(__file__).resolve().parents[1] / "content" / "ideas.md"


def tix_markdown(text: str, title: str) -> str:
    body = text.strip()
    if not body:
        raise CaptureError("TEXT is required")
    return f"### {title.strip()}\n\n{body}" if title.strip() else body


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text", default=os.environ.get("CAPTURE_TEXT", ""))
    parser.add_argument("--title", default=os.environ.get("CAPTURE_TITLE", ""))
    parser.add_argument("--date", default=os.environ.get("CAPTURE_DATE", ""))
    parser.add_argument("--path", type=Path, default=DEFAULT_PATH, help=argparse.SUPPRESS)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        if not args.date:
            raise CaptureError("DATE is required")
        entry = tix_markdown(args.text, args.title)
        insert_dated_entry(args.path, parse_capture_date(args.date), entry, args.text)
    except (CaptureError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(f"Added TIX entry to {args.path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
