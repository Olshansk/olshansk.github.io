---
name: add-tix
description: Organize a rough voice or text idea and add it to the site's dated TIX log through its deterministic Make target.
---

# Add TIX

Use this workflow when the user invokes `add-tix` or asks to capture an idea in TIX.

## Organize

- Run `make help` first.
- Preserve the core insight, uncertainty, and the user's tone.
- Remove voice-transcription filler, false starts, and repetition.
- Add a short title only when it improves scanability.
- Do not add facts, examples, implementation details, market claims, or certainty absent from the capture.
- If the input is already polished, preserve it rather than rewriting it.
- Resolve relative dates in the user's timezone and pass an explicit ISO `YYYY-MM-DD` date. Use the current date when none is requested.

## Execute

After organizing the capture into an optional title and body, run:

```bash
make add_tix TEXT="<organized body>" TITLE="<optional title>" DATE="YYYY-MM-DD"
```

Then:

1. Confirm the command changed only `content/ideas.md`.
2. Inspect the diff for faithfulness to the user's capture.
3. Run `python3 -m unittest discover -s tests -p 'test_*.py'`.
4. Run `git diff --check`.
5. Run `make test_workflow`.
6. Commit with `💡 content: add TIX entry`.
7. Open a pull request, request squash auto-merge after required checks, and report the PR URL. Never bypass a failing check.

If the deterministic command reports a possible duplicate, make no edit and tell the user which capture was rejected.
