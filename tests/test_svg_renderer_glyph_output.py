from vsa.parser import Parser
from vsa.svg_renderer import SVGRenderer


def test_svg_uses_real_lines_for_modifiers():
    document = Parser(r"[:] {/Hei_}{/lig_} is de Heer. [:]").parse()

    svg = SVGRenderer().render_document(document)

    assert "is" in svg
    assert "de" in svg
    assert "Heer" in svg
    assert "<line" in svg
    assert "<circle" not in svg


def test_svg_renders_dots():
    document = Parser(r"{tekst..}").parse()

    svg = SVGRenderer().render_document(document)

    assert svg.count('<circle') >= 2
    assert svg.count('vsa-glyph-dot') == 2
