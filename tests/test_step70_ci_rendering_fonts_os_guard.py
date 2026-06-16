from pathlib import Path
from importlib.util import module_from_spec, spec_from_file_location


SCRIPT = Path("scripts/apply-step70-ci-rendering-fonts-os-guard.py")
WORKFLOW_DIR = Path(".github/workflows")


def load_step70_module():
    spec = spec_from_file_location("apply_step70", SCRIPT)
    module = module_from_spec(spec)
    assert spec is not None
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_step70_script_exists():
    assert SCRIPT.exists()


def test_patch_workflow_adds_linux_guard_without_touching_files():
    mod = load_step70_module()

    source = """name: test
jobs:
  test:
    runs-on: windows-latest
    steps:
      - name: Run tests
        run: pytest
"""

    patched = mod.patch_workflow(source)

    assert "Install rendering fonts" in patched
    assert "if: runner.os == 'Linux'" in patched
    assert "fonts-dejavu-core" in patched


def test_patch_workflow_is_idempotent_without_touching_files():
    mod = load_step70_module()

    source = """name: test
jobs:
  test:
    runs-on: windows-latest
    steps:
      - name: Run tests
        run: pytest
"""

    once = mod.patch_workflow(source)
    twice = mod.patch_workflow(once)

    assert once == twice


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
