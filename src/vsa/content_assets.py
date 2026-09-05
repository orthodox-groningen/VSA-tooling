"""Resolve sibling source files to published asset URLs (build-time).

This module is the shared foundation for ``:::include svg|mxl|coria`` and
``:::coria``. Exporttypes ``coria`` and ``mxl`` accept a ``.vsa`` authoring
anchor (derived MXL under ``/vsa/mxl/``) or a native ``.mxl`` / ``.musicxml``
file (published under ``/mxl/``).
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path

CORIA_HTML_SOURCE_SUFFIX = ".coria.html"
DEFAULT_MXL_URL_PREFIX = "/vsa/mxl"
DEFAULT_NATIVE_MXL_URL_PREFIX = "/mxl"
DEFAULT_CORIA_HTML_URL_PREFIX = "/coria"
NATIVE_MUSICXML_SUFFIXES = frozenset({".mxl", ".musicxml"})
CORIA_MXL_SOURCE_SUFFIXES = frozenset({".vsa"}) | NATIVE_MUSICXML_SUFFIXES


class CoriaMode(str, Enum):
    AUTO = "auto"
    HTML = "html"
    MXL = "mxl"


class ContentAssetError(Exception):
    pass


@dataclass(frozen=True)
class ResolvedAsset:
    channel: str
    source_path: Path
    public_url_path: str
    coria_html_path: str | None = None


def relative_to_content_root(source: Path, content_root: Path) -> Path:
    try:
        return source.resolve().relative_to(content_root.resolve())
    except ValueError as exc:
        raise ContentAssetError(
            f"Bestand ligt buiten content-root: {source} (root: {content_root})"
        ) from exc


def published_mxl_url_path(vsa_path: Path, content_root: Path, *, prefix: str) -> str:
    relative = relative_to_content_root(vsa_path, content_root)
    return _join_url_prefix(prefix, relative.with_suffix(".mxl"))


def published_native_musicxml_url_path(
    source_path: Path,
    content_root: Path,
    *,
    prefix: str,
) -> str:
    relative = relative_to_content_root(source_path, content_root)
    return _join_url_prefix(prefix, relative)


def published_coria_html_url_path(
    source_path: Path,
    content_root: Path,
    *,
    prefix: str,
) -> str:
    relative = relative_to_content_root(source_path, content_root)
    return _join_url_prefix(prefix, relative.with_suffix(".html"))


def coria_html_source_path(source_path: Path) -> Path:
    return source_path.with_name(source_path.stem + CORIA_HTML_SOURCE_SUFFIX)


def resolve_asset(
    source_path: Path,
    content_root: Path,
    channel: str,
    *,
    mxl_url_prefix: str = DEFAULT_MXL_URL_PREFIX,
    native_mxl_url_prefix: str = DEFAULT_NATIVE_MXL_URL_PREFIX,
    coria_html_url_prefix: str = DEFAULT_CORIA_HTML_URL_PREFIX,
    coria_mode: CoriaMode = CoriaMode.AUTO,
) -> ResolvedAsset:
    """Map a ``.vsa`` or native MusicXML file to a published asset URL.

    Supported *channel* values: ``coria``, ``mxl``.
    """
    source_path = source_path.resolve()
    suffix = source_path.suffix.lower()

    if suffix == ".vsa":
        playback_url = published_mxl_url_path(
            source_path, content_root, prefix=mxl_url_prefix
        )
        missing = f"VSA-bestand niet gevonden: {source_path}"
    elif suffix in NATIVE_MUSICXML_SUFFIXES:
        playback_url = published_native_musicxml_url_path(
            source_path, content_root, prefix=native_mxl_url_prefix
        )
        missing = f"MusicXML-bestand niet gevonden: {source_path}"
    else:
        raise ContentAssetError(
            f"Verwacht een .vsa-, .mxl- of .musicxml-bestand, kreeg: {source_path.name}"
        )

    if not source_path.exists():
        raise ContentAssetError(missing)

    html_source = coria_html_source_path(source_path)
    html_path = (
        published_coria_html_url_path(
            source_path, content_root, prefix=coria_html_url_prefix
        )
        if html_source.exists()
        else None
    )

    if channel == "mxl":
        return ResolvedAsset("mxl", source_path, playback_url, html_path)

    if channel == "coria":
        return _resolve_coria_channel(
            source_path,
            playback_url,
            html_path,
            html_source,
            coria_mode,
        )

    raise ContentAssetError(f"Onbekend asset-kanaal: {channel!r}")


def _resolve_coria_channel(
    source_path: Path,
    playback_url: str,
    html_path: str | None,
    html_source: Path,
    coria_mode: CoriaMode,
) -> ResolvedAsset:
    mode = coria_mode
    if mode == CoriaMode.AUTO:
        mode = CoriaMode.HTML if html_path else CoriaMode.MXL
    if mode == CoriaMode.HTML:
        if not html_path:
            raise ContentAssetError(
                f"Geen Coria-HTML naast {source_path.name} "
                f"(verwacht {html_source.name})"
            )
        return ResolvedAsset("coria", source_path, html_path, html_path)
    return ResolvedAsset("coria", source_path, playback_url, html_path)


def _join_url_prefix(prefix: str, relative: Path) -> str:
    cleaned = prefix.rstrip("/")
    parts = relative.as_posix().split("/")
    return f"{cleaned}/{'/'.join(parts)}"
