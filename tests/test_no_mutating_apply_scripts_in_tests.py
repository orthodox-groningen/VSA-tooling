from pathlib import Path
import re


TEST_DIR = Path("tests")


def test_tests_do_not_execute_apply_scripts_on_real_repo():
    offenders = []

    pattern = re.compile(r"subprocess\.run\([^)]*apply-step", re.DOTALL)

    for path in TEST_DIR.glob("test*.py"):
        if path.name == "test_no_mutating_apply_scripts_in_tests.py":
            continue

        text = path.read_text(encoding="utf-8")
        if pattern.search(text):
            offenders.append(str(path))

    assert offenders == []
