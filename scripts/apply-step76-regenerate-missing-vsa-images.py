from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "scripts" / "build-hugo.cmd"
LINE = "python scripts\\regenerate-missing-vsa-images.py"


def main() -> None:
    if not BUILD.exists():
        print(f"Niet gevonden: {BUILD}")
        raise SystemExit(1)

    text = BUILD.read_text(encoding="utf-8")

    if LINE in text:
        print("Regenerate stap staat al in build-hugo.cmd.")
        return

    # Zet aan het einde, want dit script gebruikt gegenereerde HTML in public.
    text = text.rstrip() + f"\r\n{LINE}\r\n"
    BUILD.write_text(text, encoding="utf-8")

    print("Aangepast: scripts\\build-hugo.cmd")
    print("Toegevoegd aan einde:")
    print(LINE)


if __name__ == "__main__":
    main()
