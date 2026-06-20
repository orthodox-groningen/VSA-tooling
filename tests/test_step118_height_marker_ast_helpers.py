from vsa.ast import HeightMarkerNode, PitchMarkerNode
from vsa.height_markers import (
    first_height_marker,
    height_marker_nodes,
    height_marker_refs,
    local_height_markers,
)
from vsa.parser import Parser


def test_height_marker_helpers_extract_markers_in_document_order():
    document = Parser("tekst [:] {woord} [/:] einde [//:]").parse()

    markers = height_marker_nodes(document)

    assert len(markers) == 3
    assert all(isinstance(marker, PitchMarkerNode) for marker in markers)
    assert all(isinstance(marker, HeightMarkerNode) for marker in markers)
    assert [marker.height_modifier for marker in markers] == [[], ["/"], ["//"]]


def test_height_marker_refs_include_ast_index_and_role():
    document = Parser("tekst [:] {woord} [/:]").parse()

    refs = height_marker_refs(document)

    assert [(ref.index, ref.role, ref.height_modifier) for ref in refs] == [
        (1, "start_height", []),
        (5, "local_height", ["/"]),
    ]


def test_first_height_marker_returns_none_when_absent():
    document = Parser("gewone tekst {woord}").parse()

    assert first_height_marker(document) is None
    assert height_marker_refs(document) == []
    assert height_marker_nodes(document) == []


def test_local_height_markers_exclude_first_marker():
    document = Parser("[:] tekst [/:] meer [//:]").parse()

    refs = local_height_markers(document)

    assert [(ref.role, ref.height_modifier) for ref in refs] == [
        ("local_height", ["/"]),
        ("local_height", ["//"]),
    ]
