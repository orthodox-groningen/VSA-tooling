"""Tests for the '_ .' (dotted-half) length modifier.

'_.' means 3× standard duration. Its glyph is a full line above a
half-width line (left-aligned), matching the Liturgikon convention for
an anderhalve noot (dotted half note).
"""

import pytest

from vsa.parser import ELM_VALUES, Parser
from vsa.svg_glyphs import SVGGlyphRenderer


# ---------------------------------------------------------------------------
# ELM_VALUES ordering
# ---------------------------------------------------------------------------


def test_elm_values_contains_dotted_half():
    assert "_." in ELM_VALUES


def test_elm_values_dotted_half_before_single_underscore():
    assert ELM_VALUES.index("_.") < ELM_VALUES.index("_")


# ---------------------------------------------------------------------------
# Parser
# ---------------------------------------------------------------------------


class TestParserDottedHalf:
    def test_scope_with_dotted_half(self):
        node = Parser("{tekst_.}").parse().nodes[0]
        assert node.length_modifier == ["_."]
        assert node.text == "tekst"

    def test_scope_with_height_and_dotted_half(self):
        node = Parser("{/tekst_.}").parse().nodes[0]
        assert node.height_modifier == ["/"]
        assert node.length_modifier == ["_."]
        assert node.text == "tekst"

    def test_dotted_half_in_compound_modifier(self):
        node = Parser("{tekst_&_.}").parse().nodes[0]
        assert node.length_modifier == ["_", "_."]

    def test_double_underscore_still_parsed_correctly(self):
        node = Parser("{tekst__}").parse().nodes[0]
        assert node.length_modifier == ["__"]

    def test_double_dot_still_parsed_correctly(self):
        node = Parser("{tekst..}").parse().nodes[0]
        assert node.length_modifier == [".."]

    def test_underscore_dot_dot_is_invalid(self):
        """'_..' is not a valid ELM — parser must reject it."""
        with pytest.raises(Exception):
            Parser("{tekst_..}").parse()


# ---------------------------------------------------------------------------
# SVG renderer
# ---------------------------------------------------------------------------


class TestSVGDottedHalf:
    def setup_method(self):
        self.renderer = SVGGlyphRenderer(unit=10.0)

    def test_produces_two_line_segments(self):
        parts = self.renderer._render_elm("_.", cx=50, y=20, col_width=30)
        lines = [p for p in parts if "<line" in p]
        assert len(lines) == 2, "Expected exactly two line segments for '_. '"

    def test_top_line_is_full_width(self):
        parts = self.renderer._render_elm("_.", cx=50, y=20, col_width=30)
        lines = [p for p in parts if "<line" in p]
        # Top line: x1 < cx < x2 (spans both sides of centre)
        top = lines[0]
        assert 'x1="' in top and 'x2="' in top
        # Both x-coords should differ from cx; x1 < cx, x2 > cx
        import re
        x1 = float(re.search(r'x1="([^"]+)"', top).group(1))
        x2 = float(re.search(r'x2="([^"]+)"', top).group(1))
        assert x1 < 50 < x2, "Top line must span full width around centre"

    def test_bottom_line_is_left_half(self):
        parts = self.renderer._render_elm("_.", cx=50, y=20, col_width=30)
        lines = [p for p in parts if "<line" in p]
        bottom = lines[1]
        import re
        x1 = float(re.search(r'x1="([^"]+)"', bottom).group(1))
        x2 = float(re.search(r'x2="([^"]+)"', bottom).group(1))
        # Bottom line ends at cx (centre) — it is the left half only
        assert x2 == pytest.approx(50.0), "Bottom line must end at centre (cx)"
        assert x1 < 50, "Bottom line must start left of centre"

    def test_double_underscore_still_two_full_lines(self):
        parts = self.renderer._render_elm("__", cx=50, y=20, col_width=30)
        lines = [p for p in parts if "<line" in p]
        assert len(lines) == 2
        import re
        for line in lines:
            x2 = float(re.search(r'x2="([^"]+)"', line).group(1))
            assert x2 > 50, "Both '__' lines must be full width"
