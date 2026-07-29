"""Tests voor vsa resolve-catalogus."""

from __future__ import annotations

from pathlib import Path

import pytest

from vsa.markdown_include import IncludeError, resolve_includes
from vsa.resolve_catalogus import (
    ResolveCatalogusError,
    resolve_catalogus_markdown,
    write_resolved_markdown,
)

REPO_ROOT = Path(__file__).resolve().parents[1]
BRON_ROOT = REPO_ROOT.parent / "bron"
HUGO_CONTENT = REPO_ROOT / "examples" / "hugo-demo" / "content-source"
SESSION = HUGO_CONTENT / "praktijk" / "samenstellingen" / "geboorte-moeder-gods-2026.md"


@pytest.mark.skipif(not BRON_ROOT.is_dir(), reason="bron sibling checkout ontbreekt")
@pytest.mark.skipif(not HUGO_CONTENT.is_dir(), reason="hugo-demo content-source ontbreekt")
def test_resolve_geboorte_moeder_gods_session() -> None:
    source = SESSION.read_text(encoding="utf-8")
    result = resolve_catalogus_markdown(
        source,
        source_path=SESSION,
        content_root=HUGO_CONTENT,
        bron_root=BRON_ROOT,
    )
    assert 'zoek="' not in result.text
    assert (
        "bron:troparion-geboorte-moeder-gods/troparion-geboorte-moeder-gods/liturgikon"
        in result.text
    )
    assert (
        "bron:kondak-geboorte-moeder-gods/kondak-geboorte-moeder-gods/liturgikon"
        in result.text
    )
    assert (
        "lokaal:cherubijnenhymne/kastorski/groningen/groningen-vsa"
        in result.text
    )
    assert "Troparion" in result.resolved_queries
    assert "Kondakion" in result.resolved_queries


def test_build_rejects_unresolved_zoek(tmp_path: Path) -> None:
    md = tmp_path / "open-zoek.md"
    md.write_text(
        '---\ndefault:\n  gelegenheid: geboorte-moeder-gods\n---\n'
        ':::include svg zoek="Troparion" alt="T":::\n',
        encoding="utf-8",
    )
    with pytest.raises(IncludeError, match="resolve-catalogus"):
        resolve_includes(
            md.read_text(encoding="utf-8"),
            source_path=md,
            content_root=HUGO_CONTENT,
            bron_root=BRON_ROOT,
        )


@pytest.mark.skipif(not BRON_ROOT.is_dir(), reason="bron sibling checkout ontbreekt")
@pytest.mark.skipif(not HUGO_CONTENT.is_dir(), reason="hugo-demo content-source ontbreekt")
def test_write_resolved_markdown_to_output(tmp_path: Path) -> None:
    source = tmp_path / "sessie.md"
    source.write_text(SESSION.read_text(encoding="utf-8"), encoding="utf-8")
    output = tmp_path / "sessie-resolved.md"
    write_resolved_markdown(
        source,
        content_root=HUGO_CONTENT,
        bron_root=BRON_ROOT,
        output_path=output,
    )
    resolved = output.read_text(encoding="utf-8")
    assert 'zoek="' not in resolved
    assert output.exists()


@pytest.mark.skipif(not BRON_ROOT.is_dir(), reason="bron sibling checkout ontbreekt")
def test_build_markdown_resolves_zoek_before_includes(tmp_path: Path) -> None:
    import shutil

    from vsa.markdown_builder import build_markdown_site

    input_dir = tmp_path / "content-source"
    shutil.copytree(HUGO_CONTENT / "lokaal", input_dir / "lokaal")
    page = input_dir / "praktijk" / "demo.md"
    page.parent.mkdir(parents=True)
    page.write_text(
        '---\ndefault:\n  gelegenheid: geboorte-moeder-gods\n---\n'
        ':::include svg zoek="Cherubijnenhymne (Kastorski)" alt="Cherubijn":::\n',
        encoding="utf-8",
    )

    output_dir = tmp_path / "generated"
    assets_dir = tmp_path / "static" / "vsa"
    build_markdown_site(input_dir, output_dir, assets_dir)

    built = (output_dir / "praktijk" / "demo.md").read_text(encoding="utf-8")
    assert 'zoek="' not in built
    assert '<img class="vsa-notation"' in built


def test_cli_exposes_resolve_catalogus_command() -> None:
    from vsa.cli import _build_parser

    parser = _build_parser()
    args = parser.parse_args(
        [
            "resolve-catalogus",
            "examples/hugo-demo/content-source/praktijk/samenstellingen/geboorte-moeder-gods-2026.md",
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
        )
