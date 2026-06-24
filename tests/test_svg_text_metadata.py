from xml.etree import ElementTree

from vsa.parser import Parser
from vsa.svg_renderer import SVGRenderer


def test_svg_does_not_contain_plain_text_metadata_comments():
    document = Parser(r"[:] {/Hei_}{/lig_} is de Heer. [:]").parse()

    svg = SVGRenderer().render_document(document)

    assert "<!-- plain-text:" not in svg
    assert "is" in svg
    assert "de" in svg
    assert "Heer" in svg
    ElementTree.fromstring(svg)
