from vsa.bracket_token_stream import BracketToken, bracket_token_stream, pitch_marker_tokens


def test_empty_ehm_pitch_marker_survives_token_stream():
    assert bracket_token_stream("[:]") == [
        BracketToken(kind="pitch_marker", start=0, end=3, value="")
    ]


def test_empty_ehm_pitch_marker_survives_pitch_marker_filter():
    assert pitch_marker_tokens("tekst [:]") == [
        BracketToken(kind="pitch_marker", start=6, end=9, value="")
    ]
