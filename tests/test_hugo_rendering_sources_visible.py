from pathlib import Path


def test_rendering_demo_pages_show_source_blocks():
    base = Path("examples/hugo-demo/content-source/voorbeelden/rendering")

    for name in ["glyphs-basis.md", "pitchmarkers.md", "spacing-lettergrepen.md"]:
        text = (base / name).read_text(encoding="utf-8")

        assert "Bron:" in text
        assert "Rendering:" in text
        assert "````markdown" in text
        assert "::: vsa-notatie" in text


def test_spacing_demo_has_whitespace_case():
    text = Path(
        "examples/hugo-demo/content-source/voorbeelden/rendering/spacing-lettergrepen.md"
    ).read_text(encoding="utf-8")

    assert "gedood door het hemellicht" in text
