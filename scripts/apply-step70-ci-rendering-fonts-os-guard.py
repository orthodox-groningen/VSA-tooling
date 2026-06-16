from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_DIR = ROOT / ".github" / "workflows"


FONT_STEP_NAME = "Install rendering fonts"
FONT_STEP = """      - name: Install rendering fonts
        if: runner.os == 'Linux'
        run: sudo apt-get update && sudo apt-get install -y fonts-dejavu-core
"""


def main() -> None:
    if not WORKFLOW_DIR.exists():
        print(f"Niet gevonden: {WORKFLOW_DIR}")
        raise SystemExit(1)

    changed = []

    for path in sorted(list(WORKFLOW_DIR.glob("*.yml")) + list(WORKFLOW_DIR.glob("*.yaml"))):
        original = path.read_text(encoding="utf-8")
        text = patch_workflow(original)

        if text != original:
            path.write_text(text, encoding="utf-8")
            changed.append(path)

    print("Stap 70: CI rendering fonts OS guard")
    if changed:
        print("Aangepast:")
        for path in changed:
            print(f"- {path.relative_to(ROOT)}")
    else:
        print("Geen wijzigingen nodig.")


def patch_workflow(text: str) -> str:
    text = remove_existing_font_steps(text)

    # Plaats Linux-only fontinstallatie vóór rendering dependencies of vóór tests/build.
    markers = [
        "      - name: Install rendering dependencies",
        "      - name: Run tests",
        "      - name: Test",
        "      - name: Run VSA CLI",
        "      - name: Build",
        "      - name: Build Hugo",
    ]

    positions = [text.find(marker) for marker in markers if text.find(marker) >= 0]

    if positions:
        pos = min(positions)
        text = text[:pos] + FONT_STEP + "\n" + text[pos:]
    else:
        text = text.rstrip() + "\n\n" + FONT_STEP + "\n"

    return text


def remove_existing_font_steps(text: str) -> str:
    # Verwijder eerdere Install rendering fonts blokken, inclusief foute sudo op Windows.
    pattern = re.compile(
        r"(?:\n)?"
        r"      - name: Install rendering fonts\n"
        r"(?:        if: .*\n)?"
        r"        run: .*(?:fonts-dejavu-core|apt-get).*\n",
        flags=re.MULTILINE,
    )
    return pattern.sub("", text)


if __name__ == "__main__":
    main()
