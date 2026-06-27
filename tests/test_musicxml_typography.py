"""Tests for MusicXML typography defaults from frontmatter."""

import xml.etree.ElementTree as ET

from vsa.block_parser import DEFAULT_METADATA
from vsa.musicxml_renderer import MusicXMLRenderer
from vsa.parser import Parser


def _defaults_font(xml: str, tag: str) -> dict[str, str]:
    root = ET.fromstring(xml.split("dtd\">", 1)[-1])
    el = root.find(f".//defaults/{tag}")
    assert el is not None, f"missing <{tag}>"
    return dict(el.attrib)


def test_typography_fonts_in_defaults():
    doc = Parser("{/a_}").parse()
    xml = MusicXMLRenderer(
        metadata={
            "do": "F4",
            "mode": "major",
            "musicxml-profile": "engraving",
            "typografie.lyric-font": "Liberation Serif",
            "typografie.lyric-size": "14",
            "typografie.music-size": "12",
        },
    ).render(doc)

    assert _defaults_font(xml, "lyric-font") == {
        "font-family": "Liberation Serif",
        "font-size": "14",
    }
    assert _defaults_font(xml, "music-font") == {"font-size": "12"}


def test_typography_omitted_when_not_specified():
    doc = Parser("{/a_}").parse()
    xml = MusicXMLRenderer(
        metadata={"do": "F4", "mode": "major", "musicxml-profile": "engraving"},
    ).render(doc)
    root = ET.fromstring(xml.split("dtd\">", 1)[-1])
    assert root.find(".//defaults/lyric-font") is None
    assert root.find(".//defaults/music-font") is None


def test_typography_not_in_playback_profile():
    doc = Parser("{/a_}").parse()
    metadata = dict(DEFAULT_METADATA)
    xml = MusicXMLRenderer(metadata=metadata).render(doc)
    root = ET.fromstring(xml.split("dtd\">", 1)[-1])
    assert root.find(".//defaults") is None


def test_typography_defaults_from_block_metadata():
    doc = Parser("{/a_}").parse()
    metadata = dict(DEFAULT_METADATA)
    metadata["musicxml-profile"] = "engraving"
    xml = MusicXMLRenderer(metadata=metadata).render(doc)

    assert _defaults_font(xml, "lyric-font") == {
        "font-family": "Source Sans 3",
        "font-size": "13",
    }
    assert _defaults_font(xml, "word-font") == {
        "font-family": "Source Sans 3",
        "font-size": "12",
    }
    root = ET.fromstring(xml.split("dtd\">", 1)[-1])
    assert root.find(".//defaults/music-font") is None
