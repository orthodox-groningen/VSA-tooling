from vsa.parser import Parser
from vsa.svg_renderer import SVGRenderer


def test_svg_grid_renderer_keeps_melisma_text_once():
    document = Parser(r"{/&\&/tekst_&~&~}").parse()

    svg = SVGRenderer().render_document(document)

    assert svg.count(">tekst<") == 1
    assert svg.count("<line") >= 2


def test_svg_grid_renderer_preserves_plain_text():
    document = Parser(r"[:] {/Hei_}{/lig_} is de Heer. [:]").parse()

    svg = SVGRenderer().render_document(document)

    assert "is" in svg
    assert "de" in svg
    assert "Heer" in svg
    assert "<line" in svg
