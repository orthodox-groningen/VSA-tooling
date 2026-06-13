from vsa.parser import Parser
from vsa.svg_renderer import SVGRenderer


def test_svg_text_preserves_spaces():
    document = Parser(r"gedood door").parse()

    svg = SVGRenderer().render_document(document)

    assert 'xml:space="preserve"' in svg
    assert "gedood " in svg or "gedood door" in svg


def test_svg_margins_are_compact_by_default():
    svg = SVGRenderer().render_document(Parser(r"{tekst}").parse())

    assert 'width="80"' not in svg or 'height="120"' not in svg
