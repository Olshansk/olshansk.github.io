---
description: Auto-generate tags for a blog post or thought
---

Read the `.file` file to get the path of the target content file, then read that content file and analyze it.

Based on the content, suggest appropriate tags and update the file's frontmatter `tags` field.

## Rules

- Use title case for tags (e.g., "Machine Learning" not "machine-learning")
- Keep tags concise (1-3 words each) and relevant
- Aim for 3-7 tags
- Only update the `tags` field — do not modify any other content or frontmatter
- Apply the edit directly to the file using the Edit tool
