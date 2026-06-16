from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_DIR = ROOT / ".github" / "workflows"


def main() -> None:
    if not WORKFLOW_DIR.exists():
        print(f"Niet gevonden: {WORKFLOW_DIR}")
        return

    changed = []

    for path in sorted(list(WORKFLOW_DIR.glob("*.yml")) + list(WORKFLOW_DIR.glob("*.yaml"))):
        original = path.read_text(encoding="utf-8")
        text = normalize_blank_lines(original)

        if text != original:
            path.write_text(text, encoding="utf-8")
            changed.append(path)

    if changed:
        print("Workflow YAML whitespace opgeschoond:")
        for path in changed:
            print(f"- {path.relative_to(ROOT)}")
    else:
        print("Geen workflow whitespace wijzigingen nodig.")


def normalize_blank_lines(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.rstrip() + "\n"


if __name__ == "__main__":
    main()
