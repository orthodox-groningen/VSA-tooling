from xml.etree import ElementTree

from vsa.parser import Parser
from vsa.svg_renderer import SVGRenderer


def test_svg_renderer_writes_no_plain_text_metadata_comment():
    document = Parser("tekst <!-- plain-text: test --> einde").parse()

    svg = SVGRenderer().render_document(document)

    assert "<!-- plain-text:" not in svg


def test_svg_renderer_output_with_markdown_comment_like_text_is_valid_xml():
    document = Parser("tekst <!-- plain-text: test --> einde").parse()

    svg = SVGRenderer().render_document(document)

    ElementTree.fromstring(svg)
