"""Tests for MusicXML reciting-tone and hyphen syllable splitting."""

import xml.etree.ElementTree as ET

from vsa.musicxml_renderer import (
    MusicXMLRenderer,
    RECITING_MODE_WHOLE,
    _syllables_from_token,
    _syllables_from_tokens,
)
from vsa.parser import Parser


def _lyrics(xml: str) -> list[tuple[str, str]]:
    root = ET.fromstring(xml.split("dtd\">", 1)[-1])
    result = []
    for note in root.iter("note"):
        lyric = note.find("lyric")
        if lyric is None:
            continue
        text = lyric.findtext("text") or ""
        syllabic = lyric.findtext("syllabic") or ""
        if text or syllabic:
            result.append((text, syllabic))
    return result


def test_syllables_from_token_hyphen():
    assert _syllables_from_token("mel-se") == [("mel-", "begin"), ("se", "end")]
    assert _syllables_from_token("a-b-c") == [
        ("a-", "begin"),
        ("b-", "middle"),
        ("c", "end"),
    ]
    assert _syllables_from_token("woord") == [("woord", "single")]


def test_syllables_from_tokens_multiple_words():
    assert _syllables_from_tokens(["mel-se", "en"]) == [
        ("mel-", "begin"),
        ("se", "end"),
        ("en", "single"),
    ]


def test_reciting_quarters_default_one_note_per_word():
    doc = Parser("[:] {/do_} jubelen en zich ver {/eind_}").parse()
    xml = MusicXMLRenderer(metadata={"do": "F4", "mode": "major"}).render(doc)
    lyrics = _lyrics(xml)
    assert ("jubelen", "single") in lyrics
    assert ("en", "single") in lyrics
    assert ("zich", "single") in lyrics
    assert ("ver", "single") in lyrics
    assert not any("jubelen en zich ver" in t for t, _ in lyrics)


def test_reciting_hyphen_in_plain_text():
    doc = Parser("[:] {//he}mel-se {/eind_}").parse()
    xml = MusicXMLRenderer(metadata={"do": "F4", "mode": "major"}).render(doc)
    lyrics = _lyrics(xml)
    assert ("mel-", "begin") in lyrics
    assert ("se", "end") in lyrics


def test_reciting_whole_mode_long_sequence():
    doc = Parser("[:] {/a_} een twee drie vier {/b_}").parse()
    xml = MusicXMLRenderer(
        metadata={"do": "F4", "mode": "major", "reciting-mode": RECITING_MODE_WHOLE},
    ).render(doc)
    lyrics = _lyrics(xml)
    assert any(t == "een twee drie vier" for t, _ in lyrics)
