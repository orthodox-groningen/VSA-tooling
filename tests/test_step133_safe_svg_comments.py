from xml.etree import ElementTree

from vsa.parser import Parser
from vsa.svg_renderer import SVGRenderer, _safe_xml_comment_text


def test_safe_xml_comment_text_removes_double_hyphen_after_escaping():
    text = _safe_xml_comment_text("<!-- plain-text: test -->")

    assert "--" not in text
    assert "&lt;!" in text
    assert "&gt;" in text


def test_safe_xml_comment_text_does_not_end_with_hyphen():
    text = _safe_xml_comment_text("tekst-")

    assert not text.endswith("-")


def test_svg_renderer_never_writes_double_hyphen_inside_plain_text_comment():
    document = Parser("tekst <!-- plain-text: test --> einde").parse()

    svg = SVGRenderer().render_document(document)

    assert "<!-- plain-text:" in svg
    for comment_body in _xml_comment_bodies(svg):
        assert "--" not in comment_body


def test_svg_renderer_output_with_markdown_comment_like_text_is_valid_xml():
    document = Parser("tekst <!-- plain-text: test --> einde").parse()

    svg = SVGRenderer().render_document(document)

    ElementTree.fromstring(svg)


def _xml_comment_bodies(svg: str):
    start = 0
    while True:
        begin = svg.find("<!--", start)
        if begin == -1:
            return
        end = svg.find("-->", begin)
        assert end != -1
        yield svg[begin + 4:end]
        start = end + 3
