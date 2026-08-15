"""Genereer tropaar-toon-4-corpus: VSA → MSCZ/MXL/(PDF); of alleen template-formule."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
LIBRARY = REPO / "docs" / "specification-vsa-templates" / "library"
TEMPLATE_DIR = LIBRARY / "tropaar-toon-4"
TEMPLATE_YAML = TEMPLATE_DIR / "template.yaml"
ONDERZOEK = REPO / "docs" / "plans" / "onderzoeks-troparen-en-kondaken.md"
CORPUS_DIR = TEMPLATE_DIR / "examples" / "corpus"

MUSESCORE_CANDIDATES = (
    Path(r"C:\Program Files\MuseScore 4\bin\MuseScore4.exe"),
    Path(r"C:\Program Files\MuseScore 3\bin\MuseScore3.exe"),
)

sys.path.insert(0, str(REPO / "src"))
sys.path.insert(0, str(REPO / "scripts"))

import render_vsa_template_musicxml as render  # noqa: E402

from vsa.corpus_vsa import load_corpus, write_vsa_file  # noqa: E402
from vsa.template_instance import map_vsa_to_template  # noqa: E402


def find_musescore() -> Path | None:
    which = shutil.which("MuseScore4") or shutil.which("mscore")
    if which:
        return Path(which)
    for path in MUSESCORE_CANDIDATES:
        if path.is_file():
            return path
    return None


def export_pdf(mscz: Path, *, musescore: Path) -> Path:
    """MuseScore CLI: mscz → pdf naast het bronbestand."""
    pdf = mscz.with_suffix(".pdf")
    subprocess.run(
        [str(musescore), "-f", "-o", str(pdf), str(mscz)],
        check=True,
    )
    if not pdf.is_file():
        raise RuntimeError(f"MuseScore did not write {pdf}")
    return pdf


def expanded_title(piece_id: str, title: str) -> str:
    return f"{piece_id} — {title}"


def render_instance(
    doc: dict,
    piece,
    *,
    output_dir: Path,
    write_vsa: bool,
    musescore: Path | None = None,
) -> Path:
    """Uitgewerkt zangstuk: S=VSA, A/T/B=template → .vsa/.mscz/.mxl/[.pdf]."""
    stem = piece.filename_stem()
    vsa_path = output_dir / f"{stem}.vsa"
    if write_vsa or not vsa_path.exists():
        write_vsa_file(piece, vsa_path)
    vsa_text = vsa_path.read_text(encoding="utf-8")

    mapped = map_vsa_to_template(doc, vsa_text)
    title = expanded_title(piece.piece_id, piece.title)
    mscx = render.render_instance_mscx(doc, mapped, title=title)
    out = output_dir / f"{stem}.mscz"
    render.write_mscx_output(out, mscx)

    from vsa.musicxml_package import write_musicxml_output

    xml = render.render_instance_musicxml(doc, mapped, title=title)
    write_musicxml_output(output_dir / f"{stem}.mxl", xml)

    if musescore is not None:
        pdf = export_pdf(out, musescore=musescore)
        print(f"wrote {pdf.relative_to(REPO)}")

    if piece.piece_id == "T4-06":
        examples = TEMPLATE_DIR / "examples"
        render.write_mscx_output(examples / "elia.mscz", mscx)
        write_musicxml_output(examples / "elia.mxl", xml)
        print(f"wrote {(examples / 'elia.mscz').relative_to(REPO)}")
        print(f"wrote {(examples / 'elia.mxl').relative_to(REPO)}")
        if musescore is not None:
            elia_pdf = export_pdf(examples / "elia.mscz", musescore=musescore)
            print(f"wrote {elia_pdf.relative_to(REPO)}")
    return out


def render_template_mscz(doc: dict, *, musescore: Path | None = None) -> Path:
    """Formuleblad → template.mscz (+ optioneel PDF)."""
    mscx = render.render_template_mscx(doc)
    out = TEMPLATE_DIR / "template.mscz"
    render.write_mscx_output(out, mscx)
    # Historische alias (oude naam).
    render.write_mscx_output(TEMPLATE_DIR / "template-from-yaml.mscz", mscx)
    if musescore is not None:
        pdf = export_pdf(out, musescore=musescore)
        print(f"wrote {pdf.relative_to(REPO)}")
    return out


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Tropaar-toon-4: uitgewerkte corpusstukken (.vsa/.mscz/.mxl) "
            "of template-formule (.mscz)."
        )
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
        help="Uitvoermap voor corpus (.vsa/.mscz/.mxl)",
    )
    parser.add_argument(
        "--id",
        dest="piece_id",
        help="Alleen dit corpus-id (bijv. T4-06)",
    )
    parser.add_argument(
        "--no-vsa",
        action="store_true",
        help="Schrijf geen .vsa (gebruik bestaande)",
    )
    parser.add_argument(
        "--template",
        action="store_true",
        help="Alleen formuleblad: template.mscz (geen corpus)",
    )
    parser.add_argument(
        "--pdf",
        action="store_true",
        help="Exporteer .mscz → .pdf via MuseScore CLI",
    )
    parser.add_argument(
        "--pdf-only",
        action="store_true",
        help="Alleen bestaande corpus-.mscz naar .pdf (geen re-render)",
    )
    args = parser.parse_args()
    output_dir = args.output_dir

    musescore: Path | None = None
    if args.pdf or args.pdf_only:
        musescore = find_musescore()
        if musescore is None:
            raise SystemExit(
                "MuseScore niet gevonden (verwacht o.a. "
                r"C:\Program Files\MuseScore 4\bin\MuseScore4.exe)"
            )
        print(f"using {musescore}")

    if args.pdf_only:
        paths = sorted(output_dir.glob("T4-*.mscz"))
        elia = TEMPLATE_DIR / "examples" / "elia.mscz"
        if elia.is_file() and elia not in paths:
            paths.append(elia)
        if not paths:
            raise SystemExit(f"geen T4-*.mscz in {output_dir}")
        assert musescore is not None
        for mscz in paths:
            pdf = export_pdf(mscz, musescore=musescore)
            print(f"wrote {pdf.relative_to(REPO)}")
        return 0

    doc = render.load_resolved(TEMPLATE_YAML, LIBRARY)

    if args.template:
        out = render_template_mscz(doc, musescore=musescore)
        print(f"wrote {out.relative_to(REPO)} (template)")
        return 0

    pieces = load_corpus(args.onderzoek)
    if args.piece_id:
        pieces = [p for p in pieces if p.piece_id == args.piece_id]
        if not pieces:
            raise SystemExit(f"unknown corpus id: {args.piece_id!r}")

    failures: list[str] = []
    for piece in pieces:
        try:
            out = render_instance(
                doc,
                piece,
                output_dir=output_dir,
                write_vsa=not args.no_vsa,
                musescore=musescore,
            )
            print(f"wrote {out.relative_to(REPO)}")
        except Exception as exc:  # noqa: BLE001
            msg = f"{piece.piece_id}: {exc}"
            failures.append(msg)
            print(f"FAILED {msg}", file=sys.stderr)

    if failures:
        print(f"{len(failures)} failed:", file=sys.stderr)
        for msg in failures:
            print(f"  {msg}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
