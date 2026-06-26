import re
import shutil
from pathlib import Path

# Path is either a quoted string (allowing spaces) or an unquoted token.
# Optional parameters follow, separated by whitespace.
INCLUDE_PATTERN = re.compile(
    r'^:::include\s+(?:"([^"]+)"|(\S+))(?:\s+(.+?))?:::$'
)

_ALT_ATTR = re.compile(r'alt="([^"]*)"')
_SCALE_ATTR = re.compile(r'scale="([^"]*)"')

_RASTER_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp", ".gif"}


class IncludeError(Exception):
    pass


def resolve_includes(
    text: str,
    source_path: Path,
    include_stack: list[Path] | None = None,
    svg_assets_dir: Path | None = None,
    svg_assets_url_prefix: str = "/vsa",
    content_root: Path | None = None,
) -> str:
    """Resolve :::include path [alt="..."]::: directives recursively.

    Supported extensions and their treatment:
      .md / .markdown  — recursive transclusion
      .vsa             — wrapped as ::: vsa-notatie ::: block; alt becomes
                         block metadata so the rendered img uses it
      .svg             — copied to svg_assets_dir (absolute URL) or kept
                         relative (fallback when svg_assets_dir is None)
      .jpg/.jpeg/.png/.webp/.gif
                       — same as .svg: copied to svg_assets_dir when provided

    The optional alt="..." parameter sets the alt text of the emitted <img>.
    For .vsa files it is injected as '# alt: ...' metadata inside the block.

    content_root is used to derive collision-free filenames for asset copies.
    Detects circular references via include_stack.
    Code fences are respected.
    """
    if include_stack is None:
        include_stack = [source_path.resolve()]

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

        match = INCLUDE_PATTERN.match(stripped)
        if not match:
            result_lines.append(line)
            continue

        rel_path = (match.group(1) or match.group(2)).strip()
        params_str = match.group(3)
        included_path = (source_path.parent / rel_path).resolve()

        if included_path in include_stack:
            chain = " → ".join(str(p) for p in include_stack) + f" → {included_path}"
            raise IncludeError(f"Kringverwijzing gedetecteerd: {chain}")

        if not included_path.exists():
            raise IncludeError(
                f"Bestand niet gevonden: '{rel_path}' (vanuit {source_path})"
            )

        suffix = included_path.suffix.lower()
        supported = {".md", ".markdown", ".vsa", ".svg"} | _RASTER_SUFFIXES

        if suffix not in supported:
            raise IncludeError(
                f"Onbekend bestandstype '{suffix}' voor include:"
                f" '{rel_path}' (vanuit {source_path})"
            )

        alt = _parse_alt(params_str)
        scale = _parse_scale(params_str)

        if suffix in (".md", ".markdown"):
            raw = included_path.read_text(encoding="utf-8")
            expanded = resolve_includes(
                raw,
                source_path=included_path,
                include_stack=include_stack + [included_path],
                svg_assets_dir=svg_assets_dir,
                svg_assets_url_prefix=svg_assets_url_prefix,
                content_root=content_root,
            )
            result_lines.extend(expanded.splitlines())

        elif suffix == ".vsa":
            raw = included_path.read_text(encoding="utf-8")
            result_lines.append("::: vsa-notatie")
            if alt:
                result_lines.append(f"# alt: {alt}")
            if scale:
                result_lines.append(f"# scale: {scale}")
            result_lines.extend(raw.splitlines())
            result_lines.append(":::")

        elif suffix in {".svg"} | _RASTER_SUFFIXES:
            alt_attr = f' alt="{alt}"' if alt is not None else ' alt=""'
            if suffix == ".svg":
                svg_text = included_path.read_text(encoding="utf-8")
                style_attr = _scale_style(scale, _svg_natural_width(svg_text))
            else:
                # Raster images: percentage width (no built-in size reading)
                style_attr = f' style="width: {scale}"' if scale else ""
            if svg_assets_dir is not None:
                asset_name = _svg_asset_name(included_path, content_root)
                dest = svg_assets_dir / asset_name
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(included_path, dest)
                url = f"{svg_assets_url_prefix.rstrip('/')}/{asset_name}"
            else:
                url = rel_path
            result_lines.append(
                f'<img src="{url}" class="vsa-notation"{alt_attr}{style_attr} />'
            )

    return "\n".join(result_lines) + "\n"


def _parse_alt(params_str: str | None) -> str | None:
    if not params_str:
        return None
    m = _ALT_ATTR.search(params_str)
    return m.group(1) if m else None


def _parse_scale(params_str: str | None) -> str | None:
    if not params_str:
        return None
    m = _SCALE_ATTR.search(params_str)
    return m.group(1) if m else None


def _svg_asset_name(asset_path: Path, content_root: Path | None) -> str:
    """Derive a flat, collision-free filename for a copied asset."""
    if content_root is not None:
        try:
            relative = asset_path.relative_to(content_root)
            stem = "-".join(relative.with_suffix("").parts)
            return _safe_name(stem) + asset_path.suffix.lower()
        except ValueError:
            pass
    return _safe_name(asset_path.stem) + asset_path.suffix.lower()


def _safe_name(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9_-]+", "-", value)
    value = value.strip("-")
    return value or "asset"


def _opening_or_closing_fence(stripped: str) -> str:
    if stripped.startswith("```"):
        return "```"
    if stripped.startswith("~~~"):
        return "~~~"
    return ""


def _closes_fence(stripped: str, fence_marker: str) -> bool:
    return stripped.startswith(fence_marker)


_SVG_WIDTH_RE = re.compile(r"<svg\b[^>]*\bwidth=\"(\d+(?:\.\d+)?)\"")


def _svg_natural_width(svg_text: str) -> float | None:
    """Extract the natural pixel width from an SVG string."""
    m = _SVG_WIDTH_RE.search(svg_text)
    return float(m.group(1)) if m else None


def _scale_style(scale: str | None, natural_width: float | None) -> str:
    """Return an inline style attribute for the given scale, or empty string.

    Uses absolute pixels (natural_width × scale%) so that the visual font size
    stays consistent regardless of SVG content width. Falls back to percentage
    when natural_width is unavailable.
    """
    if not scale:
        return ""
    if natural_width is not None:
        try:
            pct = float(scale.rstrip("%"))
            px = round(natural_width * pct / 100)
            return f' style="width: {px}px"'
        except ValueError:
            pass
    return f' style="width: {scale}"'
