from pathlib import Path


def test_rendering_pages_exist():
    root = Path("examples/hugo-demo/content-source/voorbeelden/rendering")

    assert root.exists()
    assert any(path.suffix == ".md" for path in root.rglob("*.md"))


def test_spacing_diagnostics_page_is_present():
    path = Path("examples/hugo-demo/content-source/voorbeelden/rendering/spacing-diagnostiek.md")

    assert path.exists()


def test_rendering_pages_contain_vsa_examples():
    root = Path("examples/hugo-demo/content-source/voorbeelden/rendering")
    texts = "\n".join(
        path.read_text(encoding="utf-8")
        for path in root.rglob("*.md")
    )

    assert "vsa-notatie" in texts
