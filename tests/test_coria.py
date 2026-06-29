"""Tests for Coria play URL helper and Hugo shortcode."""

from pathlib import Path
from urllib.parse import parse_qs, urlparse

import pytest

from vsa.coria import coria_play_url

BRON_CORIA_CANDIDATES = (
    Path(
        "vendor/bron/zangstukken/troparion-zondag-toon-3/sources/vsa/groningen.coria.html"
    ),
    Path(
        "../bron/zangstukken/troparion-zondag-toon-3/sources/vsa/groningen.coria.html"
    ),
)


def bron_coria_html_path() -> Path | None:
    """Pad naar Coria-HTML voor tropaar toon 3 in een bron-checkout."""
    for path in BRON_CORIA_CANDIDATES:
        if path.is_file():
            return path
    return None


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
    path = bron_coria_html_path()
    if path is None:
        if Path("vendor/bron").is_dir():
            pytest.fail(
                "vendor/bron is aanwezig maar "
                "troparion-zondag-toon-3/sources/vsa/groningen.coria.html ontbreekt"
            )
        pytest.skip("bron-checkout niet aanwezig (vendor/bron of sibling ../bron)")

    assert "song_data" in path.read_text(encoding="utf-8")
