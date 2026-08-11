#!/usr/bin/env python3
"""Add a dated quote to content/quotes.md."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from capture_markdown import CaptureError, insert_dated_entry, parse_capture_date

DEFAULT_PATH = Path(__file__).resolve().parents[1] / "content" / "quotes.md"


def quote_markdown(text: str, author: str) -> str:
    quote = text.strip()
    if len(quote) >= 2 and quote[0] in {'"', "“"} and quote[-1] in {'"', "”"}:
        quote = quote[1:-1].strip()
    if not quote:
        raise CaptureError("TEXT is required")
    lines = quote.splitlines()
    if len(lines) == 1:
        rendered = f'> "{lines[0]}"'
    else:
        rendered_lines = [f'> "{lines[0]}']
        rendered_lines.extend(f"> {line}" if line else ">" for line in lines[1:-1])
        rendered_lines.append(f'> {lines[-1]}"')
        rendered = "\n".join(rendered_lines)
    if author.strip():
        rendered += f"\n\n— _{author.strip()}_"
    return rendered


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text", default=os.environ.get("CAPTURE_TEXT", ""))
    parser.add_argument("--author", default=os.environ.get("CAPTURE_AUTHOR", ""))
    parser.add_argument("--date", default=os.environ.get("CAPTURE_DATE", ""))
    parser.add_argument("--path", type=Path, default=DEFAULT_PATH, help=argparse.SUPPRESS)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        if not args.date:
            raise CaptureError("DATE is required")
        entry = quote_markdown(args.text, args.author)
        insert_dated_entry(args.path, parse_capture_date(args.date), entry, args.text)
    except (CaptureError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    print(f"Added quote to {args.path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
