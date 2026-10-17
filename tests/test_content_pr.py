"""Validate capture text preservation and isolated PR submission boundaries."""

import importlib.util
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location("content_pr", Path(__file__).parents[1] / "scripts/content_pr.py")
content_pr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(content_pr)


def test_excerpt_preserves_multiline_text_and_source():
    path, rendered = content_pr.build_entry("excerpt", {
        "TITLE": 'A "quoted" title', "TEXT": '“Exact words.”\n\nSecond paragraph.',
        "SOURCE": "https://example.com/source", "AUTHOR": "Original Author", "DATE": "2026-10-17",
    })
    assert str(path) == "content/reading/2026-10-17-a-quoted-title.md"
    assert '> “Exact words.”\n>\n> Second paragraph.' in rendered
    assert 'author: ["Original Author"]' in rendered
    assert 'tags: ["excerpt", "TodayIRead"]' in rendered
    assert '— Original Author, <https://example.com/source>' in rendered


def test_blog_file_remains_a_draft(tmp_path):
    source = tmp_path / "body.md"
    source.write_text("# My heading\n\nOriginal prose.")
    path, rendered = content_pr.build_entry("blog", {"TITLE": "My post", "BODY_FILE": str(source)})
    assert path.parent == Path("content/posts")
    assert 'draft: true' in rendered
    assert source.read_text() in rendered


@pytest.mark.parametrize("values", [
    {"TITLE": "Missing body"},
    {"TITLE": "Missing credit", "TEXT": "Words"},
    {"TITLE": "Bad source", "TEXT": "Words", "AUTHOR": "A", "SOURCE": "javascript:alert(1)"},
])
def test_invalid_excerpt_fails_before_git_operations(values):
    with pytest.raises(ValueError):
        content_pr.build_entry("excerpt", values)


def test_pr_isolated_and_only_entry_staged(monkeypatch, tmp_path):
    commands = []
    monkeypatch.setattr(content_pr.tempfile, "mkdtemp", lambda **kwargs: str(tmp_path))
    monkeypatch.setattr(content_pr.sys, "argv", ["content_pr.py", "quote"])
    for key, value in {"TITLE": "A quote", "TEXT": "Exact words", "DATE": "2026-10-17"}.items():
        monkeypatch.setenv(key, value)
    for key in ("BODY_FILE", "AUTHOR", "SOURCE"):
        monkeypatch.delenv(key, raising=False)

    def fake_run(*args, cwd=content_pr.ROOT):
        commands.append((args, cwd))
        if args[:3] == ("git", "worktree", "add"):
            (tmp_path / "worktree").mkdir()
        if args[:3] == ("git", "worktree", "remove"):
            import shutil
            shutil.rmtree(tmp_path / "worktree")
        return "https://github.com/example/blog/pull/1" if args[:3] == ("gh", "pr", "create") else ""

    monkeypatch.setattr(content_pr, "run", fake_run)
    assert content_pr.main() == 0
    staged = [args for args, cwd in commands if args[:2] == ("git", "add")]
    assert staged == [("git", "add", "--", "content/reading/2026-10-17-a-quote.md")]
    assert any(args[:3] == ("gh", "pr", "create") and "--draft" in args for args, _ in commands)
    assert all(cwd != content_pr.ROOT for args, cwd in commands if args[:2] == ("git", "commit"))
    assert not any("merge" in args for args, _ in commands)
