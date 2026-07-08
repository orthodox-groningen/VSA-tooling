from docs_contracts import doc, read_doc, assert_terms


def test_rendering_spec_exists_and_is_normative_surface():
    assert doc("rendering_spec").exists()
    assert len(read_doc("rendering_spec").splitlines()) > 200


def test_layout_algorithm_spec_mentions_pipeline():
    text = read_doc("rendering_spec")

    assert_terms(text, ("Renderpipeline", "render-units", "Collisiondetectie", "Wrapping"))


def test_svg_dom_spec_mentions_required_classes():
    text = read_doc("rendering_spec")

    assert_terms(text, ("vsa-score", "vsa-line", "vsa-unit", "vsa-pitch-marker"))


def test_rendering_config_spec_mentions_override_order():
    text = read_doc("rendering_spec")

    assert "ingebouwde defaults" in text
    assert "projectconfig" in text
    assert "CLI-overrides" in text or "CLI override" in text
