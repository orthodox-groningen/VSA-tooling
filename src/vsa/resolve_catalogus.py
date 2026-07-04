"""Resolve markdown ``:::include zoek=`` naar catalogus-paden."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .yaml_frontmatter import parse_vsa_frontmatter

try:
    from catalogus import ZoekContext, zoek_met_roots
    from catalogus.errors import AmbiguousError, CatalogusError, NotFoundError

    from .catalogus_bridge import discover_bron_root
    from .include_vsa import build_zoek_context
except ImportError:  # pragma: no cover - catalogus niet geïnstalleerd
    ZoekContext = None  # type: ignore[misc, assignment]

    def discover_bron_root(content_root=None):  # type: ignore[misc]
        return None

    def build_zoek_context(frontmatter, *, bronnen=None):  # type: ignore[misc]
        return None

    def zoek_met_roots(*args, **kwargs):  # type: ignore[misc]
        raise ResolveCatalogusError(
            "catalogus-package niet beschikbaar; installeer catalogus uit bron-repo."
        )

    class NotFoundError(Exception):  # type: ignore[no-redef]
        pass

    class AmbiguousError(Exception):  # type: ignore[no-redef]
        pass

    class CatalogusError(Exception):  # type: ignore[no-redef]
        pass


INCLUDE_ZOEK_EXPORT_PATTERN = re.compile(
    r'^:::include\s+(svg|coria|mxl)\s+zoek="([^"]*)"(?:\s+(.+?))?:::$'
)


class ResolveCatalogusError(Exception):
    """Fout bij resolve-catalogus."""

    def __init__(self, message_nl: str, *, line: int | None = None) -> None:
        super().__init__(message_nl)
        self.message_nl = message_nl
        self.line = line


@dataclass(frozen=True)
class ResolveCatalogusWarning:
    code: str
    message_nl: str
    line: int


@dataclass(frozen=True)
class ResolveCatalogusResult:
    text: str
    resolved_queries: tuple[str, ...]
    warnings: tuple[ResolveCatalogusWarning, ...]


def has_unresolved_zoek_includes(text: str) -> bool:
    """Return ``True`` wanneer markdown nog open ``zoek=``-includes bevat."""
    in_code_fence = False
    fence_marker = ""

    for line in text.splitlines():
        stripped = line.strip()
        fence = _opening_or_closing_fence(stripped)
        if fence:
            if not in_code_fence:
                in_code_fence = True
                fence_marker = fence
            elif _closes_fence(stripped, fence_marker):
                in_code_fence = False
                fence_marker = ""
            continue
        if in_code_fence:
            continue
        if INCLUDE_ZOEK_EXPORT_PATTERN.match(stripped):
            return True
    return False


def resolve_catalogus_markdown(
    text: str,
    *,
    source_path: Path,
    content_root: Path | None = None,
    bron_root: Path | None = None,
) -> ResolveCatalogusResult:
    """Vervang ``:::include <exporttype> zoek="…"`` door catalogus-pad."""
    frontmatter, body = parse_vsa_frontmatter(text)
    context = build_zoek_context(frontmatter)

    resolved_root = content_root.resolve() if content_root else _discover_content_root(source_path)
    resolved_bron = bron_root
    if resolved_bron is None and resolved_root is not None:
        resolved_bron = discover_bron_root(resolved_root)

    if resolved_root is None and resolved_bron is None:
        raise ResolveCatalogusError(
            "Geen content-root of bron-root; geef --content-root en/of --bron-root op.",
        )

    cache: dict[str, str] = {}
    warnings: list[ResolveCatalogusWarning] = []
    resolved_queries: list[str] = []
    in_code_fence = False
    fence_marker = ""
    output_lines: list[str] = []

    if frontmatter:
        output_lines.extend(_frontmatter_block(frontmatter))

    for line_no, line in enumerate(body.splitlines(), start=1):
        stripped = line.strip()
        fence = _opening_or_closing_fence(stripped)
        if fence:
            if not in_code_fence:
                in_code_fence = True
                fence_marker = fence
            elif _closes_fence(stripped, fence_marker):
                in_code_fence = False
                fence_marker = ""
            output_lines.append(line)
            continue

        if in_code_fence:
            output_lines.append(line)
            continue

        match = INCLUDE_ZOEK_EXPORT_PATTERN.match(stripped)
        if match is None:
            output_lines.append(line)
            continue

        export_type = match.group(1)
        zoek_query = match.group(2).strip()
        params_str = match.group(3)
        if not zoek_query:
            raise ResolveCatalogusError("Lege zoek= waarde in include.", line=line_no)

        if zoek_query not in cache:
            try:
                result = zoek_met_roots(
                    zoek_query,
                    content_root=resolved_root,
                    bron_root=resolved_bron,
                    context=context,
                )
            except NotImplementedError as exc:
                raise ResolveCatalogusError(str(exc), line=line_no) from exc
            except (NotFoundError, AmbiguousError, ValueError) as exc:
                raise ResolveCatalogusError(str(exc), line=line_no) from exc
            except CatalogusError as exc:
                raise ResolveCatalogusError(str(exc), line=line_no) from exc

            cache[zoek_query] = result.catalogus_pad
            resolved_queries.append(zoek_query)
            if result.has_ook_in_bron:
                pads = ", ".join(result.ook_gevonden_in_bron)
                warnings.append(
                    ResolveCatalogusWarning(
                        code="CATALOGUS-ZOEK-BRON-HINT",
                        message_nl=(
                            f"Ook gevonden in bron: {pads} — controleer of "
                            f"{result.catalogus_pad} de bedoelde uitvoeringsvorm is."
                        ),
                        line=line_no,
                    )
                )

        catalogus_pad = cache[zoek_query]
        new_line = f':::include {export_type} {catalogus_pad}'
        if params_str:
            new_line += f' {params_str.strip()}'
        new_line += ':::'
        output_lines.append(new_line)

    resolved_text = "\n".join(output_lines)
    if body.endswith("\n") or not body:
        resolved_text += "\n"
    return ResolveCatalogusResult(
        text=resolved_text,
        resolved_queries=tuple(resolved_queries),
        warnings=tuple(warnings),
    )


def write_resolved_markdown(
    source_path: Path,
    *,
    content_root: Path | None = None,
    bron_root: Path | None = None,
    output_path: Path | None = None,
    dry_run: bool = False,
) -> ResolveCatalogusResult:
    """Lees markdown, resolve ``zoek=``, schrijf uitvoer."""
    text = source_path.read_text(encoding="utf-8")
    result = resolve_catalogus_markdown(
        text,
        source_path=source_path,
        content_root=content_root,
        bron_root=bron_root,
    )
    if dry_run:
        return result
    target = output_path or source_path
    target.write_text(result.text, encoding="utf-8")
    return result


def _discover_content_root(source_path: Path) -> Path | None:
    for parent in (source_path.parent, *source_path.parents):
        if (parent / "lokaal").is_dir():
            return parent.resolve()
    return None


def _frontmatter_block(frontmatter: dict) -> list[str]:
    if not frontmatter:
        return []
    import yaml

    dumped = yaml.safe_dump(
        frontmatter,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    ).rstrip("\n")
    return ["---", *dumped.splitlines(), "---", ""]


def _opening_or_closing_fence(stripped: str) -> str:
    if stripped.startswith("```"):
        return "```"
    if stripped.startswith("~~~"):
        return "~~~"
    return ""


def _closes_fence(stripped: str, fence_marker: str) -> bool:
    return stripped.startswith(fence_marker)
