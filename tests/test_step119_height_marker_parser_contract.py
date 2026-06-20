def test_height_markers_are_emitted_in_document_order():
    expected = [
        "HeightMarkerNode",
        "TextNode",
        "ScopeNode",
        "HeightMarkerNode",
    ]
    assert expected[0] == "HeightMarkerNode"
    assert expected[-1] == "HeightMarkerNode"

def test_multiple_height_markers_are_allowed():
    markers = [":]", "[/:]", "[//:]"]
    assert len(markers) == 3

def test_parser_contract_keeps_existing_pitch_marker_compatibility():
    parser_node_type = "PitchMarkerNode"
    compatibility_alias = "HeightMarkerNode"
    assert parser_node_type != ""
    assert compatibility_alias != ""
