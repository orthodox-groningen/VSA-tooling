"""Resolve ``:::coria`` directives at build-markdown time."""

from __future__ import annotations

import re
from pathlib import Path

from .content_assets import (
    ContentAssetError,
    CoriaMode,
    DEFAULT_CORIA_HTML_URL_PREFIX,
    DEFAULT_MXL_URL_PREFIX,
    DEFAULT_NATIVE_MXL_URL_PREFIX,
    resolve_asset,
)

CORIA_PATTERN = re.compile(
    r'^:::coria\s+(?:"([^"]+)"|(\S+))(?:\s+(.+?))?:::$'
)
_LABEL_ATTR = re.compile(r'label="([^"]*)"')
_MODE_ATTR = re.compile(r'mode="([^"]*)"')


class CoriaDirectiveError(Exception):
    pass


def resolve_coria_directives(
    text: str,
    source_path: Path,
    *,
    content_root: Path,
    mxl_url_prefix: str = DEFAULT_MXL_URL_PREFIX,
    native_mxl_url_prefix: str = DEFAULT_NATIVE_MXL_URL_PREFIX,
    coria_html_url_prefix: str = DEFAULT_CORIA_HTML_URL_PREFIX,
) -> str:
    """Replace ``:::coria "melodie.vsa|mxl|musicxml" …:::`` with Hugo shortcodes."""
    lines = text.splitlines()
    result_lines: list[str] = []
    in_code_fence = False
    fence_marker = ""

    for line in lines:
        stripped = line.strip()

        fence = _opening_or_closing_fence(stripped)
        if fence:
            if not in_code_fence:
                in_code_fence = True
                fence_marker = fence
            elif _closes_fence(stripped, fence_marker):
                in_code_fence = False
                fence_marker = ""
            result_lines.append(line)
            continue

        if in_code_fence:
            result_lines.append(line)
            continue

        match = CORIA_PATTERN.match(stripped)
        if not match:
            result_lines.append(line)
            continue

        rel_path = (match.group(1) or match.group(2)).strip()
        params = match.group(3)
        vsa_path = (source_path.parent / rel_path).resolve()

        try:
            asset = resolve_asset(
                vsa_path,
                content_root,
                "coria",
                mxl_url_prefix=mxl_url_prefix,
                native_mxl_url_prefix=native_mxl_url_prefix,
                coria_html_url_prefix=coria_html_url_prefix,
                coria_mode=_parse_mode(params),
            )
        except ContentAssetError as exc:
            raise CoriaDirectiveError(
                f"{source_path}: {exc} (directive: {stripped})"
            ) from exc

        label = _parse_label(params) or "Oefenen in Coria"
        result_lines.append(_coria_shortcode(asset.public_url_path, label))

    return "\n".join(result_lines) + "\n"


DEFAULT_MXL_DOWNLOAD_LABEL = "Download MusicXML"


def emit_coria_shortcode(public_path: str, label: str) -> str:
    """Hugo shortcode for Coria HTML or MXL deep-link."""
    if public_path.startswith(f"{DEFAULT_CORIA_HTML_URL_PREFIX}/"):
        tag = "coria-html"
    else:
        tag = "coria"
    return f'{{{{< {tag} src="{public_path}" label="{label}" >}}}}'


def emit_mxl_download_shortcode(public_path: str, label: str) -> str:
    return f'{{{{< mxl-download src="{public_path}" label="{label}" >}}}}'


def _coria_shortcode(public_path: str, label: str) -> str:
    return emit_coria_shortcode(public_path, label)


def parse_coria_label(params: str | None) -> str | None:
    if not params:
        return None
    match = _LABEL_ATTR.search(params)
    return match.group(1) if match else None


def parse_coria_mode(params: str | None) -> CoriaMode:
    if not params:
        return CoriaMode.AUTO
    match = _MODE_ATTR.search(params)
    if not match:
        return CoriaMode.AUTO
    value = match.group(1).strip().lower()
    try:
        return CoriaMode(value)
    except ValueError as exc:
        raise CoriaDirectiveError(f"Onbekende coria mode: {value!r}") from exc


def _parse_label(params: str | None) -> str | None:
    return parse_coria_label(params)


def _parse_mode(params: str | None) -> CoriaMode:
    return parse_coria_mode(params)


def _opening_or_closing_fence(stripped: str) -> str:
    if stripped.startswith("```"):
        return "```"
    if stripped.startswith("~~~"):
        return "~~~"
    return ""


def _closes_fence(stripped: str, fence_marker: str) -> bool:
    return stripped.startswith(fence_marker)
