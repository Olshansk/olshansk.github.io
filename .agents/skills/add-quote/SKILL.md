---
name: add-quote
description: Add a dated, attributed or unattributed quote to the site's quotes log through its deterministic Make target.
---

# Add Quote

Use this workflow when the user invokes `add-quote` or asks to capture a quote.

## Rules

- Run `make help` first.
- Preserve the quote text verbatim. Remove only one matching pair of outer quotation marks because the script renders them canonically.
- Treat a trailing ` - author` or ` — author` outside the quote as attribution. If parsing is genuinely ambiguous, ask rather than guess.
- Never invent, research, or correct an attribution unless the user explicitly asks for verification.
- Resolve relative dates in the user's timezone and pass an explicit ISO `YYYY-MM-DD` date. Use the current date when none is requested.

## Execute

Run:

```bash
make add_quote TEXT="<quote>" AUTHOR="<optional author>" DATE="YYYY-MM-DD"
```

Then:

1. Confirm the command changed only `content/quotes.md`.
2. Inspect the diff and confirm the text and attribution match the request.
3. Run `python3 -m unittest discover -s tests -p 'test_*.py'`.
4. Run `git diff --check`.
5. Run `make test_workflow`.
6. Commit with `📝 content: add quote`.
7. Open a pull request, request squash auto-merge after required checks, and report the PR URL. Never bypass a failing check.

If the deterministic command reports a possible duplicate, make no edit and tell the user which capture was rejected.
