"""Tests for compressed MusicXML (.mxl) output."""

import xml.etree.ElementTree as ET
import zipfile

from vsa.musicxml_package import musicxml_output_suffix, write_musicxml_output
from vsa.musicxml_renderer import MusicXMLRenderer
from vsa.parser import Parser


def test_default_output_suffix_is_mxl():
    assert musicxml_output_suffix() == ".mxl"
    assert musicxml_output_suffix(format_name="musicxml") == ".musicxml"


def test_write_mxl_contains_score_xml(tmp_path):
    doc = Parser("{/a_}").parse()
    xml = MusicXMLRenderer(metadata={"do": "F4", "mode": "major"}).render(doc)
    out = tmp_path / "test.mxl"
    write_musicxml_output(out, xml)

    with zipfile.ZipFile(out) as archive:
        names = archive.namelist()
        assert names == ["META-INF/container.xml", "score.xml"]
        container = archive.read("META-INF/container.xml").decode()
        assert 'full-path="score.xml"' in container
        score = archive.read("score.xml").decode()
        assert score == xml
        root = ET.fromstring(score.split("dtd\">", 1)[-1])
        assert root.tag == "score-partwise"


def test_write_musicxml_plain(tmp_path):
    doc = Parser("{/a_}").parse()
    xml = MusicXMLRenderer(metadata={"do": "F4", "mode": "major"}).render(doc)
    out = tmp_path / "test.musicxml"
    write_musicxml_output(out, xml)
    assert out.read_text(encoding="utf-8") == xml
