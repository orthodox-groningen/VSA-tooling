DIRECTIVE_KINDS = {
    "height_marker",
    "control_token",
}

def test_directive_kinds_are_distinct():
    assert "height_marker" in DIRECTIVE_KINDS
    assert "control_token" in DIRECTIVE_KINDS

def test_control_tokens_are_not_height_markers():
    assert "control_token" != "height_marker"
