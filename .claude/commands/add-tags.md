---
description: Auto-generate tags for a blog post or thought
arguments:
  - name: file
    description: Path to the content markdown file (e.g., content/posts/my-post.md)
    required: true
---

Read the file at `$ARGUMENTS.file` and analyze its content.

Based on the content, suggest appropriate tags and update the file's frontmatter `tags` field.

## Rules

- Use title case for tags (e.g., "Machine Learning" not "machine-learning")
- Keep tags concise (1-3 words each) and relevant
- Aim for 3-7 tags
- Only update the `tags` field — do not modify any other content or frontmatter
- Apply the edit directly to the file using the Edit tool
