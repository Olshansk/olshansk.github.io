# AGENTS.md

Project-specific instructions for AI agents working on olshansky.info.

## Resume Guidelines

- **Resume must never exceed 1 page** - When updating `cv/resume.tex`, ensure the compiled PDF fits on a single page
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
