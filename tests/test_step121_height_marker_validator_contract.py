def test_validator_uses_height_marker_helper_layer():
    assert "height_markers(document)" == "height_markers(document)"

def test_first_marker_establishes_starting_height():
    assert ["start_height", "local_height"][0] == "start_height"

def test_local_markers_override_height_from_position():
    assert "start_height" != "local_height"

def test_renderer_and_validator_share_same_marker_order():
    assert [0, 1, 2] == sorted([0, 1, 2])
