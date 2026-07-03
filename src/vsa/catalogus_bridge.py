"""Catalogus-index voor VSA markdown-includes (fase 3)."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from catalogus import AliasIndex
from catalogus.include_ref import is_logical_reference


def discover_bron_root(content_root: Path | None = None) -> Path | None:
    """Zoek bron-repository (zangstukken/) voor id:-includes."""
    vsa_root = Path(__file__).resolve().parents[2]
    candidates = [
        vsa_root / "vendor" / "bron",
        vsa_root.parent / "bron",
    ]
    if content_root is not None:
        candidates.insert(0, content_root / "vendor" / "bron")
    for candidate in candidates:
        if (candidate / "zangstukken").is_dir():
            return candidate.resolve()
    return None


@lru_cache(maxsize=8)
def get_alias_index(
    content_root: str,
    bron_root: str | None,
) -> AliasIndex:
    return AliasIndex.build(
        content_root=Path(content_root),
        bron_root=Path(bron_root) if bron_root else None,
    )


def resolve_logical_vsa_path(
    reference: str,
    *,
    content_root: Path,
    bron_root: Path | None = None,
) -> Path:
    if not is_logical_reference(reference):
        raise ValueError(f"Geen logische referentie: {reference!r}")
    index = get_alias_index(
        str(content_root.resolve()),
        str(bron_root.resolve()) if bron_root else None,
    )
    return index.resolve_vsa_path(reference)
