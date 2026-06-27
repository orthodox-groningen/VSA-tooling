"""Regressietests voor MusicXML-export.

Elk regressie-geval met een ``.musicxml-regression``-markerbestand wordt
vergeleken met zijn ``expected.musicxml``.

De test controleert:

- de structurele kenmerken van de uitvoer (stap/octaaf/type/text-inhoud);
- voor ongeldige invoer: dat de export wordt geweigerd.
"""

from pathlib import Path
import xml.etree.ElementTree as ET

import pytest

from vsa.block_parser import DEFAULT_METADATA
from vsa.musicxml_renderer import MusicXMLExportError, MusicXMLRenderer, MUSICXML_PROFILE_ENGRAVING
from vsa.parser import Parser
from vsa.yaml_frontmatter import frontmatter_to_block_metadata, parse_vsa_frontmatter


def _cases():
    base = Path("examples/regression")
    return [
        p
        for p in base.iterdir()
        if p.is_dir() and (p / ".musicxml-regression").exists()
    ]


@pytest.mark.parametrize("case", _cases(), ids=lambda p: p.name)
def test_musicxml_regression(case: Path):
    input_file = case / "input.vsa"
    expected_file = case / "expected.musicxml"

    assert input_file.exists(), f"Ontbreekt: {input_file}"
    assert expected_file.exists(), f"Ontbreekt: {expected_file}"

    expected_content = expected_file.read_text(encoding="utf-8").strip()

    source = input_file.read_text(encoding="utf-8")
    frontmatter, vsa_body = parse_vsa_frontmatter(source)
    fm_meta = frontmatter_to_block_metadata(frontmatter)

    metadata = dict(DEFAULT_METADATA)
    metadata.update(fm_meta)
    # Regression fixtures beschrijven het engraving-profiel (melisma, maatstrepen).
    metadata["musicxml-profile"] = MUSICXML_PROFILE_ENGRAVING

    document = Parser(vsa_body).parse()

    # Cases marked as invalid export
    if expected_content.startswith("<!--") and "niet mogelijk" in expected_content:
        with pytest.raises((MusicXMLExportError, Exception)):
            renderer = MusicXMLRenderer(metadata=metadata)
            renderer.render(document)
        return

    renderer = MusicXMLRenderer(metadata=metadata)
    actual_xml = renderer.render(document)

    # Validate that output is well-formed XML
    root = ET.fromstring(actual_xml.split("?>", 1)[-1].split("dtd\">", 1)[-1])
    assert root.tag == "score-partwise"

    # Validate against expected: compare key structural elements
    expected_root = ET.fromstring(
        expected_content.split("?>", 1)[-1].split("dtd\">", 1)[-1]
    )

    _assert_notes_match(actual_xml, expected_content, case.name)


def _assert_notes_match(actual_xml: str, expected_xml: str, case_name: str) -> None:
    """Compare notes (step, octave, type, lyric text) between actual and expected."""
    ns = ""

    def notes(xml_str: str):
        root = ET.fromstring(xml_str.split("?>", 1)[-1].split("dtd\">", 1)[-1])
        result = []
        for note in root.iter("note"):
            pitch = note.find("pitch")
            step = pitch.findtext("step") if pitch is not None else None
            octave = pitch.findtext("octave") if pitch is not None else None
            alter = pitch.findtext("alter") if pitch is not None else "0"
            note_type = note.findtext("type")
            lyric = note.find("lyric")
            text = lyric.findtext("text") if lyric is not None else ""
            syllabic = lyric.findtext("syllabic") if lyric is not None else ""
            result.append({
                "step": step, "octave": octave, "alter": alter or "0",
                "type": note_type, "text": text, "syllabic": syllabic,
            })
        return result

    actual_notes = notes(actual_xml)
    expected_notes = notes(expected_xml)

    assert len(actual_notes) == len(expected_notes), (
        f"{case_name}: verwacht {len(expected_notes)} noten, "
        f"maar kreeg {len(actual_notes)}."
    )

    for i, (a, e) in enumerate(zip(actual_notes, expected_notes)):
        assert a == e, (
            f"{case_name}: noot {i + 1} verschilt.\n"
            f"  Actueel:  {a}\n"
            f"  Verwacht: {e}"
        )
