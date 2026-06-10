from vsa.parser import Parser
from vsa.svg_renderer import SVGRenderer


def test_svg_contains_original_plain_text_metadata():
    document = Parser(r"[:] {/Hei_}{/lig_} is de Heer. [:]").parse()

    svg = SVGRenderer().render_document(document)

    assert "<!-- plain-text: is de Heer. -->" in svg
    assert "is de Heer" in svg
