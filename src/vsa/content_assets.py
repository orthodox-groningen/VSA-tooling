"""Resolve sibling source files to published asset URLs (build-time).

This module is the shared foundation for ``:::coria`` today and a future
generalised ``:::include svg|mxl|coria …`` syntax.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path

CORIA_HTML_SOURCE_SUFFIX = ".coria.html"
DEFAULT_MXL_URL_PREFIX = "/vsa/mxl"
DEFAULT_CORIA_HTML_URL_PREFIX = "/coria"


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


def published_coria_html_url_path(
    vsa_path: Path,
    content_root: Path,
    *,
    prefix: str,
) -> str:
    relative = relative_to_content_root(vsa_path, content_root)
    return _join_url_prefix(prefix, relative.with_suffix(".html"))


def coria_html_source_path(vsa_path: Path) -> Path:
    return vsa_path.with_name(vsa_path.stem + CORIA_HTML_SOURCE_SUFFIX)


def resolve_asset(
    vsa_path: Path,
    content_root: Path,
    channel: str,
    *,
    mxl_url_prefix: str = DEFAULT_MXL_URL_PREFIX,
    coria_html_url_prefix: str = DEFAULT_CORIA_HTML_URL_PREFIX,
    coria_mode: CoriaMode = CoriaMode.AUTO,
) -> ResolvedAsset:
    """Map a sibling ``.vsa`` source file to a published asset URL.

    Supported *channel* values: ``coria``, ``mxl``.
    """
    vsa_path = vsa_path.resolve()
    if vsa_path.suffix.lower() != ".vsa":
        raise ContentAssetError(f"Verwacht een .vsa-bestand, kreeg: {vsa_path.name}")

    if not vsa_path.exists():
        raise ContentAssetError(f"VSA-bestand niet gevonden: {vsa_path}")

    mxl_path = published_mxl_url_path(
        vsa_path, content_root, prefix=mxl_url_prefix
    )
    html_source = coria_html_source_path(vsa_path)
    html_path = (
        published_coria_html_url_path(
            vsa_path, content_root, prefix=coria_html_url_prefix
        )
        if html_source.exists()
        else None
    )

    if channel == "mxl":
        return ResolvedAsset("mxl", vsa_path, mxl_path, html_path)

    if channel == "coria":
        mode = coria_mode
        if mode == CoriaMode.AUTO:
            mode = CoriaMode.HTML if html_path else CoriaMode.MXL
        if mode == CoriaMode.HTML:
            if not html_path:
                raise ContentAssetError(
                    f"Geen Coria-HTML naast {vsa_path.name} "
                    f"(verwacht {html_source.name})"
                )
            return ResolvedAsset("coria", vsa_path, html_path, html_path)
        return ResolvedAsset("coria", vsa_path, mxl_path, html_path)

    raise ContentAssetError(f"Onbekend asset-kanaal: {channel!r}")


def _join_url_prefix(prefix: str, relative: Path) -> str:
    cleaned = prefix.rstrip("/")
    parts = relative.as_posix().split("/")
    return f"{cleaned}/{'/'.join(parts)}"
