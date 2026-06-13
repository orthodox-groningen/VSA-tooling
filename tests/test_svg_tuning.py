from vsa.config import SVGRenderingConfig
from vsa.parser import Parser
from vsa.scope_layout import build_scope_layout
from vsa.svg_glyphs import SVGGlyphRenderer


def test_default_lower_width_factor_is_compact():
    config = SVGRenderingConfig()

    assert config.lower.width_factor == 0.55
    assert config.scope_gap == 0.0


def test_single_modifier_scope_is_not_forced_to_large_width():
    document = Parser(r"{Gij_}").parse()

    layout = build_scope_layout(document.nodes[0])

    assert layout.width < 40


def test_stacked_slashes_are_less_steep_and_distinguishable():
    glyphs = SVGGlyphRenderer(unit=8.0)
    parts = glyphs.render_height_modifier(["//"], 0, 20, 24)
    svg = "\n".join(parts)

    assert svg.count("vsa-glyph-rise") == 2
    assert 'y1="22.43"' in svg
    assert 'y1="18.75"' in svg
