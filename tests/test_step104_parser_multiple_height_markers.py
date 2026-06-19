import pytest

from vsa.ast import HeightMarkerNode, PitchMarkerNode, TextNode
from vsa.errors import VSASyntaxError
from vsa.parser import Parser


def test_height_marker_alias_keeps_existing_pitch_marker_compatibility():
    marker = HeightMarkerNode(height_modifier=["/"], start=1, end=5)

    assert isinstance(marker, PitchMarkerNode)
    assert marker.ehm == ["/"]
    assert marker.to_dict() == {
        "type": "PitchMarkerNode",
        "height_modifier": ["/"],
    }


def test_parser_accepts_multiple_height_markers_in_document_order():
    doc = Parser("[:] begin [/:] midden [//:] einde").parse()

    assert [type(node).__name__ for node in doc.nodes] == [
        "PitchMarkerNode",
        "TextNode",
        "PitchMarkerNode",
        "TextNode",
        "PitchMarkerNode",
        "TextNode",
    ]

    markers = [node for node in doc.nodes if isinstance(node, PitchMarkerNode)]
    assert [marker.height_modifier for marker in markers] == [[], ["/"], ["//"]]
    assert [marker.start for marker in markers] == [0, 10, 22]


def test_parser_accepts_text_before_between_and_after_height_markers():
    doc = Parser("tekst vóór [:] tekst tussen [\\:] tekst na").parse()

    assert isinstance(doc.nodes[0], TextNode)
    assert doc.nodes[0].text == "tekst vóór "

    markers = [node for node in doc.nodes if isinstance(node, PitchMarkerNode)]
    assert [marker.height_modifier for marker in markers] == [[], ["\\"]]

    assert doc.nodes[-1].text == " tekst na"


def test_parser_uses_bracket_directive_end_token_not_plain_closing_bracket():
    with pytest.raises(VSASyntaxError) as excinfo:
        Parser("[/] geen hoogte-marker").parse()

    assert ":]" in str(excinfo.value)


def test_parser_rejects_ampersand_directive_as_pitch_marker():
    with pytest.raises(VSASyntaxError) as excinfo:
        Parser("[/&\\:]").parse()

    assert "Ongeldige modifier" in str(excinfo.value)


def test_parser_rejects_elm_as_pitch_marker_body():
    with pytest.raises(VSASyntaxError) as excinfo:
        Parser("[_:]").parse()

    assert "Ongeldige modifier" in str(excinfo.value)
