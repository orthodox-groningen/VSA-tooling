"""Pad B: VSA-S + template A/T/B voor tropaar-toon-4 (Elia)."""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

import render_vsa_template_musicxml as render  # noqa: E402
import yaml  # noqa: E402

from vsa.pad_b import PadBError, map_stanza, map_vsa_to_template  # noqa: E402
from vsa.vsa_stanzas import extract_stanza_notes  # noqa: E402

LIBRARY = ROOT / "docs" / "specification-vsa-templates" / "library"
TEMPLATE_YAML = LIBRARY / "tropaar-toon-4" / "template.yaml"
ELIA_VSA = LIBRARY / "tropaar-toon-4" / "examples" / "elia.vsa"


def _template() -> dict:
    return yaml.safe_load(TEMPLATE_YAML.read_text(encoding="utf-8"))


def _elia_text() -> str:
    return ELIA_VSA.read_text(encoding="utf-8")


def test_elia_has_seven_stanzas() -> None:
    stanzas = extract_stanza_notes(_elia_text())
    assert len(stanzas) == 7
    assert [n.lyric for n in stanzas[0]] == [
        "Gij",
        "waart",
        "een",
        "En",
        "gel",
        "in",
        "het",
        "vlees",
    ]


def test_elia_r1_recite_then_cadence() -> None:
    doc = _template()
    stanzas = extract_stanza_notes(_elia_text())
    phrase = next(p for p in doc["phrases"] if p["id"] == "1")
    mapped = map_stanza(stanzas[0], phrase, do=doc["do"], mode=doc["mode"])
    roles = [n.template_event["role"] for n in mapped]
    lyrics = [n.lyric for n in mapped]
    assert lyrics[:3] == ["Gij", "waart", "een"]
    assert roles[:3] == ["recite", "recite", "recite"]
    assert lyrics[3:5] == ["En", "gel"]
    assert roles[3:5] == ["cadence", "cadence"]
    assert [str(n.s_pitch) for n in mapped[5:7]] == ["Bb4", "Bb4"]
    assert mapped[-1].lyric == "vlees"
    assert str(mapped[-1].s_pitch) == "A4"


def test_elia_r2_skips_optional_link_uses_e_st() -> None:
    doc = _template()
    stanzas = extract_stanza_notes(_elia_text())
    phrase = next(p for p in doc["phrases"] if p["id"] == "2")
    mapped = map_stanza(stanzas[1], phrase, do=doc["do"], mode=doc["mode"])
    assert mapped[0].lyric == "de"
    assert mapped[0].template_event.get("anchor") == "e.st."
    assert mapped[0].show_anchor
    assert not any(n.template_event.get("optional") for n in mapped)
    recite_lyrics = [
        n.lyric for n in mapped if n.template_event.get("role") == "recite"
    ]
    assert recite_lyrics == ["grond", "slag", "der", "pro"]
    assert all(n.duration.note_type == "quarter" for n in mapped if n.template_event.get("role") == "recite")
    assert mapped[-1].lyric == "ten"
    assert mapped[-1].template_event.get("role") == "cadence"


def test_elia_full_phrase_assignment() -> None:
    mapped = map_vsa_to_template(_template(), _elia_text())
    assert [pid for pid, _ in mapped] == [
        "1",
        "2",
        "1",
        "2",
        "1",
        "2",
        "laatste",
    ]
    assert [len(notes) for _, notes in mapped] == [8, 7, 11, 6, 16, 11, 19]
    for _, notes in mapped:
        for note in notes:
            if note.template_event.get("role") == "recite":
                assert note.duration.note_type == "quarter"


def test_elia_r3_voorloper_is_three_quarters() -> None:
    mapped = map_vsa_to_template(_template(), _elia_text())
    lyrics = [n.lyric for n in mapped[2][1]]
    assert lyrics[4:7] == ["Voor", "lo", "per"]
    assert all(n.duration.note_type == "quarter" for n in mapped[2][1][4:7])


