from vsa.ast import TextNode
from vsa.svg_line_layout import WhitespaceNode, split_text_node


def test_split_text_node_into_word_and_whitespace_chunks():
    chunks = split_text_node(TextNode(" is de Heer. "))

    texts = [chunk.text for chunk in chunks]

    assert texts == [" ", "is", " ", "de", " ", "Heer.", " "]
    assert isinstance(chunks[0], WhitespaceNode)
    assert isinstance(chunks[2], WhitespaceNode)
    assert isinstance(chunks[4], WhitespaceNode)
    assert isinstance(chunks[6], WhitespaceNode)


def test_split_text_node_ignores_empty_text():
    assert split_text_node(TextNode("")) == []
