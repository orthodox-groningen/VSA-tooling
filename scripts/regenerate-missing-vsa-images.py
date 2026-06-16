from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from vsa.markdown_vsa_blocks import extract_vsa_blocks_preserving_newlines
from vsa.parser import Parser
from vsa.svg_renderer import SVGRenderer


PUBLIC = ROOT / "examples" / "hugo-demo" / "public"
CONTENT_SOURCE = ROOT / "examples" / "hugo-demo" / "content-source"
VSA_DIR = PUBLIC / "vsa"

IMG_RE = re.compile(
    r'<img\b[^>]*\bclass="[^"]*\bvsa-notation\b[^"]*"[^>]*\bsrc="(?P<src>/vsa/(?P<name>[^"]+?)-block-(?P<block>\d+)\.svg)"',
    re.IGNORECASE,
)


def main() -> None:
    if not PUBLIC.exists():
        print(f"Niet gevonden: {PUBLIC}")
        print("Draai eerst scripts\\build-hugo.cmd")
        raise SystemExit(2)

    VSA_DIR.mkdir(parents=True, exist_ok=True)

    missing = collect_missing_images()

    if not missing:
        print("Geen ontbrekende VSA SVG's gevonden.")
        return

    written = []
    failed = []

    for item in missing:
        html, stem, block_number, target = item
        source = html_to_content_source(html)

        if source is None or not source.exists():
            failed.append((html, target, "geen content-source markdown gevonden"))
            continue

        try:
            svg = render_block(source, block_number)
        except Exception as exc:
            failed.append((html, target, str(exc)))
            continue

        target.write_text(svg, encoding="utf-8")
        written.append(target)

    print("Stap 76: ontbrekende VSA SVG's regenereren")
    if written:
        print("Geschreven:")
        for path in written:
            print(f"- {path.relative_to(ROOT)}")

    if failed:
        print()
        print("Niet gelukt:")
        for html, target, reason in failed:
            print(f"- {html.relative_to(ROOT)} -> {target.relative_to(ROOT)}: {reason}")
        raise SystemExit(1)


def collect_missing_images() -> list[tuple[Path, str, int, Path]]:
    missing = []

    for html in sorted(PUBLIC.rglob("*.html")):
        text = html.read_text(encoding="utf-8", errors="ignore")
        for match in IMG_RE.finditer(text):
            stem = match.group("name")
            block_number = int(match.group("block"))
            target = VSA_DIR / f"{stem}-block-{block_number}.svg"
            if not target.exists():
                missing.append((html, stem, block_number, target))

    return missing


def normalize_path(path: Path) -> Path:
    if path.is_absolute():
        return path.resolve()

    return (ROOT / path).resolve()


def html_to_content_source(html: Path) -> Path | None:
    html = normalize_path(html)

    try:
        rel = html.relative_to(PUBLIC.resolve())
    except ValueError:
        return None

    if rel.name.lower() != "index.html":
        return None

    route_parts = rel.parent.parts
    if not route_parts:
        return CONTENT_SOURCE / "_index.md"

    candidates = [
        CONTENT_SOURCE.joinpath(*route_parts).with_suffix(".md"),
        CONTENT_SOURCE.joinpath(*route_parts) / "index.md",
        CONTENT_SOURCE.joinpath(*route_parts) / "_index.md",
    ]

    for candidate in candidates:
        if candidate.exists():
            return candidate

    return candidates[0]


def render_block(source: Path, block_number: int) -> str:
    markdown = source.read_text(encoding="utf-8")
    blocks = extract_vsa_blocks_preserving_newlines(markdown)

    if block_number < 1 or block_number > len(blocks):
        raise ValueError(f"blok {block_number} bestaat niet in {source}")

    block = blocks[block_number - 1]
    document = Parser(block.source).parse()
    renderer = SVGRenderer()
    return renderer.render_document(document)


if __name__ == "__main__":
    main()
