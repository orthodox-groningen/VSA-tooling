"""Generate or check docs walkthrough SVG previews from a manifest.

Usage:
  python scripts/sync-docs-walkthrough-svgs.py
  python scripts/sync-docs-walkthrough-svgs.py --check
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    import tomli as tomllib  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "guides" / "assets" / "walkthroughs" / "manifest.toml"
ASSETS_DIR = MANIFEST.parent


def _load_manifest() -> list[dict]:
    data = tomllib.loads(MANIFEST.read_text(encoding="utf-8"))
    entries = data.get("svg")
    if not isinstance(entries, list) or not entries:
        raise SystemExit(f"Geen [[svg]]-entries in {MANIFEST.relative_to(ROOT)}")
    return entries


def _render(source: Path, max_line_width: float) -> str:
    from vsa.svg_export import export_svg
    import tempfile

    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".svg", delete=False, encoding="utf-8"
    ) as tmp:
        tmp_path = Path(tmp.name)
    try:
        export_svg(str(source), str(tmp_path), max_line_width=max_line_width)
        return tmp_path.read_text(encoding="utf-8")
    finally:
        tmp_path.unlink(missing_ok=True)


def _expected_outputs(entries: list[dict]) -> set[Path]:
    return {(ROOT / e["output"]).resolve() for e in entries}


def sync(*, check: bool) -> int:
    entries = _load_manifest()
    expected = _expected_outputs(entries)
    errors: list[str] = []

    ASSETS_DIR.mkdir(parents=True, exist_ok=True)

    for entry in entries:
        source = ROOT / entry["source"]
        output = ROOT / entry["output"]
        width = float(entry.get("max_line_width", 800.0))

        if not source.is_file():
            errors.append(f"bron ontbreekt: {entry['source']}")
            continue

        try:
            svg = _render(source, width)
        except Exception as exc:  # noqa: BLE001 — surface any render failure
            errors.append(f"render faalde voor {entry['source']}: {exc}")
            continue

        if check:
            if not output.is_file():
                errors.append(f"output ontbreekt: {entry['output']}")
            elif output.read_text(encoding="utf-8") != svg:
                errors.append(f"output verouderd: {entry['output']}")
        else:
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(svg, encoding="utf-8")
            print(f"SVG geschreven: {entry['output']}")

    # Orphan cleanup / check: SVG's in assets dir die niet in het manifest staan.
    for path in sorted(ASSETS_DIR.glob("*.svg")):
        if path.resolve() not in expected:
            rel = path.relative_to(ROOT).as_posix()
            if check:
                errors.append(f"orphan SVG (niet in manifest): {rel}")
            else:
                path.unlink()
                print(f"orphan verwijderd: {rel}")

    if errors:
        for msg in errors:
            print(msg, file=sys.stderr)
        return 1
    if check:
        print("OK - walkthrough-SVGs match manifest")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Faal als outputs ontbreken, afwijken of orphans bestaan",
    )
    args = parser.parse_args(argv)
    return sync(check=args.check)


if __name__ == "__main__":
    raise SystemExit(main())
