from vsa.parser import Parser
from vsa.svg_line_layout import LineLayoutSettings, build_lines
from vsa.svg_renderer import SVGRenderer


def test_svg_renderer_draws_all_height_marker_dashes():
    document = Parser("[:] tekst [/:] meer [//:] einde").parse()
    svg = SVGRenderer().render_document(document)

    assert svg.count('class="vsa-pitch-marker-dash"') == 3
    assert svg.count('class="vsa-unit vsa-pitch-marker"') == 3


def test_svg_renderer_draws_height_glyphs_for_non_empty_height_markers():
    document = Parser("[:] tekst [/:] meer [//:] einde").parse()
    svg = SVGRenderer().render_document(document)

    # Eerste marker `[:]` heeft alleen een dash.
    # Tweede en derde marker hebben naast de dash ook hoogte-glyphs.
    assert svg.count('class="vsa-pitch-marker-upper-glyph vsa-upper-glyphs"') == 2


def test_svg_line_layout_counts_multiple_height_marker_widths():
    document = Parser("[:] tekst [/:] meer [//:] einde").parse()

    compact = build_lines(
        document,
        max_width=800,
        settings=LineLayoutSettings(pitch_marker_width=20, pitch_marker_gap=0),
    )
    spaced = build_lines(
        document,
        max_width=800,
        settings=LineLayoutSettings(pitch_marker_width=20, pitch_marker_gap=10),
    )

    assert len(compact) == 1
    assert len(spaced) == 1
    assert spaced[0].width == compact[0].width + 30


def test_svg_renderer_keeps_text_before_between_and_after_height_markers():
    document = Parser("voor [:] tussen [\\:] na").parse()
    svg = SVGRenderer().render_document(document)

    assert "voor" in svg
    assert "tussen" in svg
    assert "na" in svg
    assert svg.count('class="vsa-unit vsa-pitch-marker"') == 2
