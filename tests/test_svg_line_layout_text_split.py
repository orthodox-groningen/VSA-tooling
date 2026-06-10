from vsa.ast import TextNode, Document
from vsa.svg_line_layout import split_text_node, build_lines


def test_split_text_node_into_word_chunks():
    chunks = split_text_node(TextNode(" is de Heer. "))

    texts = [chunk.text for chunk in chunks]

    assert texts == ["is ", "de ", "Heer. "]


def test_long_text_node_can_wrap_between_words():
    document = Document(nodes=[
        TextNode(" is de Heer, en heilig is Zijn Naam. "),
        TextNode("en nog meer tekst.")
    ])

    lines = build_lines(document, max_width=180)

    assert len(lines) > 1
    assert all(line.width <= 220 for line in lines)
