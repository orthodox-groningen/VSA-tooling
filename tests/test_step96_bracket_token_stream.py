from vsa.bracket_token_stream import BracketToken, bracket_token_stream, pitch_marker_tokens


def test_token_stream_keeps_plain_text_when_no_directives():
    assert bracket_token_stream("Heer ontferm U") == [
        BracketToken(kind="text", start=0, end=14, value="Heer ontferm U")
    ]


def test_token_stream_splits_text_and_pitch_marker():
    tokens = bracket_token_stream("Heer [:] ontferm")

    assert tokens == [
        BracketToken(kind="text", start=0, end=5, value="Heer "),
        BracketToken(kind="pitch_marker", start=5, end=8, value=""),
        BracketToken(kind="text", start=8, end=16, value=" ontferm"),
    ]


def test_token_stream_keeps_empty_pitch_marker_body():
    tokens = bracket_token_stream("[:]")

    assert tokens == [
        BracketToken(kind="pitch_marker", start=0, end=3, value="")
    ]


def test_token_stream_keeps_multiple_pitch_markers_in_order():
    tokens = bracket_token_stream("[:] begin [\\:] einde")

    assert [token.kind for token in tokens] == ["pitch_marker", "text", "pitch_marker", "text"]
    assert [token.value for token in tokens if token.kind == "pitch_marker"] == ["", "\\"]


def test_token_stream_classifies_non_pitch_directive_separately():
    tokens = bracket_token_stream("tekst [/&\\:] verder")

    assert tokens == [
        BracketToken(kind="text", start=0, end=6, value="tekst "),
        BracketToken(kind="directive", start=6, end=12, value="/&\\"),
        BracketToken(kind="text", start=12, end=19, value=" verder"),
    ]


def test_missing_end_token_remains_plain_text():
    assert bracket_token_stream("tekst [/] verder") == [
        BracketToken(kind="text", start=0, end=16, value="tekst [/] verder")
    ]


def test_pitch_marker_tokens_filters_text_and_other_directives():
    tokens = pitch_marker_tokens("a [:] b [_:] c [\\:]")

    assert tokens == [
        BracketToken(kind="pitch_marker", start=2, end=5, value=""),
        BracketToken(kind="pitch_marker", start=15, end=19, value="\\"),
    ]
