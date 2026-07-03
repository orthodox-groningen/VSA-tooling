"""Tests voor scripts/sync_bron_zondagen.py."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest
import yaml

_scripts_dir = Path(__file__).resolve().parent.parent / "scripts"
if str(_scripts_dir) not in sys.path:
    sys.path.insert(0, str(_scripts_dir))

from sync_bron_zondagen import sync_zangstuk


def _write_zangstuk(
    root: Path,
    zangstuk_id: str,
    tone: int,
    *,
    vsa_body: str = "[:] test {/x}.",
    coria: bool = False,
    scan_name: str = "koormap.jpg",
    scan_bytes: bytes = b"fake-jpg",
) -> None:
    zdir = root / zangstuk_id
    zdir.mkdir(parents=True)
    (zdir / "zangstuk.yaml").write_text(
        yaml.dump({"id": zangstuk_id, "toon": tone}, allow_unicode=True),
        encoding="utf-8",
    )
    if zangstuk_id.startswith("troparion-melodie-"):
        scan_dir = zdir / "sources" / "scan"
        scan_dir.mkdir(parents=True)
        (scan_dir / scan_name).write_bytes(scan_bytes)
    else:
        vsa_dir = zdir / "sources" / "vsa"
        vsa_dir.mkdir(parents=True)
        (vsa_dir / "groningen.vsa").write_text(vsa_body, encoding="utf-8")
        if coria:
            (vsa_dir / "groningen.coria.html").write_text("<html></html>", encoding="utf-8")


def test_sync_troparion_with_coria(tmp_path: Path) -> None:
    bron = tmp_path / "bron" / "zangstukken"
    out = tmp_path / "out"
    _write_zangstuk(bron, "troparion-zondag-toon-3", 3, coria=True)

    count = sync_zangstuk(bron / "troparion-zondag-toon-3", out, None, dry_run=False)

    assert count == 2
    assert (out / "tropaar-zondag-toon-3.vsa").is_file()
    assert (out / "tropaar-zondag-toon-3.coria.html").is_file()


def test_sync_melodie_toon_5(tmp_path: Path) -> None:
    bron = tmp_path / "bron" / "zangstukken"
    out = tmp_path / "out"
    _write_zangstuk(
        bron,
        "troparion-melodie-toon-5",
        5,
        scan_name="koormap-5.jpg",
    )

    count = sync_zangstuk(bron / "troparion-melodie-toon-5", out, None, dry_run=False)

    assert count == 1
    assert (out / "tropaarmelodie-toon-5.jpg").read_bytes() == b"fake-jpg"


def test_load_tone_accepts_legacy_tone_field(tmp_path: Path) -> None:
    bron = tmp_path / "bron" / "zangstukken"
    out = tmp_path / "out"
    zdir = bron / "kondak-zondag-toon-1"
    zdir.mkdir(parents=True)
    (zdir / "zangstuk.yaml").write_text(
        yaml.dump({"id": "kondak-zondag-toon-1", "tone": 1}, allow_unicode=True),
        encoding="utf-8",
    )
    vsa_dir = zdir / "sources" / "vsa"
    vsa_dir.mkdir(parents=True)
    (vsa_dir / "groningen.vsa").write_text("[:] test {/x}.", encoding="utf-8")

    count = sync_zangstuk(zdir, out, None, dry_run=False)

    assert count == 1
    assert (out / "kondak-zondag-toon-1.vsa").is_file()


def test_sync_respects_tones_filter(tmp_path: Path) -> None:
    bron = tmp_path / "bron" / "zangstukken"
    out = tmp_path / "out"
    _write_zangstuk(bron, "kondak-zondag-toon-2", 2)
    _write_zangstuk(bron, "kondak-zondag-toon-3", 3)

    sync_zangstuk(bron / "kondak-zondag-toon-2", out, {3}, dry_run=False)
    sync_zangstuk(bron / "kondak-zondag-toon-3", out, {3}, dry_run=False)

    assert not (out / "kondak-zondag-toon-2.vsa").exists()
    assert (out / "kondak-zondag-toon-3.vsa").is_file()
