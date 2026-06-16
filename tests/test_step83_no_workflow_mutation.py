from pathlib import Path
from importlib.util import module_from_spec, spec_from_file_location


SCRIPT = Path("scripts/normalize-workflow-yaml-whitespace.py")


def load_module():
    spec = spec_from_file_location("normalize_workflow_yaml_whitespace", SCRIPT)
    module = module_from_spec(spec)
    assert spec is not None
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_normalize_script_exists():
    assert SCRIPT.exists()


def test_normalize_blank_lines_collapses_excessive_blank_lines():
    mod = load_module()

    source = "a\n\n\n\nb\n\n\nc\n"
    assert mod.normalize_blank_lines(source) == "a\n\nb\n\nc\n"
