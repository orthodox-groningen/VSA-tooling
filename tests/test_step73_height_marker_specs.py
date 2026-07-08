from docs_contracts import doc, read_doc, assert_terms


def test_height_marker_contract_lives_in_rendering_spec():
    assert doc("rendering_spec").exists()


def test_height_marker_spec_allows_multiple_markers_and_surrounding_text():
    text = read_doc("rendering_spec")

    assert_terms(
        text,
        (
            "mogen meerdere hoogte-markeringen voorkomen",
            "vóór de eerste hoogte-markering",
            "tussen hoogte-markeringen",
            "na de laatste hoogte-markering",
        ),
    )


def test_height_marker_spec_defines_position_semantics():
    text = read_doc("rendering_spec")

    assert_terms(
        text,
        (
            "eerste hoogte-markering",
            "beginhoogte",
            "latere hoogte-markering",
            "lokale hoogte op die positie",
        ),
    )


def test_height_marker_spec_prefers_document_stream_nodes():
    text = read_doc("rendering_spec")

    assert_terms(
        text,
        (
            "gewone positionele semantische nodes",
            "Document(nodes=[TextNode, HeightMarkerNode, ScopeNode, ...])",
            "height_markers = alle HeightMarkerNode nodes in bronvolgorde",
        ),
    )
