import re

from vsa.parser import Parser
from vsa.svg_layout_measure import measure_document_width
from vsa.svg_renderer import SVGRenderer


def _svg_width(svg: str):
    match = re.search(r'width="([0-9]+)"', svg)
    assert match
    return int(match.group(1))


def test_measure_short_document_width_is_not_1200():
    document = Parser("{tekst}").parse()

    width = measure_document_width(document)

    assert width < 300


def test_renderer_uses_measured_width():
    document = Parser("{tekst}").parse()

    svg = SVGRenderer().render_document(document)

    assert _svg_width(svg) < 300
    assert "viewBox" in svg


def test_longer_document_gets_wider_svg():
    short_doc = Parser("{tekst}").parse()
    long_doc = Parser("{lange} tekst met veel meer gewone woorden").parse()

    short_svg = SVGRenderer().render_document(short_doc)
    long_svg = SVGRenderer().render_document(long_doc)

    assert _svg_width(long_svg) > _svg_width(short_svg)
