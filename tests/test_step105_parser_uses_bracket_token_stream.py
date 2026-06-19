import pytest

from vsa.ast import PitchMarkerNode, TextNode
from vsa.bracket_token_stream import BracketToken, bracket_token_stream
from vsa.errors import VSASyntaxError
from vsa.parser import Parser


def test_parser_height_markers_match_bracket_token_stream_positions():
    source = "voor [:] midden [/:] na"
    doc = Parser(source).parse()

    stream_markers = [
        token for token in bracket_token_stream(source)
        if token.kind == "pitch_marker"
    ]
    ast_markers = [
        node for node in doc.nodes
        if isinstance(node, PitchMarkerNode)
    ]

    assert [(node.start, node.end, node.height_modifier) for node in ast_markers] == [
        (token.start, token.end, [] if token.value == "" else [token.value])
        for token in stream_markers
    ]


def test_parser_rejects_non_pitch_bracket_directive_from_token_stream():
    assert bracket_token_stream("[_:]")[0] == BracketToken(
        kind="directive",
        start=0,
        end=4,
        value="_",
    )

    with pytest.raises(VSASyntaxError):
        Parser("[_:]").parse()


def test_parser_uses_same_end_token_behavior_as_bracket_token_stream():
    assert bracket_token_stream("[/] geen marker") == [
        BracketToken(kind="text", start=0, end=15, value="[/] geen marker")
    ]

    with pytest.raises(VSASyntaxError) as excinfo:
        Parser("[/] geen marker").parse()

    assert ":]" in str(excinfo.value)


def test_parser_keeps_text_nodes_around_bracket_token_markers():
    doc = Parser("a [:] b [\\:] c").parse()

    assert [type(node).__name__ for node in doc.nodes] == [
        "TextNode",
        "PitchMarkerNode",
        "TextNode",
        "PitchMarkerNode",
        "TextNode",
    ]
    assert [node.text for node in doc.nodes if isinstance(node, TextNode)] == ["a ", " b ", " c"]