def test_elia_pad_b_mscx_has_lyrics_no_repeats_no_breve() -> None:
    doc = _template()
    mapped = map_vsa_to_template(doc, _elia_text())
    mscx = render.render_pad_b_mscx(doc, mapped, title="T4-06 — Profeet Elia (pad B)")
    staff1 = re.search(r'<Staff id="1">(.*?)</Staff>', mscx, re.DOTALL)
    assert staff1
    body = staff1.group(1)
    # Layout mag splitsen; onzichtbare binnen-strofe-maten via <BarLine visible=0>.
    n_meas = body.count("<Measure len=")
    n_hidden = body.count("<subtype>normal</subtype><visible>0</visible>")
    assert n_meas >= 7
    assert n_meas - n_hidden == 7
    assert "<startRepeat/>" not in mscx
    assert "<headType>breve</headType>" not in mscx
    assert "<Lyrics>" in mscx
    assert "<text>Gij</text>" in mscx
    assert "<text>vlees</text>" in mscx
    assert "<text>grond-</text>" in mscx or "<text>Voor-</text>" in mscx
    assert f"<lyricsOddFontFace>{render.LYRIC_FONT}</lyricsOddFontFace>" in mscx
    assert f"<family>{render.LYRIC_FONT}</family>" in mscx
    assert f"<minNoteDistance>{render.PAD_B_MIN_NOTE_DISTANCE}</minNoteDistance>" in mscx
    assert "<LayoutBreak>" not in mscx  # instance: MuseScore pakt systemen zelf
    # Geen formule-labels / ankers / cycle-frames in pad-B instance.
    assert "l. st" not in mscx
    assert "l.st." not in mscx
    assert "↓" not in mscx
    assert "<HBox>" not in mscx
    # Alleen titel-VBox, geen cycle-VBox met frase-volgorde.
    assert body.count("<VBox>") == 1
    # Geen [1] / [laatste] staff text (rectangle frase-id).
    assert not re.search(
        r"<StaffText>.*?rectangle.*?<text>(1|2|laatste)</text>",
        mscx,
        re.DOTALL,
    )
    assert "<showTimeSig>0</showTimeSig>" in mscx
    assert "<genCourtesyTimesig>0</genCourtesyTimesig>" in mscx
    assert f"<measureSpacing>{render.PAD_B_MEASURE_SPACING}</measureSpacing>" in mscx
    assert "<stretch>0.85</stretch>" in mscx
    # SA/TB als akkoord (één stem) → geen tweede <voice> met alleen A/B.
    assert body.count("<voice>") == n_meas
    # Melisma-slurs ook op SA-balk (niet alleen TB).
    assert body.count('Spanner type="Slur"') >= 2


def test_elia_pad_b_hyphens_and_melisma_slurs() -> None:
    doc = _template()
    mapped = map_vsa_to_template(doc, _elia_text())
    mscx = render.render_pad_b_mscx(doc, mapped, title="Elia pad B")
    assert "<text>Voor-</text>" in mscx
    assert "<text>lo-</text>" in mscx
    assert "<text>per</text>" in mscx
    assert "<text>ge-</text>" in mscx
    assert "<text>ne-</text>" in mscx
    assert "<text>zing</text>" in mscx
    # Geplakte VSA-woorden: {En_}gel, pro{fe_}{\ten_}
    assert "<text>En-</text>" in mscx
    assert "<text>gel</text>" in mscx
    assert "<text>pro-</text>" in mscx
    assert "<text>fe-</text>" in mscx
    assert "<text>ten</text>" in mscx
    # Melisma-lettergrepen houden ook een streepje (li-, e-).
    assert "<text>li-</text>" in mscx or "<text>e-</text>" in mscx
    assert 'Spanner type="Slur"' in mscx
    assert "<ticks>" in mscx


def test_elia_glued_words_get_syllabic() -> None:
    stanzas = extract_stanza_notes(_elia_text())
    assert [(n.lyric, n.syllabic) for n in stanzas[0] if n.lyric][3:5] == [
        ("En", "begin"),
        ("gel", "end"),
    ]
    assert [(n.lyric, n.syllabic) for n in stanzas[1] if n.lyric][4:7] == [
        ("pro", "begin"),
        ("fe", "middle"),
        ("ten", "end"),
    ]


