from pathlib import Path
import re


PYPROJECT = Path("pyproject.toml")
REQUIREMENTS = Path("requirements-rendering.txt")
WORKFLOW_DIR = Path(".github/workflows")


def main():
    changed = []

    if patch_pyproject():
        changed.append(str(PYPROJECT))

    if patch_workflows():
        changed.append(".github/workflows/*.yml")

    print("Stap 66 - Pillow dependency en CI setup")
    if changed:
        print("Aangepast:")
        for item in changed:
            print(f"- {item}")
    else:
        print("Geen automatische wijzigingen nodig of geen doelbestanden gevonden.")

    print()
    print("Controle:")
    print("python scripts\\debug-font-metrics.py")
    print("python -m pytest tests\\test_step66_pillow_dependency_ci.py -v")


def patch_pyproject() -> bool:
    if not PYPROJECT.exists():
        return False

    text = PYPROJECT.read_text(encoding="utf-8")
    original = text

    if "Pillow" in text or "pillow" in text:
        return False

    # PEP 621 style dependencies = [...]
    match = re.search(r"dependencies\s*=\s*\[(?P<body>.*?)\]", text, flags=re.DOTALL)
    if match:
        body = match.group("body").rstrip()
        insertion = body
        if body and not body.endswith(","):
            insertion += ","
        insertion += '\n    "Pillow>=10.0",'
        text = text[:match.start("body")] + insertion + text[match.end("body"):]
    else:
        text += """

[project.optional-dependencies]
rendering = [
    "Pillow>=10.0",
]
"""

    if text != original:
        PYPROJECT.write_text(text, encoding="utf-8")
        return True

    return False


def patch_workflows() -> bool:
    if not WORKFLOW_DIR.exists():
        return False

    changed = False

    for path in list(WORKFLOW_DIR.glob("*.yml")) + list(WORKFLOW_DIR.glob("*.yaml")):
        text = path.read_text(encoding="utf-8")
        original = text

        if "fonts-dejavu-core" not in text:
            text = insert_before_first_python_or_build_step(
                text,
                """      - name: Install rendering fonts
        run: sudo apt-get update && sudo apt-get install -y fonts-dejavu-core

"""
            )

        if "requirements-rendering.txt" not in text:
            text = insert_before_first_python_or_build_step(
                text,
                """      - name: Install rendering dependencies
        run: python -m pip install -r requirements-rendering.txt

"""
            )

        if text != original:
            path.write_text(text, encoding="utf-8")
            changed = True

    return changed


def insert_before_first_python_or_build_step(text: str, block: str) -> str:
    markers = [
        "      - name: Build",
        "      - name: Build Hugo",
        "      - name: Generate",
        "      - name: Test",
        "      - name: Install dependencies",
    ]

    positions = [text.find(marker) for marker in markers if text.find(marker) >= 0]
    if positions:
        pos = min(positions)
        return text[:pos] + block + text[pos:]

    return text.rstrip() + "\n\n" + block


if __name__ == "__main__":
    main()
