from pathlib import Path


def test_rendering_demo_subpages_exist():
    base = Path("examples/hugo-demo/content-source/voorbeelden/rendering")

    assert (base / "glyphs-basis.md").exists()
    assert (base / "pitchmarkers.md").exists()
    assert (base / "spacing-lettergrepen.md").exists()


def test_rendering_index_links_to_subpages():
    text = Path("examples/hugo-demo/content-source/voorbeelden/rendering.md").read_text(
        encoding="utf-8"
    )

    assert "glyphs-basis/" in text
    assert "pitchmarkers/" in text
    assert "spacing-lettergrepen/" in text


def test_spacing_demo_contains_practice_case():
    text = Path(
        "examples/hugo-demo/content-source/voorbeelden/rendering/spacing-lettergrepen.md"
    ).read_text(encoding="utf-8")

    assert "grote ge{na_}{\\de}" in text
    assert "Toen {/Gij_}" in text
