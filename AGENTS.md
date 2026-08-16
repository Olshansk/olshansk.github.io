# AGENTS.md

Project-specific instructions for AI agents working on olshansky.info.

## Makefile First

**Always run `make help` before performing any operation manually.** The Makefile provides helpers for common tasks including content creation, tagging, resume generation, and more. Use these targets instead of running commands or creating files by hand.

## Resume Guidelines

- **Resume must never exceed 1 page** - When updating `cv/DanielOlshanskyResume.tex`, ensure the compiled PDF fits on a single page
- Run `make resume_generate` after changes to verify page count
- If content overflows, reduce descriptions or remove less relevant entries rather than shrinking fonts

## Media Files for Posts/Thoughts

### Location
- Posts: `static/images/posts/`
- Thoughts: `static/images/thoughts/`

### Naming Convention
- Format: `{YYYY-MM-DD}-{slug}-{description}.{ext}`
- Example: `2026-01-20-mad-scientists-quadrants.webp`
- The date prefix should match the post/thought date

### Renaming Posts/Thoughts
When changing the date of a post or thought, update ALL of:
1. Filename: `content/{posts,thoughts}/{date}-{slug}.md`
2. Frontmatter: `date:` field in the markdown
3. Media files: Rename in `static/images/{posts,thoughts}/`
4. References: Update image/video paths in the markdown content
5. Git: Unstage old filenames if they were previously staged

## Quotes and TIX Captures

- Use `make add_quote TEXT="..." AUTHOR="..." DATE=YYYY-MM-DD`; do not edit `content/quotes.md` directly.
- Use `make add_tix TEXT="..." TITLE="..." DATE=YYYY-MM-DD`; do not edit `content/ideas.md` directly.
- Pass dates explicitly in ISO format so cloud-runner timezones cannot change the intended date.
- Preserve quote text verbatim and never invent an attribution.
- Organize TIX voice/text captures in the `add-tix` skill; the Make target only performs deterministic insertion.
- Routine capture pull requests must change only their corresponding destination file.

## Python (uv)

- All Python in this repo runs through `uv`; never call `python3`, `pip`, or a `.venv/bin` binary directly.
- Run scripts with `uv run python scripts/<name>.py` and tools with `uv run <tool>` (for example `uv run pytest`).
- `make test` runs the capture tests; `make py_sync` rebuilds the environment from `uv.lock`.
- Commit `uv.lock`; CI installs with `uv sync --locked` so a stale lockfile fails the build instead of silently resolving.
- Capture scripts in `scripts/` are deliberately stdlib-only — add a dependency only if it is genuinely needed.
- Legacy one-offs in `migration_scripts/` need the optional group: `uv run --group migration python migration_scripts/<name>.py`.

## Book Notes Workflow (Snipd Exports)
- When consolidating Snipd exports in `book_notes/`, unzip nested `ExportBlock-...-Part-1.zip` files before parsing.
- Consolidate into a single markdown file (example: `book_notes/breaking-history-consolidated.md`).
- Include source transcript under each snip as blockquotes with quoted lines: `> "..."`; preserve blank lines as `> ""` to keep paragraph breaks.
- After consolidation, it is safe to delete the raw zip exports, `Private & Shared*` folders, and the `extracted/` staging directory.
