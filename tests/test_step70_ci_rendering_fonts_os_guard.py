from pathlib import Path


WORKFLOW_DIR = Path(".github/workflows")


def test_existing_workflows_do_not_have_unguarded_font_install():
    if not WORKFLOW_DIR.exists():
        return

    offenders = []

    for path in list(WORKFLOW_DIR.glob("*.yml")) + list(WORKFLOW_DIR.glob("*.yaml")):
        lines = path.read_text(encoding="utf-8").splitlines()

        for index, line in enumerate(lines):
            if "sudo apt-get" in line and "fonts-dejavu-core" in line:
                previous = "\n".join(lines[max(0, index - 3):index + 1])
                if "if: runner.os == 'Linux'" not in previous:
                    offenders.append(f"{path}:{index + 1}")

    assert offenders == []


def test_rendering_requirements_are_documented():
    assert Path("requirements-rendering.txt").exists()
    text = Path("requirements-rendering.txt").read_text(encoding="utf-8")
    assert "Pillow" in text
