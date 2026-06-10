from vsa.syntax_validator import SyntaxValidator


def test_unclosed_scope():
    diagnostics = SyntaxValidator("{tekst").validate()

    assert diagnostics.has_errors()

    assert diagnostics.items[0].code == "VSA-SYNTAX-UNCLOSED-SCOPE"


def test_unexpected_close_brace():
    diagnostics = SyntaxValidator("tekst}").validate()

    assert diagnostics.has_errors()

    assert diagnostics.items[0].code == "VSA-SYNTAX-UNEXPECTED-CLOSE-BRACE"


def test_valid_text():
    diagnostics = SyntaxValidator("{tekst}").validate()

    assert not diagnostics.has_errors()
