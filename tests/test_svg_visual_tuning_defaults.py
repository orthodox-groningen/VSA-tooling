from vsa.config import SVGRenderingConfig
from vsa.svg_glyphs import SVGGlyphRenderer


def test_visual_tuning_defaults_are_compact():
    config = SVGRenderingConfig()

    assert config.line_height == 38.0
    assert config.margin_x == 8.0
    assert config.margin_y == 8.0
    assert config.upper.width_factor == 0.48
    assert config.lower.width_factor == 0.55


def test_stacked_slash_gap_is_larger_than_previous_compact_gap():
    glyphs = SVGGlyphRenderer(unit=8.0)
    parts = glyphs.render_height_modifier(["//"], 0, 20, 24)
    svg = "\n".join(parts)

    assert svg.count("vsa-glyph-rise") == 2
    assert 'y1="22.43"' in svg
    assert 'y1="18.75"' in svg
