"""Eenmalige migratie: zondag-zangstukken van hugo-demo naar bron-repo.

Gebruik: python scripts/migrate_zondag_to_bron.py --vsa-zondagen <pad> --bron-root <pad>
"""

from __future__ import annotations

import argparse
import shutil
import textwrap
from pathlib import Path

MELODIE_SOURCE: dict[int, tuple[str, str]] = {
    1: ("tropaarmelodie-toon-1.jpg", "koormap.jpg"),
    2: ("tropaarmelodie-toon-2.jpg", "koormap.jpg"),
    3: ("tropaarmelodie-toon-3.jpg", "koormap.jpg"),
    4: ("tropaarmelodie-toon-4.jpg", "koormap.jpg"),
    5: ("tropaarmelodie-toon-5.jpg", "koormap-5.jpg"),
    6: ("tropaarmelodie-toon-6.jpg", "koormap.jpg"),
    7: ("tropaarmelodie-toon-7.jpg", "koormap.jpg"),
    8: ("tropaarmelodie-toon-8.jpg", "koormap.jpg"),
}

MELODIE_EXTRA: dict[int, tuple[str, str]] = {
    2: ("tropaarmelodie-toon-2a.jpg", "koormap-a.jpg"),
    4: ("tropaarmelodie-toon-4a.jpg", "koormap-a.jpg"),
    5: ("tropaarmelodie-toon-5.jpg", "koormap-5.jpg"),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Migreer zondag-zangstukken naar bron-repo.")
    parser.add_argument("--vsa-zondagen", type=Path, required=True)
    parser.add_argument("--bron-root", type=Path, required=True)
    return parser.parse_args()


def _write_yaml(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).lstrip(), encoding="utf-8")


def _copy(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def migrate_tone(vsa_dir: Path, bron_zangstukken: Path, tone: int) -> None:
    # Troparion
    trop_id = f"troparion-zondag-toon-{tone}"
    trop_dir = bron_zangstukken / trop_id
    _copy(vsa_dir / f"tropaar-zondag-toon-{tone}.vsa", trop_dir / "sources" / "vsa" / "groningen.vsa")
    coria = vsa_dir / f"tropaar-zondag-toon-{tone}.coria.html"
    if coria.is_file():
        _copy(coria, trop_dir / "sources" / "vsa" / "groningen.coria.html")
    _write_yaml(
        trop_dir / "zangstuk.yaml",
        f"""\
        id: {trop_id}
        title: Troparion - Zondag, toon {tone}
        occasion: Zondag (opstandingscyclus)
        occasion_type: zondag-cyclus
        tone: {tone}
        sources:
          - id: groningen
            file: sources/vsa/groningen.vsa
            author: Parochie Groningen
            reference: koormap Groningen
            copyright_status: vrij
        """,
    )

    # Kondak
    kond_id = f"kondak-zondag-toon-{tone}"
    kond_dir = bron_zangstukken / kond_id
    _copy(vsa_dir / f"kondak-zondag-toon-{tone}.vsa", kond_dir / "sources" / "vsa" / "groningen.vsa")
    _write_yaml(
        kond_dir / "zangstuk.yaml",
        f"""\
        id: {kond_id}
        title: Kondak - Zondag, toon {tone}
        occasion: Zondag (opstandingscyclus)
        occasion_type: zondag-cyclus
        tone: {tone}
        sources:
          - id: groningen
            file: sources/vsa/groningen.vsa
            author: Parochie Groningen
            reference: koormap Groningen
            copyright_status: vrij
        """,
    )

    # Melodie
    mel_id = f"troparion-melodie-toon-{tone}"
    mel_dir = bron_zangstukken / mel_id
    src_name, dst_name = MELODIE_SOURCE[tone]
    _copy(vsa_dir / src_name, mel_dir / "sources" / "scan" / dst_name)

    extra_sources = ""
    if tone in MELODIE_EXTRA:
        extra_src, extra_dst = MELODIE_EXTRA[tone]
        if (vsa_dir / extra_src).is_file():
            _copy(vsa_dir / extra_src, mel_dir / "sources" / "scan" / extra_dst)
            extra_sources = f"""
          - id: koormap-scan-alt
            file: sources/scan/{extra_dst}
            reference: koormap Groningen
            copyright_status: vrij"""

    primary_id = "koormap-scan"
    _write_yaml(
        mel_dir / "zangstuk.yaml",
        f"""\
        id: {mel_id}
        title: Troparion-melodie - Zondag, toon {tone}
        occasion: Zondag (opstandingscyclus)
        occasion_type: zondag-cyclus
        tone: {tone}
        sources:
          - id: {primary_id}
            file: sources/scan/{dst_name}
            reference: koormap Groningen
            copyright_status: vrij{extra_sources}
        """,
    )

    print(f"  toon {tone}: {trop_id}, {kond_id}, {mel_id}")


def main() -> int:
    args = parse_args()
    vsa_dir = args.vsa_zondagen.resolve()
    bron_zangstukken = (args.bron_root / "zangstukken").resolve()
    bron_zangstukken.mkdir(parents=True, exist_ok=True)

    print(f"Migreren van {vsa_dir} naar {bron_zangstukken}")
    for tone in range(1, 9):
        migrate_tone(vsa_dir, bron_zangstukken, tone)
    print("Klaar: 24 zangstuk-mappen.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
