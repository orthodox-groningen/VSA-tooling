from vsa.parser import Parser
from vsa.svg_renderer import SVGRenderer


def test_svg_renderer_keeps_text_nodes():
    document = Parser("[:] {/Hei_}{/lig_} is de Heer. [:]").parse()

    svg = SVGRenderer().render_document(document)

    assert svg.startswith("<svg")
    assert "</svg>" in svg
    assert "Hei" in svg
    assert "lig" in svg
    assert "is" in svg
    assert "de" in svg
    assert "Heer" in svg


def test_svg_renderer_does_not_use_debug_circles():
    document = Parser("{/tekst_}").parse()

    svg = SVGRenderer().render_document(document)

    assert "<circle" not in svg
    assert "tekst" in svg
    assert "<line" in svg


def test_svg_renderer_pitch_marker_line():
    document = Parser("[:] {tekst} [:]").parse()

    svg = SVGRenderer().render_document(document)

    assert svg.count("<line") == 2
