from vsa.svg_glyphs import SVGGlyphRenderer


def test_render_up_slash_as_line():
    renderer = SVGGlyphRenderer()

    parts = renderer.render_height_modifier(["/"], 0, 20, 20)

    assert any("<line" in part for part in parts)


def test_render_double_underscore_as_two_lines():
    renderer = SVGGlyphRenderer()

    parts = renderer.render_length_modifier(["__"], 0, 20, 40)

    assert len([part for part in parts if "<line" in part]) == 2


def test_render_dots_as_filled_circles():
    renderer = SVGGlyphRenderer()

    parts = renderer.render_length_modifier([".."], 0, 20, 40)

    assert len([part for part in parts if "<circle" in part]) == 2
    assert not any("vsa-glyph-dot" in part and "<line" in part for part in parts)
