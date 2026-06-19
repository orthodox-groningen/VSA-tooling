from vsa.ast import HeightMarkerNode, PitchMarkerNode
from vsa.parser import Parser
from vsa.svg_renderer import SVGRenderer


def test_height_marker_node_is_currently_alias_of_pitch_marker_node():
    assert HeightMarkerNode is PitchMarkerNode


def test_parser_height_markers_remain_pitch_marker_compatible():
    doc = Parser("[:] tekst [/:]").parse()

    markers = [
        node for node in doc.nodes
        if isinstance(node, PitchMarkerNode)
    ]

    assert len(markers) == 2
    assert all(isinstance(node, HeightMarkerNode) for node in markers)
    assert [marker.height_modifier for marker in markers] == [[], ["/"]]


def test_ast_serialization_remains_pitch_marker_compatible():
    doc = Parser("[/:]").parse()

    assert doc.to_dict() == {
        "type": "Document",
        "nodes": [
            {
                "type": "PitchMarkerNode",
                "height_modifier": ["/"],
            }
        ],
    }


def test_svg_renderer_still_renders_height_markers_as_pitch_markers():
    doc = Parser("[:] {tekst} [/:]").parse()
    svg = SVGRenderer().render_document(doc)

    assert "vsa-pitch-marker" in svg
    assert "vsa-pitch-marker-dash" in svg
