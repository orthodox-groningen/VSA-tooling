from vsa.parser import Parser
from vsa.svg_renderer import SVGRenderer
from vsa.svg_line_layout import build_lines


def test_text_width_preserves_spaces_between_words():
    document = Parser(r"de Heer en goed").parse()

    svg = SVGRenderer().render_document(document)

    assert 'xml:space="preserve"' in svg
    assert "de " in svg
    assert "Heer " in svg
    assert "en " in svg


def test_line_width_counts_spaces():
    spaced = Parser(r"de Heer").parse()
    compact = Parser(r"deHeer").parse()

    spaced_width = build_lines(spaced)[0].width
    compact_width = build_lines(compact)[0].width

    assert spaced_width > compact_width


def test_scope_gap_is_zero_by_default():
    from vsa.config import SVGRenderingConfig

    assert SVGRenderingConfig().scope_gap == 0.0
