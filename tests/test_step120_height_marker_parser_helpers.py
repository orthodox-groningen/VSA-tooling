from vsa.height_markers import (
    first_height_marker,
    height_marker_nodes,
    height_marker_refs,
    height_markers,
    is_height_marker_node,
    last_height_marker,
    local_height_markers,
)
from vsa.parser import Parser


def test_parser_height_markers_are_detected_by_unified_helper():
    document = Parser("tekst [:] midden [/:] einde").parse()

    assert [marker.height_modifier for marker in height_markers(document)] == [[], ["/"]]
    assert [marker.height_modifier for marker in height_marker_refs(document)] == [[], ["/"]]
    assert [node.height_modifier for node in height_marker_nodes(document)] == [[], ["/"]]


def test_height_marker_roles_are_assigned_in_document_order():
    document = Parser("[:] tekst [/:] meer [//:]").parse()
    markers = height_markers(document)

    assert [marker.index for marker in markers] == [0, 2, 4]
    assert [marker.role for marker in markers] == [
        "start_height",
        "local_height",
        "local_height",
    ]
    assert markers[0].is_start_marker
    assert markers[1].is_local_marker


def test_first_last_and_local_height_marker_helpers():
    document = Parser("voor [:] midden [\\:] na [//:]").parse()

    assert first_height_marker(document).height_modifier == []
    assert last_height_marker(document).height_modifier == ["//"]
    assert [marker.height_modifier for marker in local_height_markers(document)] == [
        ["\\"],
        ["//"],
    ]


def test_missing_height_marker_helpers_return_empty_or_none():
    document = Parser("gewone tekst {tekst}").parse()

    assert height_markers(document) == []
    assert height_marker_refs(document) == []
    assert height_marker_nodes(document) == []
    assert first_height_marker(document) is None
    assert last_height_marker(document) is None


def test_is_height_marker_node_uses_current_compatibility_layer():
    document = Parser("[/:]").parse()

    assert is_height_marker_node(document.nodes[0])
