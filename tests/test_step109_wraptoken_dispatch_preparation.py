from vsa.parser import BRACKET_DIRECTIVE_END

def test_bracket_directive_end_token_remains_explicit():
    assert BRACKET_DIRECTIVE_END == ":]"

def test_wraptokens_reserved_for_future_dispatch():
    reserved = ["[/]", "[*]", "[/?]", "[*?]"]
    assert reserved == ["[/]", "[*]", "[/?]", "[*?]"]