def test_elia_pad_b_instance_layout_packs_systems() -> None:
    doc = _template()
    mapped = map_vsa_to_template(doc, _elia_text())
    mscx = render.render_pad_b_mscx(doc, mapped, title="Elia pad B")
    assert f"<minNoteDistance>{render.PAD_B_MIN_NOTE_DISTANCE}</minNoteDistance>" in mscx
    assert "<lastSystemFillLimit>0</lastSystemFillLimit>" in mscx
    staff1 = re.search(r'<Staff id="1">(.*?)</Staff>', mscx, re.DOTALL)
    assert staff1
    body = staff1.group(1)
    n_meas = body.count("<Measure len=")
    n_hidden = body.count("<subtype>normal</subtype><visible>0</visible>")
    n_breaks = body.count("<LayoutBreak>")
    assert n_meas >= 7
    assert n_meas - n_hidden == 7
    assert n_breaks == 0


def test_elia_pad_b_elia_a_is_half() -> None:
    """VSA ``{\\a_}`` → half op laatste cadens van frase 2."""
    mapped = map_vsa_to_template(_template(), _elia_text())
    lyrics = [(n.lyric, n.duration.note_type) for n in mapped[3][1]]
    assert ("a", "half") in lyrics


def test_elia_pad_b_musicxml_coria_nonempty() -> None:
    doc = _template()
    mapped = map_vsa_to_template(doc, _elia_text())
    xml = render.render_pad_b_musicxml(doc, mapped, title="Elia pad B")
    assert len(xml) > 1000
    assert "<score-partwise" in xml
    assert "<lyric" in xml
    assert 'slur type="start"' in xml
    assert "<text>Voor-</text>" in xml or ">Voor-</text>" in xml or (
        "<syllabic>begin</syllabic><text>Voor</text>" in xml.replace("\n", "")
    )
    assert "<text>En-</text>" not in xml  # streepje komt uit syllabic, niet uit text
    assert "<syllabic>begin</syllabic><text>En</text>" in xml.replace("\n", "")
    assert "<syllabic>begin</syllabic><text>pro</text>" in xml.replace("\n", "")
    assert "<!DOCTYPE" not in xml
    assert "<extend type=\"stop\"/>" not in xml
    assert "<extend type=\"continue\"/>" not in xml
    # Vier aparte parts voor solo-oefenen in Coria.
    assert "<part-name>Soprano</part-name>" in xml
    assert "<part-name>Alto</part-name>" in xml
    assert "<part-name>Tenor</part-name>" in xml
    assert "<part-name>Bass</part-name>" in xml
    assert 'id="P4"' in xml
    # Tenor: F-sleutel; geen geforceerde stokrichting (auto naar midden).
    tenor = re.search(r'<part id="P3">(.*?)</part>', xml, re.DOTALL)
    assert tenor
    assert "<sign>F</sign>" in tenor.group(1)
    assert "clef-octave-change" not in tenor.group(1)
    assert "<stem>up</stem>" not in tenor.group(1)
    assert "<stem>down</stem>" not in tenor.group(1)
    # Één maat per strofe (7), geen splits binnen een frase.
    sop = re.search(r'<part id="P1">(.*?)</part>', xml, re.DOTALL)
    assert sop
    assert sop.group(1).count("<measure number=") == 7
    # #do (alt) = F# met alter én accidental (Coria).
    assert "<step>F</step><alter>1</alter>" in xml.replace("\n", "")
    assert "<accidental>sharp</accidental>" in xml
    # Bb in F-dur: alter blijft, géén overbodige <accidental>flat>.
    assert "<accidental>flat</accidental>" not in xml
    # Lyrics op elke stem (Coria solo/mute).
    for pid in ("P1", "P2", "P3", "P4"):
        part = re.search(rf'<part id="{pid}">(.*?)</part>', xml, re.DOTALL)
        assert part, pid
        assert "<lyric" in part.group(1), pid
        assert "<text>Voor</text>" in part.group(1), pid
    path_mxl = LIBRARY / "tropaar-toon-4" / "examples" / "elia.mxl"
    assert path_mxl.is_file() and path_mxl.stat().st_size > 0


