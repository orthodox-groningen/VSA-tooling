from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
CONTENT_ROOT = ROOT / "examples/hugo-demo/content-source"
START = "<!-- VSA-NAV-START -->"
END = "<!-- VSA-NAV-END -->"


def main() -> None:
    if not CONTENT_ROOT.exists():
        print(f"Niet gevonden: {CONTENT_ROOT}")
        raise SystemExit(1)

    changed = []

    for path in sorted(CONTENT_ROOT.rglob("*.md")):
        original = path.read_text(encoding="utf-8")
        text = remove_nav_blocks(original)

        if text != original:
            path.write_text(text.rstrip() + "\n", encoding="utf-8")
            changed.append(path)

    print("Stap 69: VSA-NAV blokken verwijderd.")
    if changed:
        for path in changed:
            print(f"- {path.relative_to(ROOT)}")
    else:
        print("Geen VSA-NAV blokken gevonden.")


def remove_nav_blocks(text: str) -> str:
    pattern = re.compile(
        r"\n*<!-- VSA-NAV-START -->.*?<!-- VSA-NAV-END -->\n*",
        flags=re.DOTALL,
    )
    text = pattern.sub("\n\n", text)

    # Ruim overtollige lege regels op, zonder codeblokken inhoudelijk te wijzigen.
    text = re.sub(r"\n{4,}", "\n\n\n", text)

    return text.strip() + "\n"


if __name__ == "__main__":
    main()
