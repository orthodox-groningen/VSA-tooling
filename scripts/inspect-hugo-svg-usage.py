from __future__ import annotations

from pathlib import Path
import re
import sys


PUBLIC_DIR = Path("examples/hugo-demo/public")


def main():
    query = " ".join(sys.argv[1:]).strip().lower()

    if not PUBLIC_DIR.exists():
        print(f"Niet gevonden: {PUBLIC_DIR}")
        print("Draai eerst: scripts\\build-hugo.cmd")
        raise SystemExit(2)

    html_files = sorted(PUBLIC_DIR.rglob("*.html"))
    svg_files = sorted((PUBLIC_DIR / "vsa").glob("*.svg")) if (PUBLIC_DIR / "vsa").exists() else []

    if query:
        html_files = [
            path for path in html_files
            if query in str(path).lower()
            or query in path.read_text(encoding="utf-8", errors="ignore").lower()
        ]
        svg_files = [
            path for path in svg_files
            if query in str(path).lower()
            or query in path.read_text(encoding="utf-8", errors="ignore").lower()
        ]

    print("=== Hugo SVG usage inspectie ===")
    print(f"Public dir : {PUBLIC_DIR}")
    print(f"HTML files : {len(html_files)}")
    print(f"SVG files  : {len(svg_files)}")
    print()

    print("=== SVG bestanden ===")
    for path in svg_files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        line_count = text.count('class="vsa-line"')
        width = _extract_attr(text, "width")
        height = _extract_attr(text, "height")

        print(f"{path}")
        print(f"  vsa-line count: {line_count}")
        print(f"  size          : {width} x {height}")
        if line_count <= 1:
            print("  LET OP: deze SVG heeft maar één renderregel.")
        print()

    print("=== HTML verwijzingen naar SVG ===")
    for path in html_files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        refs = _find_svg_refs(text)

        if not refs:
            continue

        print(path)
        for ref in refs:
            svg_path = _resolve_svg_ref(path, ref)
            exists = svg_path.exists() if svg_path else False
            line_count = None

            if exists:
                svg_text = svg_path.read_text(encoding="utf-8", errors="ignore")
                line_count = svg_text.count('class="vsa-line"')

            print(f"  ref       : {ref}")
            print(f"  resolved  : {svg_path if svg_path else '?'}")
            print(f"  exists    : {exists}")
            if line_count is not None:
                print(f"  vsa-lines : {line_count}")

        scale_hints = _find_scale_hints(text)
        if scale_hints:
            print("  scale/html hints:")
            for hint in scale_hints:
                print(f"    {hint}")
        print()

    css_files = sorted(PUBLIC_DIR.rglob("*.css"))
    print("=== CSS hints ===")
    for path in css_files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        hits = []
        for pattern in ["svg", "img", "vsa", "max-width", "height", "object-fit"]:
            if pattern in text:
                hits.append(pattern)
        if hits:
            print(f"{path}: {', '.join(sorted(set(hits)))}")


def _extract_attr(svg: str, name: str) -> str:
    match = re.search(rf'\b{name}="([^"]+)"', svg)
    return match.group(1) if match else "?"


def _find_svg_refs(html: str) -> list[str]:
    refs = []
    for pattern in [
        r'<img[^>]+src="([^"]+\.svg)"',
        r'<object[^>]+data="([^"]+\.svg)"',
        r'<embed[^>]+src="([^"]+\.svg)"',
        r'<a[^>]+href="([^"]+\.svg)"',
    ]:
        refs.extend(re.findall(pattern, html, flags=re.IGNORECASE))
    return refs


def _resolve_svg_ref(html_path: Path, ref: str) -> Path | None:
    ref = ref.split("#", 1)[0].split("?", 1)[0]
    if ref.startswith("/"):
        return PUBLIC_DIR / ref.lstrip("/")
    return (html_path.parent / ref).resolve()


def _find_scale_hints(html: str) -> list[str]:
    hints = []
    for match in re.finditer(r'<img[^>]+\.svg[^>]*>', html, flags=re.IGNORECASE):
        tag = match.group(0)
        attrs = []
        for attr in ["width", "height", "style", "class"]:
            found = re.search(rf'\b{attr}="([^"]+)"', tag)
            if found:
                attrs.append(f'{attr}="{found.group(1)}"')
        if attrs:
            hints.append("img " + " ".join(attrs))
    return hints


if __name__ == "__main__":
    main()
