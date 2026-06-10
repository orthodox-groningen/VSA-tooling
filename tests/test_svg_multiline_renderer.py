import re

from vsa.parser import Parser
from vsa.svg_renderer import SVGRenderer


def _extract_height(svg):
    match = re.search(r'height="([0-9]+)"', svg)
    assert match
    return int(match.group(1))


def test_multiline_renderer_increases_height():
    short_doc = Parser("{tekst}").parse()

    long_doc = Parser(" ".join(["{tekst}"] * 50)).parse()

    renderer = SVGRenderer()
    renderer.max_line_width = 300

    short_svg = renderer.render_document(short_doc)
    long_svg = renderer.render_document(long_doc)

    assert _extract_height(long_svg) > _extract_height(short_svg)


def test_multiline_renderer_keeps_text():
    source = " ".join(["{tekst}"] * 10)

    document = Parser(source).parse()

    renderer = SVGRenderer()
    renderer.max_line_width = 250

    svg = renderer.render_document(document)

    assert svg.count(">tekst<") == 10
