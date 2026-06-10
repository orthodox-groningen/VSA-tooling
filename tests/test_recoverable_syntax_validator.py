from vsa.recoverable_syntax_validator import RecoverableSyntaxValidator


def test_collects_multiple_syntax_errors():
    text = "{}\n{te kst}\ntekst}\n{open"

    diagnostics = RecoverableSyntaxValidator(text).validate()

    codes = [item.code for item in diagnostics.items]

    assert "VSA-SYNTAX-EMPTY-SCOPE" in codes
    assert "VSA-SYNTAX-WHITESPACE-IN-SCOPE" in codes
    assert "VSA-SYNTAX-UNEXPECTED-CLOSE-BRACE" in codes
    assert "VSA-SYNTAX-UNCLOSED-SCOPE" in codes


def test_valid_text_has_no_errors():
    diagnostics = RecoverableSyntaxValidator("{tekst}").validate()

    assert not diagnostics.has_errors()


def test_pitch_marker_errors_are_collected():
    diagnostics = RecoverableSyntaxValidator("[//] [/:").validate()

    codes = [item.code for item in diagnostics.items]

    assert "VSA-SYNTAX-PITCH-MARKER-MISSING-COLON" in codes
    assert "VSA-SYNTAX-UNCLOSED-PITCH-MARKER" in codes
