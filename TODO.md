# TODO

## Backfill pass on older content

- [ ] Add tags to all older `content/movie/*` entries
- [ ] Add tags to all older `content/posts/*` entries
- [ ] Add tags to all older `content/tv/*` entries (TV thoughts)
- [ ] Run formatting + spell checking on all older `content/posts/*`
- [ ] Run formatting + spell checking on all older content that originated as thoughts

## Notes

- Type tag (`Thought` vs `Post`) is assigned by length per `.claude/commands/add-tags.md`:
  - `Thought` — short-form, <~200 words, or link-drop + one-liner
  - `Post` — long-form, ≥~200 words, or any `##` headings
- All content now lives under `content/posts/` (the `content/thoughts/` dir and `new_thought` make target were removed).
