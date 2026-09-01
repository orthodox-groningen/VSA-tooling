"""Tests for '-.' and '~.' (dotted-quarter) length modifiers.

Both tokens mean 1½ × standard duration. SVG is a left-half underline.
MusicXML default mapping is a dotted quarter note.
"""

import xml.etree.ElementTree as ET

import pytest

from vsa.duration_model import elm_to_duration
from vsa.musicxml_renderer import MusicXMLRenderer
from vsa.parser import ELM_VALUES, Parser
from vsa.svg_glyphs import SVGGlyphRenderer


def test_elm_values_contains_dotted_quarter_tokens():
    assert "-." in ELM_VALUES
    assert "~." in ELM_VALUES


def test_elm_values_dotted_quarter_before_shorter_tokens():
    assert ELM_VALUES.index("-.") < ELM_VALUES.index("-")
    assert ELM_VALUES.index("-.") < ELM_VALUES.index(".")
    assert ELM_VALUES.index("~.") < ELM_VALUES.index("~")
    assert ELM_VALUES.index("~.") < ELM_VALUES.index(".")


class TestParserDottedQuarter:
    def test_dash_dot(self):
        node = Parser("{tekst-.}").parse().nodes[0]
        assert node.length_modifier == ["-."]
        assert node.text == "tekst"

    def test_tilde_dot(self):
        node = Parser("{tekst~.}").parse().nodes[0]
        assert node.length_modifier == ["~."]
        assert node.text == "tekst"

    def test_height_and_dash_dot(self):
        node = Parser("{/tekst-.}").parse().nodes[0]
        assert node.height_modifier == ["/"]
        assert node.length_modifier == ["-."]

    def test_compound_with_dotted_quarter(self):
        node = Parser("{tekst-.&~}").parse().nodes[0]
        assert node.length_modifier == ["-.", "~"]

    def test_dash_alone_still_standard(self):
        node = Parser("{tekst-}").parse().nodes[0]
        assert node.length_modifier == ["-"]

    def test_underscore_dot_still_dotted_half(self):
        node = Parser("{tekst_.}").parse().nodes[0]
        assert node.length_modifier == ["_."]


class TestDurationDottedQuarter:
    def test_dash_dot_is_dotted_quarter(self):
        dur = elm_to_duration("-.")
        assert dur.note_type == "quarter"
        assert dur.dots == 1
        assert dur.divisions_value == 6

    def test_tilde_dot_same_as_dash_dot(self):
        assert elm_to_duration("~.") == elm_to_duration("-.")


class TestSVGDottedQuarter:
    def setup_method(self):
        self.renderer = SVGGlyphRenderer(unit=10.0)

    def test_dash_dot_is_left_half_line(self):
        parts = self.renderer._render_elm("-.", cx=50, y=20, col_width=30)
        lines = [p for p in parts if "<line" in p]
        assert len(lines) == 1
        import re

        x1 = float(re.search(r'x1="([^"]+)"', lines[0]).group(1))
        x2 = float(re.search(r'x2="([^"]+)"', lines[0]).group(1))
        assert x1 < 50
        assert x2 == pytest.approx(50.0)

    def test_tilde_dot_same_glyph_as_dash_dot(self):
        a = self.renderer._render_elm("-.", cx=50, y=20, col_width=30)
        b = self.renderer._render_elm("~.", cx=50, y=20, col_width=30)
        assert a == b


class TestMusicXMLDottedQuarter:
    def _note_types(self, xml: str) -> list[tuple[str, int]]:
        root = ET.fromstring(xml.split('dtd">', 1)[-1])
        notes = []
        for note in root.iter("note"):
            if note.find("rest") is not None:
                continue
            ntype = note.findtext("type") or ""
            dots = len(note.findall("dot"))
            notes.append((ntype, dots))
        return notes

    def test_dash_dot_exports_dotted_quarter(self):
        doc = Parser("[:] {/Heer-.}").parse()
        xml = MusicXMLRenderer(metadata={"do": "F4", "mode": "major"}).render(doc)
        assert ("quarter", 1) in self._note_types(xml)

    def test_tilde_dot_exports_dotted_quarter(self):
        doc = Parser("[:] {/Heer~.}").parse()
        xml = MusicXMLRenderer(metadata={"do": "F4", "mode": "major"}).render(doc)
        assert ("quarter", 1) in self._note_types(xml)
