from vsa.ast import ControlTokenNode, Document, TextNode


def test_control_token_node_serializes_minimal_abstract_meaning():
    node = ControlTokenNode(token="[/]", meaning="phrase_boundary", start=3, end=6)

    assert node.to_dict() == {
        "type": "ControlTokenNode",
        "token": "[/]",
        "meaning": "phrase_boundary",
    }


def test_document_can_contain_control_token_node_in_sequence():
    document = Document(nodes=[
        TextNode("voor"),
        ControlTokenNode(token="[*]", meaning="phrase_rest"),
        TextNode("na"),
    ])

    assert document.to_dict() == {
        "type": "Document",
        "nodes": [
            {"type": "TextNode", "text": "voor"},
            {
                "type": "ControlTokenNode",
                "token": "[*]",
                "meaning": "phrase_rest",
            },
            {"type": "TextNode", "text": "na"},
        ],
    }


def test_control_token_node_keeps_source_span_without_serializing_it():
    node = ControlTokenNode(token="[*?]", meaning="optional_phrase_rest", start=10, end=14)

    assert node.start == 10
    assert node.end == 14
    assert "start" not in node.to_dict()
    assert "end" not in node.to_dict()
