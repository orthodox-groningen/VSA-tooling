"""
Parses optional YAML frontmatter from .vsa files.

A .vsa file may begin with a YAML block delimited by ``---``:

    ---
    muziek:
      do: F4
      mode: major
      tempo: 132
    identificatie:
      title: Troparion van de zondag, toon 1
      composer: Traditioneel
      language: nl
    ---
    [:] ...

The ``muziek`` section maps directly to block metadata keys (do, mode, tempo,
duration-model, meter, validate-ending). The ``identificatie`` section maps to
MusicXML identification fields. The ``typografie`` section maps to font
defaults for export renderers (see spec §4.1.2 and §8.2.10). Other sections
are preserved for future use.

Files without a ``---`` delimiter are returned unchanged.
"""

from __future__ import annotations

_DELIMITER = "---"


def parse_vsa_frontmatter(text: str) -> tuple[dict, str]:
    """Strip and parse optional YAML frontmatter from VSA source text.

    Returns ``(metadata_dict, vsa_body)`` where ``metadata_dict`` is empty
    when no valid frontmatter is present.
    """
    meta, body, _offset = parse_vsa_frontmatter_with_body_offset(text)
    return meta, body


def parse_vsa_frontmatter_with_body_offset(text: str) -> tuple[dict, str, int]:
    """Zoals ``parse_vsa_frontmatter``, plus start-offset van de body in ``text``."""
    if not text.startswith(_DELIMITER):
        return {}, text, 0

    # Find the closing delimiter on its own line
    after_open = text[len(_DELIMITER) :]
    close_idx = after_open.find("\n" + _DELIMITER)
    if close_idx == -1:
        return {}, text, 0

    yaml_text = after_open[:close_idx].strip()
    # ``close_idx`` wijst naar de ``\\n`` vóór de sluitende ``---``.
    close_at = len(_DELIMITER) + close_idx
    body_from = close_at + 1 + len(_DELIMITER)
    rest = text[body_from:]
    body = rest.lstrip("\n")
    body_offset = body_from + (len(rest) - len(body))

    try:
        import yaml  # optional; only needed for .vsa frontmatter

        data = yaml.safe_load(yaml_text) or {}
    except Exception:
        return {}, text, 0

    if not isinstance(data, dict):
        return {}, text, 0

    return data, body, body_offset


def frontmatter_to_block_metadata(frontmatter: dict) -> dict[str, str]:
    """Flatten YAML frontmatter into the flat ``key=value`` dict format used
    by :class:`~vsa.block_parser.MarkdownBlock`.

    The ``muziek`` section's keys are promoted to the top level (they match
    existing block metadata keys like ``do``, ``mode``, ``tempo``).

    All other sections are stored as ``section.key`` to avoid collisions.
    """
    result: dict[str, str] = {}

    muziek = frontmatter.get("muziek", {})
    if isinstance(muziek, dict):
        for k, v in muziek.items():
            result[str(k)] = str(v)

    for section, values in frontmatter.items():
        if section == "muziek":
            continue
        if isinstance(values, dict):
            for k, v in values.items():
                result[f"{section}.{k}"] = str(v)
        else:
            result[str(section)] = str(values)

    return result
