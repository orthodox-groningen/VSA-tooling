from pathlib import Path
from importlib.util import module_from_spec, spec_from_file_location
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
CLEAN = ROOT / "scripts" / "clean-hugo-public.py"
CHECK = ROOT / "scripts" / "check-hugo-links-and-assets.py"
APPLY = ROOT / "scripts" / "apply-step86-clean-build-regenerate-check.py"


def load_checker():
    spec = spec_from_file_location("check_hugo_links_and_assets", CHECK)
    module = module_from_spec(spec)
    assert spec is not None
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_step86_scripts_exist():
    assert CLEAN.exists()
    assert CHECK.exists()
    assert APPLY.exists()


def test_linkchecker_skips_livereload():
    mod = load_checker()
    assert mod.should_skip("/livereload.js?mindelay=10&v=2&port=1313&path=livereload")


def test_apply_step86_no_longer_mutates_build_hugo():
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