def test_elia_pad_b_musicxml_alto_fs_has_accidental() -> None:
    """Laatste A van [1] is #do → F#; zonder accidental speelt Coria F."""
    doc = _template()
    mapped = map_vsa_to_template(doc, _elia_text())
    events = render.prepare_pad_b_events(
        render.mapped_notes_to_events(mapped[0][1], doc["do"], doc["mode"])
    )
    last_a = events[-1]["pitches"]["A"]
    assert last_a == ("F", 1, 4)
    xml = render.render_pad_b_musicxml(doc, mapped, title="Elia pad B")
    # Alto-part (P2) moet F# met accidental bevatten.
    alto = re.search(r'<part id="P2">(.*?)</part>', xml, re.DOTALL)
    assert alto
    assert "<accidental>sharp</accidental>" in alto.group(1)
    assert re.search(
        r"<step>F</step>\s*<alter>1</alter>\s*<octave>4</octave>",
        alto.group(1),
    )


def test_elia_pad_b_visible_barline_per_stanza() -> None:
    doc = _template()
    mapped = map_vsa_to_template(doc, _elia_text())
    mscx = render.render_pad_b_mscx(doc, mapped, title="Elia pad B")
    staff1 = re.search(r'<Staff id="1">(.*?)</Staff>', mscx, re.DOTALL)
    assert staff1
    body = staff1.group(1)
    n_meas = body.count("<Measure len=")
    n_hidden = body.count("<subtype>normal</subtype><visible>0</visible>")
    assert n_meas - n_hidden == 7
    lens = re.findall(r'<Measure len="([^"]+)">', body)
    assert all("/" in x for x in lens)


def test_pitch_mismatch_in_laatste_raises() -> None:
    """mi–fa–mi op template mi–re–mi (oude T4-08) → hoogte-mismatch, geen stil hold."""
    doc = _template()
    phrase = next(p for p in doc["phrases"] if p["id"] == "laatste")
    # Schep-melisma als vroeger fout: /-&_ → mi–fa–mi i.p.v. mi–re–mi.
    text = (
        "---\ndo: F4\nmode: major\n---\n\n"
        "// Ver-vul-ling van het Heils-plan van de {-&/Schep_&_}{\\per_}. [//:]\n"
    )
    stanzas = extract_stanza_notes(text)
    with pytest.raises(PadBError, match="hoogte-mismatch"):
        map_stanza(stanzas[0], phrase, do=doc["do"], mode=doc["mode"])


def test_pitch_mismatch_past_tail_raises() -> None:
    doc = _template()
    phrase = next(p for p in doc["phrases"] if p["id"] == "laatste")
    # Cadens al klaar (mi–re–mi), daarna nog een scoped fa.
    text = (
        "---\ndo: F4\nmode: major\n---\n\n"
        "// xxx {-&\\a_&_}{/b_}{\\c_}{/extra_}. [//:]\n"
    )
    stanzas = extract_stanza_notes(text)
    with pytest.raises(PadBError, match="hoogte-mismatch"):
        map_stanza(stanzas[0], phrase, do=doc["do"], mode=doc["mode"])


def test_elia_pad_b_s_from_vsa_atb_from_template() -> None:
    doc = _template()
    mapped = map_vsa_to_template(doc, _elia_text())
    events = render.mapped_notes_to_events(mapped[0][1], doc["do"], doc["mode"])
    # Recite A/T/B = do / sol-1 / do-1 → F4 / C4 / F3
    assert events[0]["pitches"]["S"] == ("A", 0, 4)
    assert events[0]["pitches"]["A"] == ("F", 0, 4)
    assert events[0]["pitches"]["T"] == ("C", 0, 4)
    assert events[0]["pitches"]["B"] == ("F", 0, 3)
    # {/in} = fa → A/T/B re / la-1 / re-1
    in_ev = next(ev for ev in events if ev.get("lyric") == "in")
    assert in_ev["pitches"]["S"] == ("B", -1, 4)
    assert in_ev["pitches"]["A"] == ("G", 0, 4)


def test_elia_pad_b_mscz_written() -> None:
    path = LIBRARY / "tropaar-toon-4" / "examples" / "elia.mscz"
    assert path.is_file(), "run: python scripts\\render_tropaar_toon4_corpus.py"
    with zipfile.ZipFile(path) as archive:
        mscx = archive.read("score.mscx").decode("utf-8")
    assert "<Lyrics>" in mscx
    assert "Profeet Elia" in mscx or "Elia" in mscx
