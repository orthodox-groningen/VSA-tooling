from pathlib import Path
import subprocess
import sys


SCRIPT = Path("scripts/apply-step70-ci-rendering-fonts-os-guard.py")
WORKFLOW_DIR = Path(".github/workflows")


def test_step70_script_exists():
    assert SCRIPT.exists()


def test_step70_script_runs():
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Stap 70" in result.stdout


def test_rendering_font_install_is_linux_guarded_after_apply():
    if not WORKFLOW_DIR.exists():
        return

    offenders = []

    for path in list(WORKFLOW_DIR.glob("*.yml")) + list(WORKFLOW_DIR.glob("*.yaml")):
        text = path.read_text(encoding="utf-8")

        if "fonts-dejavu-core" not in text:
            continue

        if "if: runner.os == 'Linux'" not in text:
            offenders.append(str(path))

    assert offenders == []


def test_no_unguarded_sudo_apt_get_font_step_after_apply():
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
