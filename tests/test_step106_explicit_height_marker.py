from vsa.ast import HeightMarkerNode, PitchMarkerNode
from vsa.parser import Parser


def test_height_marker_name_is_compatible_alias_for_now():
    marker = HeightMarkerNode(height_modifier=["/"], start=1, end=5)

    assert isinstance(marker, PitchMarkerNode)
    assert marker.ehm == ["/"]


def test_parser_keeps_pitch_marker_serialization_compatible():
    doc = Parser("[/:]").parse()

    assert isinstance(doc.nodes[0], PitchMarkerNode)
    assert doc.to_dict()["nodes"][0] == {
        "type": "PitchMarkerNode",
        "height_modifier": ["/"],
    }
