"""Create one blog, quote, or excerpt entry in an isolated draft pull request."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
import uuid
from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]


def build_entry(kind: str, values: dict[str, str]) -> tuple[Path, str]:
    """Validate one capture and render its frontmatter and unmodified body.

    How:
    1. Validate the title, local date, body, and source attribution.
    2. Assign the section and content tag without changing supplied prose.
    3. Render JSON-compatible YAML scalars and a dated destination path.
    """
    title = values.get("TITLE", "").strip()
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    if not title or not slug:
        raise ValueError("TITLE must contain at least one ASCII letter or number")
    day = values.get("DATE") or datetime.now(ZoneInfo("America/Los_Angeles")).date().isoformat()
    datetime.strptime(day, "%Y-%m-%d")
    if kind not in {"blog", "quote", "excerpt"}:
        raise ValueError("Expected blog, quote, or excerpt")
    body = values.get("TEXT", "")
    if values.get("BODY_FILE"):
        if body:
            raise ValueError("Supply TEXT or BODY_FILE, not both")
        body = Path(values["BODY_FILE"]).expanduser().read_text()
    if not body.strip():
        raise ValueError("Supply TEXT or BODY_FILE with the entry's complete text")
    source = values.get("SOURCE", "").strip()
    author = values.get("AUTHOR", "").strip()
    if kind == "excerpt" and (not source or not author):
        raise ValueError("Excerpts require SOURCE and AUTHOR")
    if source and (urlsplit(source).scheme not in {"http", "https"} or not urlsplit(source).netloc):
        raise ValueError("SOURCE must be an absolute HTTP(S) URL")
    fields = {"title": title, "date": day, "draft": kind == "blog", "tags": [kind]}
    if kind != "blog":
        fields.update(ShowToc=False, ShowReadingTime=False, ShowWordCount=False, ShowPostNavLinks=False)
        if kind == "excerpt":
            fields["tags"].append("TodayIRead")
        # An empty source author must not inherit the site's curator as attribution.
        fields["author"] = [author]
        body = "\n".join("> " + line if line else ">" for line in body.split("\n"))
        attribution = author
        if source:
            attribution += (", " if attribution else "") + f"<{source}>"
        if attribution:
            body += "\n\n— " + attribution
    header = "\n".join(f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in fields.items())
    section = "posts" if kind == "blog" else "reading"
    return Path("content") / section / f"{day}-{slug}.md", f"---\n{header}\n---\n\n{body}\n"


def run(*args: str, cwd: Path = ROOT) -> str:
    """Run a checked command and return its standard output."""
    return subprocess.run(args, cwd=cwd, check=True, text=True, stdout=subprocess.PIPE).stdout.strip()


def main() -> int:
    """Validate, isolate, check, and submit a single content PR.

    How:
    1. Render the supplied entry and verify GitHub authentication.
    2. Fetch main and create a unique branch in a temporary worktree.
    3. Reject duplicate captures and write only the new entry.
    4. Run capture tests and a production Hugo build before committing.
    5. Push the branch and open a custom draft PR, retaining failed work for recovery.
    """
    worktree = None
    try:
        kind = sys.argv[1]
        path, content = build_entry(kind, dict(os.environ))
        run("gh", "auth", "status")
        run("git", "fetch", "origin", "main")
        branch = f"codex/{kind}-{path.stem}-{uuid.uuid4().hex[:8]}"
        worktree = Path(tempfile.mkdtemp(prefix="blog-capture-")) / "worktree"
        run("git", "worktree", "add", "-b", branch, str(worktree), "origin/main")
        destination = worktree / path
        if destination.exists():
            raise ValueError(f"Entry already exists: {path}")
        if kind != "blog":
            body = content.split("---\n\n", 1)[1]
            for existing in (worktree / "content/reading").glob("*.md"):
                if body.strip() in existing.read_text():
                    raise ValueError(f"Duplicate capture: {existing.name}")
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content)
        run("git", "submodule", "update", "--init", "--recursive", "--", "themes/PaperMod", cwd=worktree)
        run("make", "test", cwd=worktree)
        run("hugo", "--environment", "production", cwd=worktree)
        run("git", "diff", "--check", cwd=worktree)
        run("git", "add", "--", str(path), cwd=worktree)
        title = os.environ["TITLE"].strip()
        run("git", "commit", "-m", f"docs({kind}): {title}", cwd=worktree)
        run("git", "push", "-u", "origin", branch, cwd=worktree)
        body_file = worktree.parent / "pr-body.md"
        body_file.write_text(
            f"Add the {kind} entry **{title}** at `{path}`.\n\n"
            f"Content tag: `{kind}`. Only this entry is included.\n\n"
            "Validation: `make test`, production Hugo build, and `git diff --check`.\n"
        )
        stamp = datetime.now(ZoneInfo("America/Los_Angeles")).strftime("%d/%m/%y")
        url = run("gh", "pr", "create", "--draft", "--base", "main", "--head", branch,
                  "--title", f"[{stamp}] {kind.title()}: {title}", "--body-file", str(body_file), cwd=worktree)
        print(url)
        body_file.unlink()
        print(f"PR checkout retained at {worktree}")
        return 0
    except (ValueError, OSError, subprocess.CalledProcessError, IndexError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        if isinstance(exc, subprocess.CalledProcessError) and exc.stdout:
            print(exc.stdout, file=sys.stderr)
        if worktree:
            print(f"Capture work retained at {worktree}; inspect before retrying.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
