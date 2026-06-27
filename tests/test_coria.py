"""Tests for Coria play URL helper and Hugo shortcode."""

from pathlib import Path
from urllib.parse import parse_qs, urlparse

from vsa.coria import coria_play_url


def test_coria_play_url_encodes_score_url():
    url = coria_play_url(
        "https://example.org/vsa/praktijk-zondagen-tropaar-zondag-toon-3.mxl"
    )
    parsed = urlparse(url)
    assert parsed.scheme == "https"
    assert parsed.netloc == "coria.nl"
    assert parsed.path == "/play_from_url"
    params = parse_qs(parsed.query)
    assert params["back"] == ["coria.nl"]
    assert params["url"] == [
        "https://example.org/vsa/praktijk-zondagen-tropaar-zondag-toon-3.mxl"
    ]


def test_coria_shortcode_builds_play_from_url_link():
    text = Path("examples/hugo-demo/layouts/shortcodes/coria.html").read_text(
        encoding="utf-8"
    )
    assert "coria.nl/play_from_url" in text
    assert "urlquery" in text
    assert 'rel="noopener noreferrer"' in text


def test_coria_html_shortcode_links_to_hosted_html():
    text = Path("examples/hugo-demo/layouts/shortcodes/coria-html.html").read_text(
        encoding="utf-8"
    )
    assert "relURL" in text
    assert "coria.nl/play_from_url" not in text
    assert 'rel="noopener noreferrer"' in text


def test_coria_html_example_exists_for_tropaar_toon_3():
    path = Path(
        "examples/hugo-demo/content-source/praktijk/zondagen/"
        "tropaar-zondag-toon-3.coria.html"
    )
    assert path.exists()
    assert "song_data" in path.read_text(encoding="utf-8")
