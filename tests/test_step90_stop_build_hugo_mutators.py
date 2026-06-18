from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "scripts" / "build-hugo.cmd"

MUTATORS = [
    ROOT / "scripts" / "apply-step76-regenerate-missing-vsa-images.py",
    ROOT / "scripts" / "apply-step84-hugo-link-asset-checker.py",
    ROOT / "scripts" / "apply-step86-clean-build-regenerate-check.py",
]


def test_build_hugo_is_not_corrupt():
    text = BUILD.read_text(encoding="utf-8").replace("\r\n", "\n")
    assert "\n\n\n" not in text
    assert "hugo ^\npython scripts" not in text
    assert "regenerate-missing-vsa-images.py" not in text
    assert "check-hugo-links-and-assets.py" not in text


def test_old_mutators_do_not_change_build_hugo():
    before = BUILD.read_text(encoding="utf-8")

    for script in MUTATORS:
        result = subprocess.run(
            [sys.executable, str(script)],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        assert result.returncode == 0

    after = BUILD.read_text(encoding="utf-8")
    assert before == after
