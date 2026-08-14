"""Corpus stap 1: stanza-telling en uitgevouwen formule-MSCX."""

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

from vsa.corpus_vsa import CORPUS_ENTRIES, count_stanzas, load_corpus  # noqa: E402
from vsa.template_mapping import assign_stanzas_to_phrases, select_mapping_plan  # noqa: E402

LIBRARY = ROOT / "docs" / "specification-vsa-templates" / "library"
TEMPLATE_YAML = LIBRARY / "tropaar-toon-4" / "template.yaml"
ONDERZOEK = ROOT / "docs" / "plans" / "onderzoeks-troparen-en-kondaken.md"

# Regels uit corpus.md (overzichtstabel).
EXPECTED_STANZAS: dict[str, int] = {
    "T4-01": 6,
    "T4-02": 7,
    "T4-03": 6,
    "T4-04": 9,
    "T4-05": 7,
    "T4-06": 7,
    "T4-07": 7,
    "T4-08": 7,
    "T4-09": 7,
    "T4-10": 5,
    "T4-11": 7,
    "T4-12": 7,
}

ELIA_PHRASES = ["1", "2", "1", "2", "1", "2", "laatste"]


@pytest.mark.parametrize("piece_id,expected", EXPECTED_STANZAS.items())
def test_corpus_stanza_counts(piece_id: str, expected: int) -> None:
    piece = next(p for p in load_corpus(ONDERZOEK) if p.piece_id == piece_id)
    assert piece.stanza_count == expected


def test_corpus_has_twelve_pieces() -> None:
    assert len(CORPUS_ENTRIES) == 12
    assert len(load_corpus(ONDERZOEK)) == 12


def test_elia_phrase_assignment() -> None:
    doc = render.load_resolved(TEMPLATE_YAML, LIBRARY)
    plan = select_mapping_plan(doc, 7)
    assert assign_stanzas_to_phrases(plan, 7) == ELIA_PHRASES


def _staff1_block(mscx: str) -> str:
    match = re.search(r'<Staff id="1">(.*?)</Staff>', mscx, re.DOTALL)
    assert match, "staff 1 not found"
    return match.group(1)


def _measure_count_staff1(mscx: str) -> int:
    return _staff1_block(mscx).count("<Measure len=")


def test_expanded_elia_has_seven_measures_no_repeats() -> None:
    doc = render.load_resolved(TEMPLATE_YAML, LIBRARY)
    mscx = render.render_expanded_mscx(
        doc,
        ELIA_PHRASES,
        title="T4-06 — Profeet Elia",
    )
    assert _measure_count_staff1(mscx) == 7
    assert "<startRepeat/>" not in mscx
    assert "<endRepeat>" not in mscx
    assert "Profeet Elia" in mscx
    assert ", ".join(ELIA_PHRASES) in mscx


def test_expanded_elia_frase_labels_in_order() -> None:
    doc = render.load_resolved(TEMPLATE_YAML, LIBRARY)
    mscx = render.render_expanded_mscx(
        doc,
        ELIA_PHRASES,
        title="T4-06 — Profeet Elia",
    )
    staff1 = _staff1_block(mscx)
    labels = re.findall(
        r'<frameType>1</frameType><text>.*?>([\w]+)</text>',
        staff1,
    )
    assert labels == ELIA_PHRASES


def test_andreas_five_measures() -> None:
    doc = render.load_resolved(TEMPLATE_YAML, LIBRARY)
    plan = select_mapping_plan(doc, 5)
    phrase_ids = assign_stanzas_to_phrases(plan, 5)
    assert phrase_ids == ["1", "2", "1", "2", "laatste"]
    mscx = render.render_expanded_mscx(
        doc,
        phrase_ids,
        title="T4-10 — Apostel Andreas",
    )
    assert _measure_count_staff1(mscx) == 5


def test_corpus_batch_generates_mscz_files() -> None:
    corpus_dir = TEMPLATE_YAML.parent / "examples" / "corpus"
    expected = {f"{pid}-{slug}.mscz" for pid, slug, _ in CORPUS_ENTRIES}
    missing = expected - {p.name for p in corpus_dir.glob("*.mscz")}
    assert not missing, f"missing corpus mscz: {sorted(missing)}"
    for path in corpus_dir.glob("T4-*.mscz"):
        with zipfile.ZipFile(path) as archive:
            mscx = archive.read("score.mscx").decode("utf-8")
        assert "<Measure " in mscx
        assert "<startRepeat/>" not in mscx
