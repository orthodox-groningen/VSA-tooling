from vsa.ast import (
    Document,
    TextNode,
    ScopeNode,
    PitchMarkerNode,
)


def test_ast_imports():
    doc = Document()

    assert doc.nodes == []

    text = TextNode(text="tekst")
    assert text.text == "tekst"

    scope = ScopeNode(
        height_modifier=["/"],
        text="tekst",
        length_modifier=["_"]
    )

    assert scope.text == "tekst"

    marker = PitchMarkerNode(
        height_modifier=["//"]
    )

    assert marker.height_modifier == ["//"]
