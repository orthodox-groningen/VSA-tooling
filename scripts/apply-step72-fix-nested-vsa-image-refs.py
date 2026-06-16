from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "scripts" / "build-hugo.cmd"
LINE = "python scripts\\repair-vsa-image-refs.py"


def main() -> None:
    if not BUILD.exists():
        print(f"Niet gevonden: {BUILD}")
        raise SystemExit(1)

    text = BUILD.read_text(encoding="utf-8")

    if LINE in text:
        print("Repair stap staat al in build-hugo.cmd.")
        return

    markers = [
        "[3/4] Run tests",
        "[3/4] Build Hugo",
        "hugo",
    ]

    inserted = False
    for marker in markers:
        idx = text.find(marker)
        if idx >= 0:
            line_start = text.rfind("\n", 0, idx)
            if line_start < 0:
                line_start = 0
            text = text[:line_start] + f"\r\n{LINE}\r\n" + text[line_start:]
            inserted = True
            break

    if not inserted:
        text = text.rstrip() + f"\r\n{LINE}\r\n"

    BUILD.write_text(text, encoding="utf-8")
    print("Aangepast: scripts\\build-hugo.cmd")
    print("Voer nu uit:")
    print(LINE)


if __name__ == "__main__":
    main()
