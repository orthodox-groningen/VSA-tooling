#!/usr/bin/env python3
"""Rename TEv2 glossary ``_index.md`` to MkDocs ``index.md``.

HRGT writes ``terminologie/_index.md`` (Hugo/TEv2 convention). MkDocs publishes
that as ``/terminologie/_index/``, not ``/terminologie/``. After HRGT+sort,
rename so the public glossary URL matches ``saf.yaml`` ``navpath: /terminologie``.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "terminologie_dir",
        nargs="?",
        default="terminologie",
        type=Path,
        help="Directory with glossary _index.md (default: terminologie)",
    )
    args = parser.parse_args()
    src = args.terminologie_dir / "_index.md"
    dst = args.terminologie_dir / "index.md"
    if not src.is_file():
        print(f"ERROR: missing {src}", file=sys.stderr)
        return 1
    if dst.exists():
        dst.unlink()
    src.replace(dst)
    print(f"Renamed {src} -> {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
