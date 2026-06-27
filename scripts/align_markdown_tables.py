#!/usr/bin/env python3
"""Align markdown table columns in .md files (padding cells to equal column width)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

_SEPARATOR_RE = re.compile(r"^:?-{3,}:?$")


def _is_separator_cell(cell: str) -> bool:
    return bool(_SEPARATOR_RE.match(cell.strip()))


def _parse_row(line: str) -> list[str] | None:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None

    inner = stripped[1:-1]
    cells: list[str] = []
    current: list[str] = []
    i = 0
    while i < len(inner):
        ch = inner[i]
        if ch == "\\" and i + 1 < len(inner) and inner[i + 1] == "|":
            current.append("\\|")
            i += 2
            continue
        if ch == "|":
            cells.append("".join(current).strip())
            current = []
            i += 1
            continue
        current.append(ch)
        i += 1
    cells.append("".join(current).strip())
    return cells


def _align_table(rows: list[list[str]]) -> list[str]:
    if not rows:
        return []

    num_cols = len(rows[0])
    widths = [0] * num_cols
    for row in rows:
        if len(row) != num_cols:
            return []
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(cell), 3)

    out: list[str] = []
    for row in rows:
        if all(_is_separator_cell(c) for c in row):
            cells = ["-" * widths[i] for i in range(num_cols)]
        else:
            cells = [row[i].ljust(widths[i]) for i in range(num_cols)]
        out.append("| " + " | ".join(cells) + " |")
    return out


def _in_code_fence(line: str, in_fence: bool, fence_marker: str) -> tuple[bool, str]:
    stripped = line.strip()
    if stripped.startswith("```"):
        if not in_fence:
            return True, stripped[:3]
        if stripped.startswith(fence_marker):
            return False, ""
    return in_fence, fence_marker


def align_markdown(text: str) -> str:
    lines = text.splitlines()
    result: list[str] = []
    in_code_fence = False
    fence_marker = ""
    i = 0

    while i < len(lines):
        in_code_fence, fence_marker = _in_code_fence(lines[i], in_code_fence, fence_marker)
        if in_code_fence:
            result.append(lines[i])
            i += 1
            continue

        row = _parse_row(lines[i])
        if row is None:
            result.append(lines[i])
            i += 1
            continue

        block: list[list[str]] = [row]
        j = i + 1
        while j < len(lines):
            in_code_fence, fence_marker = _in_code_fence(lines[j], in_code_fence, fence_marker)
            if in_code_fence:
                break
            next_row = _parse_row(lines[j])
            if next_row is None or len(next_row) != len(row):
                break
            block.append(next_row)
            j += 1

        aligned = _align_table(block)
        if aligned:
            result.extend(aligned)
        else:
            result.extend(lines[i:j])
        i = j

    return "\n".join(result) + ("\n" if text.endswith("\n") else "")


def process_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    updated = align_markdown(original)
    if updated != original:
        path.write_text(updated, encoding="utf-8", newline="\n")
        return True
    return False


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: align_markdown_tables.py <file-or-dir> ...", file=sys.stderr)
        return 1

    changed = 0
    for arg in argv[1:]:
        p = Path(arg)
        files = [p] if p.is_file() else sorted(p.rglob("*.md"))
        for f in files:
            if process_file(f):
                print(f"aligned: {f}")
                changed += 1
    print(f"Done. {changed} file(s) updated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
