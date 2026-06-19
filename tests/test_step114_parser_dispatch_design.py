CONTROL_TOKENS = {
    "[*]",
    "[/]",
    "[*?]",
    "[/?]",
}

def test_reserved_control_token_set():
    assert CONTROL_TOKENS == {"[*]", "[/]", "[*?]", "[/?]"}

def test_height_marker_syntax_remains_separate():
    assert "[:]" not in CONTROL_TOKENS
    assert "[/:]" not in CONTROL_TOKENS
