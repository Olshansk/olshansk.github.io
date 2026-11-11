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

## Today I X and reading excerpts

- For a supplied reading excerpt and source URL, use `make new_reading TITLE="..."` to create an individual entry under `content/tix/`, tagged `["TIX", "TodayIRead"]`.
- Preserve the excerpt verbatim and link the source with its author(s). Set frontmatter `author` to the credited source author(s), not Daniel.
- Check for duplicate excerpt/source pairs first. Add commentary only when requested.
- The user's standing instruction is to create blog and TIX/reading content with `draft: false`, so it publishes when its PR is merged. Existing unrelated drafts are not part of a selected publishing batch.
- `/index.xml` includes all published content. `/posts/index.xml` is blog-only. `/tix/index.xml` includes all Today I X entries; `/tags/todayiquoted/index.xml` and `/tags/todayiread/index.xml` filter quotes and readings. Keep TIX entries out of the Posts list; preserve source attribution.
- Use `make new_blog`, `make new_quote`, or `make new_excerpt` for new captures. Each target is authorized to commit only its entry in an isolated branch and open its own draft PR. Never merge automatically. Content uses `draft: false`; a draft GitHub PR is a separate review state.
- Every TIX entry has exactly two classification tags: `TIX` first, then one CamelCase `TodayI…` action, such as `TodayIRead`, `TodayIIdeated`, `TodayIQuoted`, or `TodayIFound`. Classify original ideas as `TodayIIdeated`; classify reading notes and excerpts as `TodayIRead`.
- Store tag values without `#`; render them with `#` on listing badges and article tag links (e.g. `#TIX #TodayIIdeated`). Do not create abbreviated or spaced variants such as `TIR` or `Today I Read`, or redundant `quote`/`excerpt` tags. Tags are the only classification source; do not add `capture_kind` or `entry_type` fields.
- Blog captures keep `blog` and their existing topic tags. The older `new_post`, `new_reading`, and `add_quote` targets remain local helpers.
- `make add_quote` remains the helper for the existing general-purpose `content/quotes.md` log.

## Close out reviewed content

- For repository sync, health checks, and the three most recent TIX PRs to
  review, use [olsh-tix-prep](.agents/skills/olsh-tix-prep/SKILL.md). Preparation
  does not authorize content edits, PR merges, or branch deletion.
- For an explicitly requested proofreading and PR close-out batch, use
  [close-out-tix](.agents/skills/close-out-tix/SKILL.md). Verify the selected
  posts against the local tracker, proofread, validate, squash-merge, remove
  their exact local and remote branches, and finish on updated `main`.
- Before closing out a selected content PR for merge/publication, set its content
  frontmatter to `draft: false` and verify the page in a normal production build.
  Hugo `draft: true` hides content. Inspection and push-only requests do not
  authorize merging, publication, or cleanup; leave unrelated drafts untouched.

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
