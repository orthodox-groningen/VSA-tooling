"""Tests voor vsa resolve-catalogus."""

from __future__ import annotations

from pathlib import Path

import pytest

from vsa.markdown_include import IncludeError, resolve_includes
from vsa.resolve_catalogus import (
    ResolveCatalogusError,
    resolve_catalogus_markdown,
)


def test_build_rejects_unresolved_zoek(tmp_path: Path) -> None:
    content_root = tmp_path / "content-source"
    content_root.mkdir()
    md = content_root / "open-zoek.md"
    md.write_text(
        '---\ndefault:\n  gelegenheid: geboorte-moeder-gods\n---\n'
        ':::include svg zoek="Troparion" alt="T":::\n',
        encoding="utf-8",
    )
    with pytest.raises(IncludeError, match="resolve-catalogus"):
        resolve_includes(
            md.read_text(encoding="utf-8"),
            source_path=md,
            content_root=content_root,
            bron_root=tmp_path / "bron",
        )


def test_cli_exposes_resolve_catalogus_command() -> None:
    from vsa.cli import _build_parser

    parser = _build_parser()
    args = parser.parse_args(
        [
            "resolve-catalogus",
            "examples/consumer-minimal/content-source/smoke.md",
            "--dry-run",
        ]
    )
    assert args.command == "resolve-catalogus"
    assert args.dry_run is True


def test_resolve_empty_zoek_raises(tmp_path: Path) -> None:
    root = tmp_path / "content-source"
    root.mkdir()
    (root / "lokaal").mkdir()
    md = root / "bad.md"
    md.write_text(':::include svg zoek="" alt="x":::\n', encoding="utf-8")
    with pytest.raises(ResolveCatalogusError, match="Lege zoek"):
        resolve_catalogus_markdown(
            md.read_text(encoding="utf-8"),
            source_path=md,
            content_root=root,
            bron_root=tmp_path / "bron",
        )
