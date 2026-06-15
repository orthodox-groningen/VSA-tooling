from pathlib import Path
import re
import sys

LINE_RE = re.compile(
    r'<g[^>]+class="vsa-line"[^>]*translate\(([^,]+),([^)]+)\)'
)

def inspect(path: Path):
    text = path.read_text(encoding="utf-8", errors="ignore")

    print(f"=== {path} ===")

    matches = LINE_RE.findall(text)

    if not matches:
        print("Geen vsa-line translate-posities gevonden.")
        return

    for idx, (x, y) in enumerate(matches, start=1):
        print(f"line {idx}: x={x} y={y}")

def main():
    if len(sys.argv) < 2:
        print("Gebruik:")
        print("python scripts\\inspect-svg-line-y.py <svgfile>")
        raise SystemExit(2)

    for arg in sys.argv[1:]:
        inspect(Path(arg))

if __name__ == "__main__":
    main()
