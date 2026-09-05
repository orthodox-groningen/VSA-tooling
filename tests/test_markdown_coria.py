"""Tests for :::coria directives and content asset resolution."""

from pathlib import Path

import pytest

from vsa.content_assets import resolve_asset
from vsa.markdown_builder import build_markdown_site
from vsa.markdown_coria import CoriaDirectiveError, resolve_coria_directives


def test_resolve_asset_mxl_path(tmp_path: Path):
    content = tmp_path / "content"
    piece = content / "praktijk" / "melodie.vsa"
    piece.parent.mkdir(parents=True)
    piece.write_text("{/a_}", encoding="utf-8")

    asset = resolve_asset(piece, content, "mxl")
    assert asset.public_url_path == "/vsa/mxl/praktijk/melodie.mxl"


def test_resolve_asset_coria_prefers_html_sibling(tmp_path: Path):
    content = tmp_path / "content"
    piece = content / "melodie.vsa"
    piece.parent.mkdir(parents=True)
    piece.write_text("{/a_}", encoding="utf-8")
    piece.with_name("melodie.coria.html").write_text("<html></html>", encoding="utf-8")

    asset = resolve_asset(piece, content, "coria")
    assert asset.public_url_path == "/coria/melodie.html"


def test_resolve_coria_directive_emits_html_shortcode(tmp_path: Path):
    content = tmp_path / "content"
    md_dir = content / "praktijk"
    md_dir.mkdir(parents=True)
    vsa = md_dir / "melodie.vsa"
    vsa.write_text("{/a_}", encoding="utf-8")
    vsa.with_name("melodie.coria.html").write_text("<html></html>", encoding="utf-8")
    md = md_dir / "page.md"
    md.write_text(':::coria "melodie.vsa" label="Oefenen":::\n', encoding="utf-8")

    result = resolve_coria_directives(
        md.read_text(encoding="utf-8"),
        md,
        content_root=content,
    )

    assert 'coria-html src="/coria/praktijk/melodie.html"' in result
    assert 'label="Oefenen"' in result
    assert ":::coria" not in result


def test_resolve_coria_directive_falls_back_to_mxl(tmp_path: Path):
    content = tmp_path / "content"
    md_dir = content / "praktijk"
    md_dir.mkdir(parents=True)
    vsa = md_dir / "melodie.vsa"
    vsa.write_text("{/a_}", encoding="utf-8")
    md = md_dir / "page.md"
    md.write_text(':::coria "melodie.vsa":::\n', encoding="utf-8")

    result = resolve_coria_directives(
        md.read_text(encoding="utf-8"),
        md,
        content_root=content,
    )

    assert 'coria src="/vsa/mxl/praktijk/melodie.mxl"' in result
    assert "coria-html" not in result


def test_resolve_coria_missing_vsa_raises(tmp_path: Path):
    content = tmp_path / "content"
    md = content / "page.md"
    content.mkdir()
    md.write_text(':::coria "ontbreekt.vsa":::\n', encoding="utf-8")

    with pytest.raises(CoriaDirectiveError, match="niet gevonden"):
        resolve_coria_directives(
            md.read_text(encoding="utf-8"),
            md,
            content_root=content,
        )


def test_build_markdown_copies_coria_html(tmp_path: Path):
    input_dir = tmp_path / "in"
    output_dir = tmp_path / "out"
    assets_dir = tmp_path / "static" / "vsa"
    coria_dir = tmp_path / "static" / "coria"
    piece_dir = input_dir / "praktijk"
    piece_dir.mkdir(parents=True)
    (piece_dir / "melodie.vsa").write_text("{/a_}", encoding="utf-8")
    (piece_dir / "melodie.coria.html").write_text("<html></html>", encoding="utf-8")
    (input_dir / "page.md").write_text(
        '::: vsa-notatie\n{/a_}\n:::\n:::coria "praktijk/melodie.vsa":::\n',
        encoding="utf-8",
    )

    build_markdown_site(
        input_dir,
        output_dir,
        assets_dir,
        coria_assets_dir=coria_dir,
    )

    assert (coria_dir / "praktijk" / "melodie.html").exists()
    generated = (output_dir / "page.md").read_text(encoding="utf-8")
    assert "coria-html" in generated


def test_resolve_asset_native_mxl_path(tmp_path: Path):
    content = tmp_path / "content"
    piece = content / "praktijk" / "corpus" / "nicolaas.mxl"
    piece.parent.mkdir(parents=True)
    piece.write_bytes(b"PK\x03\x04")

    asset = resolve_asset(piece, content, "mxl")
    assert asset.public_url_path == "/mxl/praktijk/corpus/nicolaas.mxl"


def test_resolve_coria_directive_native_mxl(tmp_path: Path):
    content = tmp_path / "content"
    md_dir = content / "praktijk"
    md_dir.mkdir(parents=True)
    (md_dir / "melodie.mxl").write_bytes(b"PK\x03\x04")
    md = md_dir / "page.md"
    md.write_text(':::coria "melodie.mxl" label="Oefenen":::\n', encoding="utf-8")

    result = resolve_coria_directives(
        md.read_text(encoding="utf-8"),
        md,
        content_root=content,
    )

    assert 'coria src="/mxl/praktijk/melodie.mxl"' in result
    assert ":::coria" not in result


def test_build_markdown_copies_native_mxl(tmp_path: Path):
    input_dir = tmp_path / "in"
    output_dir = tmp_path / "out"
    assets_dir = tmp_path / "static" / "vsa"
    mxl_dir = tmp_path / "static" / "mxl"
    piece_dir = input_dir / "praktijk"
    piece_dir.mkdir(parents=True)
    (piece_dir / "melodie.mxl").write_bytes(b"PK\x03\x04")
    (piece_dir / "score.musicxml").write_text("<score-partwise/>", encoding="utf-8")
    (input_dir / "page.md").write_text(
        ':::include coria "praktijk/melodie.mxl":::\n'
        ':::include mxl "praktijk/score.musicxml":::\n',
        encoding="utf-8",
    )

    result = build_markdown_site(
        input_dir,
        output_dir,
        assets_dir,
        native_mxl_assets_dir=mxl_dir,
    )

    assert (mxl_dir / "praktijk" / "melodie.mxl").exists()
    assert (mxl_dir / "praktijk" / "score.musicxml").exists()
    generated = (output_dir / "page.md").read_text(encoding="utf-8")
    assert 'coria src="/mxl/praktijk/melodie.mxl"' in generated
    assert 'mxl-download src="/mxl/praktijk/score.musicxml"' in generated
    assert any(path.endswith("melodie.mxl") for path in result.static_files)
