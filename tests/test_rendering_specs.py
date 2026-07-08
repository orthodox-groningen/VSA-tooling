from pathlib import Path


SPEC_FILES = [
    Path("docs/specification/rendering.md"),
    Path("docs/specification/rendering.md"),
    Path("docs/specification/rendering.md"),
]


def test_rendering_specs_are_not_placeholders():
    for path in SPEC_FILES:
        assert path.exists(), f"Ontbrekende spec: {path}"
        text = path.read_text(encoding="utf-8")

        assert len(text) > 2500, f"Spec lijkt te summier: {path}"


def test_layout_algorithm_spec_mentions_pipeline():
    text = Path("docs/specification/rendering.md").read_text(encoding="utf-8")

    assert "Renderpipeline" in text
    assert "render-units" in text
    assert "Collisiondetectie" in text
    assert "Wrapping" in text


def test_svg_dom_spec_mentions_required_classes():
    text = Path("docs/specification/rendering.md").read_text(encoding="utf-8")

    assert "vsa-score" in text
    assert "vsa-line" in text
    assert "vsa-unit" in text
    assert "vsa-pitch-marker" in text


def test_rendering_config_spec_mentions_override_order():
    text = Path("docs/specification/rendering.md").read_text(encoding="utf-8")

    assert "ingebouwde defaults" in text
    assert "theme defaults" in text
    assert "projectconfig" in text
    assert "CLI override" in text
