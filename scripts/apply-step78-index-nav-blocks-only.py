from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "scripts" / "build-hugo.cmd"
OLD_SCRIPTS = [
    "python scripts\\apply-step71-hugo-index-navigation.py",
    "python scripts\\apply-step75-navigation-praktijk-moved.py",
]
NEW_LINE = "python scripts\\update-index-navigation-blocks.py"


def main() -> None:
    if not BUILD.exists():
        print(f"Niet gevonden: {BUILD}")
        raise SystemExit(1)

    text = BUILD.read_text(encoding="utf-8")
    original = text

    for line in OLD_SCRIPTS:
        text = text.replace(line + "\r\n", "")
        text = text.replace(line + "\n", "")
        text = text.replace(line, "")

    if NEW_LINE not in text:
        marker = "[2/4] Generate Markdown + SVG"
        if marker in text:
            text = text.replace(
                f"echo {marker}",
                f"echo {marker}\r\n{NEW_LINE}",
                1,
            )
        else:
            text = text.rstrip() + f"\r\n{NEW_LINE}\r\n"

    if text != original:
        BUILD.write_text(text, encoding="utf-8")
        print("Aangepast: scripts\\build-hugo.cmd")
    else:
        print("Geen wijzigingen nodig in scripts\\build-hugo.cmd")

    print("Voer nu uit:")
    print(NEW_LINE)


if __name__ == "__main__":
    main()
