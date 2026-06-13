from vsa.config import SVGRenderingConfig
from vsa.parser import Parser
from vsa.scope_layout import build_scope_layout, estimate_scope_text_width
from vsa.svg_glyphs import SVGGlyphRenderer
from vsa.svg_renderer import SVGRenderer


def test_upper_glyph_offset_is_higher():
    assert SVGRenderingConfig().upper.offset_y == -22.0


def test_text_width_estimate_is_roomier():
    assert estimate_scope_text_width("baard", 20) == 55.0


def test_multi_ehm_scope_forces_filler_space():
    document = Parser(r"{/&/&/&/schon}").parse()
    layout = build_scope_layout(document.nodes[0])

    assert layout.filler_width > 0


def test_single_ehm_glyph_is_capped_to_accent_width():
    glyphs = SVGGlyphRenderer(unit=8.0)
    svg = "\n".join(glyphs.render_height_modifier(["/"], 0, 20, 80))

    assert 'x1="34.60"' in svg
    assert 'x2="45.40"' in svg


def test_filler_line_uses_dash_height_not_upper_y():
    document = Parser(r"{/&/&/&/schon}").parse()
    svg = SVGRenderer().render_document(document)

    assert "vsa-filler-line" in svg
    assert 'y1="30.00"' in svg
