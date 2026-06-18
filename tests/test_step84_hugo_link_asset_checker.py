from pathlib import Path
from importlib.util import module_from_spec, spec_from_file_location
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "check-hugo-links-and-assets.py"
APPLY = ROOT / "scripts" / "apply-step84-hugo-link-asset-checker.py"


def load_module():
    spec = spec_from_file_location("check_hugo_links_and_assets", SCRIPT)
    module = module_from_spec(spec)
    assert spec is not None
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_checker_script_exists():
    assert SCRIPT.exists()
    assert APPLY.exists()


def test_skip_external_and_fragment_links():
    mod = load_module()
    assert mod.should_skip("#x")
    assert mod.should_skip("https://example.org")
    assert mod.should_skip("mailto:test@example.org")
    assert not mod.should_skip("/praktijk/")


def test_forbidden_routes_detect_old_locations():
    mod = load_module()
    assert mod.is_forbidden_route("/zondag/")
    assert mod.is_forbidden_route("/voorbeelden/praktijk/weekdagen/")
    assert not mod.is_forbidden_route("/praktijk/zondagen/")


def test_apply_step84_no_longer_mutates_build_hugo():
    build = ROOT / "scripts" / "build-hugo.cmd"
    before = build.read_text(encoding="utf-8") if build.exists() else ""

    result = subprocess.run(
        [sys.executable, str(APPLY)],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    after = build.read_text(encoding="utf-8") if build.exists() else ""
    assert result.returncode == 0
    assert before == after
