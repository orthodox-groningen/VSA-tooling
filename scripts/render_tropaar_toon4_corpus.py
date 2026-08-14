"""Genereer uitgevouwen formule-MSCX voor het tropaar-toon-4-corpus (stap 1)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LIBRARY = REPO / "docs" / "specification-vsa-templates" / "library"
TEMPLATE_DIR = LIBRARY / "tropaar-toon-4"
TEMPLATE_YAML = TEMPLATE_DIR / "template.yaml"
ONDERZOEK = REPO / "docs" / "plans" / "onderzoeks-troparen-en-kondaken.md"
CORPUS_DIR = TEMPLATE_DIR / "examples" / "corpus"

sys.path.insert(0, str(REPO / "src"))
sys.path.insert(0, str(REPO / "scripts"))

import render_vsa_template_musicxml as render  # noqa: E402

from vsa.corpus_vsa import load_corpus, write_vsa_file  # noqa: E402
from vsa.pad_b import map_vsa_to_template  # noqa: E402
from vsa.template_mapping import assign_stanzas_to_phrases, select_mapping_plan  # noqa: E402


def expanded_title(piece_id: str, title: str) -> str:
    return f"{piece_id} — {title}"


def render_pad_b_piece(doc: dict, piece, *, output_dir: Path, write_vsa: bool) -> Path:
    stem = piece.filename_stem()
    vsa_path = output_dir / f"{stem}.vsa"
    if write_vsa:
        write_vsa_file(piece, vsa_path)
    vsa_text = (
        vsa_path.read_text(encoding="utf-8")
        if vsa_path.exists()
        else (
            "---\n"
            f"title: {piece.title}\n"
            "do: F4\n"
            "mode: major\n"
            "---\n\n"
            f"{piece.body}\n"
        )
    )
    mapped = map_vsa_to_template(doc, vsa_text)
    title = expanded_title(piece.piece_id, piece.title) + " (pad B)"
    mscx = render.render_pad_b_mscx(doc, mapped, title=title)
    out = output_dir / f"{stem}.pad-b.mscz"
    render.write_mscx_output(out, mscx)
    if piece.piece_id == "T4-06":
        from vsa.musicxml_package import write_musicxml_output

        examples = TEMPLATE_DIR / "examples"
        render.write_mscx_output(examples / "elia.pad-b.mscz", mscx)
        # .mxl = gecomprimeerde MusicXML voor Coria; geen aparte .musicxml
        # (zelfde inhoud, alleen ongezipt).
        xml = render.render_pad_b_musicxml(doc, mapped, title=title)
        write_musicxml_output(examples / "elia.pad-b.mxl", xml)
        print(f"wrote {(examples / 'elia.pad-b.mscz').relative_to(REPO)}")
        print(f"wrote {(examples / 'elia.pad-b.mxl').relative_to(REPO)}")
    return out


def render_piece(
    doc: dict, piece, *, output_dir: Path, write_vsa: bool
) -> Path:
    plan = select_mapping_plan(doc, piece.stanza_count)
    phrase_ids = assign_stanzas_to_phrases(plan, piece.stanza_count)
    stem = piece.filename_stem()
    if write_vsa:
        write_vsa_file(piece, output_dir / f"{stem}.vsa")
    mscx = render.render_expanded_mscx(
        doc,
        phrase_ids,
        title=expanded_title(piece.piece_id, piece.title),
        cycle_label_text=", ".join(phrase_ids),
    )
    out = output_dir / f"{stem}.mscz"
    render.write_mscx_output(out, mscx)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Uitgevouwen formule-MSCX voor tropaar-toon-4-corpus (stap 1)."
    )
    parser.add_argument(
        "--onderzoek",
        type=Path,
        default=ONDERZOEK,
        help="Bron: onderzoeks-troparen-en-kondaken.md",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=CORPUS_DIR,
        help="Uitvoermap voor .vsa en .mscz",
    )
    parser.add_argument(
        "--id",
        dest="piece_id",
        help="Alleen dit corpus-id (bijv. T4-06)",
    )
    parser.add_argument(
        "--no-vsa",
        action="store_true",
        help="Schrijf geen .vsa-bestanden",
    )
    parser.add_argument(
        "--pad-b",
        action="store_true",
        help="Pad B: VSA-S + template A/T/B + lyrics (stap 2; default T4-06)",
    )
    args = parser.parse_args()
    output_dir = args.output_dir

    doc = render.load_resolved(TEMPLATE_YAML, LIBRARY)
    pieces = load_corpus(args.onderzoek)
    if args.piece_id:
        pieces = [p for p in pieces if p.piece_id == args.piece_id]
        if not pieces:
            raise SystemExit(f"unknown corpus id: {args.piece_id!r}")
    elif args.pad_b:
        pieces = [p for p in pieces if p.piece_id == "T4-06"]

    for piece in pieces:
        if args.pad_b:
            out = render_pad_b_piece(
                doc, piece, output_dir=output_dir, write_vsa=not args.no_vsa
            )
            n_notes = "pad B"
        else:
            out = render_piece(
                doc, piece, output_dir=output_dir, write_vsa=not args.no_vsa
            )
            n_notes = f"{piece.stanza_count} maten"
        rel = out.relative_to(REPO)
        print(f"wrote {rel} ({n_notes})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
