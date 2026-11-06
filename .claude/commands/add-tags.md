---
description: Auto-generate tags for a blog post or thought
---

Read the `.file` file to get the path of the target content file, then read that content file and analyze it.

Based on the content, suggest appropriate tags and update the file's frontmatter `tags` field.

## TIX entries

For `content/tix/`, `content/ideas.md`, and `content/quotes.md`, use exactly two tags: `TIX` and one CamelCase `TodayI…` action. Use `TodayIRead` for reading notes/excerpts, `TodayIIdeated` for original ideas, `TodayIQuoted` for quotes, and `TodayIFound` for discoveries. Preserve an existing valid action when it matches the content. Store tags without `#`; the templates add it for display. Remove duplicate, spaced, and abbreviated classifications. Do not add topic tags or the length-based type tags below to TIX entries.

The remaining rules apply to other content.

## Rules

- Use title case for tags (e.g., "Machine Learning" not "machine-learning")
- Keep tags concise (1-3 words each) and relevant
- Aim for 3-7 content tags
- Only update the `tags` field — do not modify any other content or frontmatter
- Apply the edit directly to the file using the Edit tool

## Type tag (always include exactly one)

In addition to content tags, the first tag MUST classify the piece by length:

- `"Thought"` — short-form: under ~200 words of body content (excluding frontmatter), or essentially a link + one-liner.
- `"Post"` — long-form: ~200 words or more of body content, multi-section, or has any `##` headings.

Edge cases:

- If a file has multiple `##` headings, classify as `"Post"` even if total words are low.
- If unsure between the two, prefer `"Thought"` for link-drops and quick reactions; prefer `"Post"` for anything with a structured argument.

Put the type tag first, then content tags. Example: `tags: ["Post", "AI", "Education", "Cryptoeconomics"]`.
