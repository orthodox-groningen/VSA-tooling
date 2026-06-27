"""Tests for the playback MusicXML export profile (default)."""

import xml.etree.ElementTree as ET

from vsa.block_parser import DEFAULT_METADATA
from vsa.musicxml_renderer import (
    MUSICXML_PROFILE_ENGRAVING,
    MUSICXML_PROFILE_PLAYBACK,
    MusicXMLRenderer,
)
from vsa.parser import Parser


def _root(xml: str) -> ET.Element:
    return ET.fromstring(xml.split("dtd\">", 1)[-1])


def test_playback_is_default_profile():
    doc = Parser("{/a_}").parse()
    xml = MusicXMLRenderer(metadata={"do": "F4", "mode": "major"}).render(doc)
    root = _root(xml)
    assert root.find(".//score-instrument/instrument-sound") is not None
    assert root.find(".//defaults") is None


def test_playback_has_midi_part_list():
    doc = Parser("{/a_}").parse()
    metadata = dict(DEFAULT_METADATA)
    xml = MusicXMLRenderer(metadata=metadata).render(doc)
    root = _root(xml)

    assert root.find(".//score-instrument/instrument-sound").text == "keyboard.piano.grand"
    assert root.find(".//midi-instrument/midi-channel").text == "1"
    assert root.find(".//encoding/supports[@element='stem']") is not None


def test_playback_notes_have_voice_and_stem():
    doc = Parser("{/a_}").parse()
    xml = MusicXMLRenderer(
        metadata={"do": "F4", "mode": "major", "musicxml-profile": MUSICXML_PROFILE_PLAYBACK},
    ).render(doc)
    root = _root(xml)
    for note in root.findall(".//note"):
        assert note.findtext("voice") == "1"
        assert note.findtext("stem") == "up"


def test_playback_melisma_only_first_note_has_lyric():
    doc = Parser("{/&\\&/mel_&~&~}").parse()
    xml = MusicXMLRenderer(
        metadata={"do": "F4", "mode": "major", "musicxml-profile": MUSICXML_PROFILE_PLAYBACK},
    ).render(doc)
    root = _root(xml)
    lyrics = root.findall(".//note/lyric")
    assert len(lyrics) == 1
    assert lyrics[0].findtext("text") == "mel"
    assert lyrics[0].find("extend") is not None
    assert lyrics[0].find("extend").get("type") is None


def test_playback_no_regular_barlines():
    doc = Parser("{/a_} * {/b_}").parse()
    xml = MusicXMLRenderer(
        metadata={"do": "F4", "mode": "major", "musicxml-profile": MUSICXML_PROFILE_PLAYBACK},
    ).render(doc)
    root = _root(xml)
    bar_styles = [
        barline.findtext("bar-style")
        for barline in root.findall(".//barline")
    ]
    assert "regular" not in bar_styles
    assert bar_styles == ["light-heavy"]


def test_playback_double_barline_emitted():
    doc = Parser("{/a_} // {/b_}").parse()
    xml = MusicXMLRenderer(
        metadata={"do": "F4", "mode": "major", "musicxml-profile": MUSICXML_PROFILE_PLAYBACK},
    ).render(doc)
    root = _root(xml)
    bar_styles = [
        barline.findtext("bar-style")
        for barline in root.findall(".//barline")
    ]
    assert "light-light" in bar_styles
    assert "light-heavy" in bar_styles


def test_playback_beams_sixteenth_groups():
    doc = Parser("{/a_&..&..&..}").parse()
    xml = MusicXMLRenderer(
        metadata={"do": "F4", "mode": "major", "musicxml-profile": MUSICXML_PROFILE_PLAYBACK},
    ).render(doc)
    root = _root(xml)
    beams = root.findall(".//note/beam")
    assert len(beams) >= 6
    assert {beam.text for beam in beams} <= {"begin", "continue", "end"}


def test_engraving_profile_has_defaults_and_regular_barlines():
    doc = Parser("{/a_} * {/b_}").parse()
    metadata = dict(DEFAULT_METADATA)
    metadata["musicxml-profile"] = MUSICXML_PROFILE_ENGRAVING
    xml = MusicXMLRenderer(metadata=metadata).render(doc)
    root = _root(xml)

    assert root.find(".//defaults") is not None
    assert root.find(".//score-instrument") is None
    bar_styles = [
        barline.findtext("bar-style")
        for barline in root.findall(".//barline")
    ]
    assert "regular" in bar_styles


def test_engraving_melisma_typed_extend_on_middle_notes():
    doc = Parser("{/&\\&/mel_&~&~}").parse()
    xml = MusicXMLRenderer(
        metadata={"do": "F4", "mode": "major", "musicxml-profile": MUSICXML_PROFILE_ENGRAVING},
    ).render(doc)
    root = _root(xml)
    extend_types = [
        lyric.find("extend").get("type")
        for lyric in root.findall(".//note/lyric")
        if lyric.find("extend") is not None
    ]
    assert extend_types == ["start", "continue", "stop"]
