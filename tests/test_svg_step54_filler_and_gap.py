from vsa.config import SVGRenderingConfig
from vsa.parser import Parser
from vsa.svg_renderer import SVGRenderer


def test_filler_line_uses_text_dash_height_not_upper_glyph_height():
    document = Parser(r"{/&/&/&/schon}").parse()
    svg = SVGRenderer().render_document(document)

    assert "vsa-filler-line" in svg
    assert 'y1="30.00"' in svg


def test_upper_glyph_height_remains_unchanged():
    assert SVGRenderingConfig().upper.offset_y == -22.0


def test_lower_glyphs_are_slightly_lower():
    assert SVGRenderingConfig().lower.offset_y == 7.0


def test_optical_scope_gap_is_configurable_default():
    assert SVGRenderingConfig().optical_scope_gap == 4.0


def test_adjacent_modified_scopes_receive_extra_visual_advance():
    document = Parser(r"me{\\de}{/eeu_}wi{\ge}").parse()

    normal = SVGRenderer()
    normal_svg = normal.render_document(document)

    no_gap_config = SVGRenderingConfig(optical_scope_gap=0.0)
    no_gap = SVGRenderer(svg_config=no_gap_config)
    no_gap_svg = no_gap.render_document(document)

    assert normal_svg != no_gap_svg
