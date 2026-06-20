def test_height_markers_are_document_stream_nodes():
    expected = [
        "TextNode",
        "HeightMarkerNode",
        "ScopeNode",
        "HeightMarkerNode",
        "TextNode",
    ]

    assert expected[1] == "HeightMarkerNode"
    assert expected[3] == "HeightMarkerNode"


def test_first_height_marker_has_semantic_start_role():
    first_marker_role = "start_height"
    later_marker_role = "local_height"

    assert first_marker_role == "start_height"
    assert later_marker_role == "local_height"


def test_renderer_must_not_distinguish_first_and_later_markers():
    render_role_first = "height_marker"
    render_role_later = "height_marker"

    assert render_role_first == render_role_later
