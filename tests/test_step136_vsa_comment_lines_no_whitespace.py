from vsa.parser import Parser
from vsa.svg_renderer import SVGRenderer
from vsa.vsa_comments import strip_vsa_html_comments


def text_nodes(document):
    return [
        node.text
        for node in document.nodes
        if type(node).__name__ == "TextNode"
    ]


def test_comment_only_line_is_removed_without_blank_line():
    source = "eerste\n<!-- broncommentaar -->\ntweede"

    assert strip_vsa_html_comments(source) == "eerste\ntweede"


def test_comment_only_line_with_indentation_is_removed_without_blank_line():
    source = "eerste\n   <!-- broncommentaar -->   \ntweede"

    assert strip_vsa_html_comments(source) == "eerste\ntweede"


def test_inline_comment_is_removed_without_removing_surrounding_source_text():
    source = "eerste <!-- broncommentaar --> tweede"

    assert strip_vsa_html_comments(source) == "eerste  tweede"


def test_parser_does_not_create_text_node_for_comment_only_line():
    document = Parser("eerste\n<!-- broncommentaar -->\ntweede").parse()

    assert text_nodes(document) == ["eerste\ntweede"]


def test_svg_contains_no_extra_comment_blank_line():
    document = Parser("eerste\n<!-- broncommentaar -->\ntweede").parse()

    svg = SVGRenderer().render_document(document)

    assert "<!--" not in svg
    assert "broncommentaar" not in svg
    assert svg.count('class="vsa-line"') == 2
