"""Check the rendered reading section, attribution, and feed boundaries."""

import html
import json
import re
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SLUG = "2026-10-17-human-attention-is-the-bottleneck"
SOURCE = "https://www.anthropic.com/research/employment-at-anthropic"
AUTHORS = ["Nathan Wilmers", "Regina Catipon", "Maxim Massenkoff", "Peter McCrory"]
QUOTE = (
    "This acceleration makes human attention the bottleneck for agent output. "
    "Even among non-technical employees, reading all the output of their Claude agents "
    "would take half their work week. In response, employees turn to “meta-work,” "
    "of building visibility tools and monitoring agent pipelines."
)


@pytest.fixture(scope="module")
def site(tmp_path_factory):
    """Build production output once for all rendered-content checks."""
    destination = tmp_path_factory.mktemp("reading-site")
    subprocess.run(
        ["hugo", "--destination", str(destination)],
        cwd=ROOT, check=True, capture_output=True, text=True,
    )
    return destination


def test_quote_and_source_render_with_original_author_metadata(site):
    page = (site / "reading" / SLUG / "index.html").read_text()
    blockquote = re.search(r"<blockquote[^>]*>(.*?)</blockquote>", page, re.S).group(1)
    assert html.unescape(re.sub(r"<[^>]+>", "", blockquote)).strip() == QUOTE
    assert f'href="{SOURCE}"' in page
    assert 'name="author" content="Daniel Olshansky"' not in page
    assert 'property="article:author" content="Daniel Olshansky"' not in page
    assert ', '.join(AUTHORS) in page
    schemas = [json.loads(item) for item in re.findall(
        r'<script type="application/ld\+json">(.*?)</script>', page, re.S
    )]
    articles = [item for item in schemas if item.get("@type") in {"Article", "BlogPosting"}]
    assert articles
    for article in articles:
        assert [author["name"] for author in article["author"]] == AUTHORS


def test_reading_feed_contains_complete_quote_and_attribution(site):
    items = ET.parse(site / "reading/index.xml").findall("./channel/item")
    assert items
    assert all("/reading/" in item.findtext("link") for item in items)
    item = next(item for item in items if SLUG in item.findtext("link"))
    content = item.findtext("{http://purl.org/rss/1.0/modules/content/}encoded")
    assert QUOTE in html.unescape(re.sub(r"<[^>]+>", "", content))
    assert SOURCE in content
    assert all(author in content for author in AUTHORS)


def test_everything_feed_includes_reading_but_blog_feed_does_not(site):
    for path in ("posts/index.xml",):
        items = ET.parse(site / path).findall("./channel/item")
        assert items
        assert any("/posts/" in item.findtext("link") for item in items)
        assert all("/reading/" not in item.findtext("link") for item in items)
    assert SLUG not in (site / "posts/index.html").read_text()
    assert SLUG in (site / "index.xml").read_text()


def test_reading_and_tag_are_discoverable(site):
    assert '/reading/' in (site / "index.html").read_text()
    assert SLUG in (site / "reading/index.html").read_text()
    assert '/reading/index.xml' in (site / "reading/index.html").read_text()
    assert SLUG in (site / "tags/todayiread/index.html").read_text()


def test_separate_content_feeds_and_existing_blog_tags(site):
    quote_items = ET.parse(site / "tags/quote/index.xml").findall("./channel/item")
    excerpt_items = ET.parse(site / "tags/excerpt/index.xml").findall("./channel/item")
    blog_items = ET.parse(site / "tags/blog/index.xml").findall("./channel/item")
    assert quote_items and excerpt_items and blog_items
    assert all("/quotes/" in item.findtext("link") for item in quote_items)
    assert all("/reading/" in item.findtext("link") for item in excerpt_items)
    assert all("/posts/" in item.findtext("link") for item in blog_items)
    assert SLUG in (site / "tags/excerpt/index.html").read_text()
    assert all(item.findtext("{http://purl.org/rss/1.0/modules/content/}encoded") for item in quote_items + excerpt_items + blog_items)
    blog_links = {item.findtext("link") for item in ET.parse(site / "posts/index.xml").findall("./channel/item")}
    assert blog_links == {item.findtext("link") for item in blog_items}
