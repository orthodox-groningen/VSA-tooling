from pathlib import Path

BUILD = Path("scripts/build-hugo.cmd")
ASSERT = Path("scripts/assert-real-font-metrics.py")


def test_assert_real_font_metrics_script_exists():
    assert ASSERT.exists()


def test_build_hugo_uses_venv_python_when_available():
    text = BUILD.read_text(encoding="utf-8")
    assert 'if exist .venv\\Scripts\\python.exe set "PY=.venv\\Scripts\\python.exe"' in text
    assert '"%PY%" scripts\\update-spacing-diagnostics-metadata.py' in text
    assert '"%PY%" scripts\\assert-real-font-metrics.py' in text
    assert '"%PY%" -m vsa.cli build-markdown ^' in text


def test_build_hugo_is_compact_and_does_not_call_linkchecker():
    text = BUILD.read_text(encoding="utf-8").replace("\r\n", "\n")
    assert "\n\n\n" not in text
    assert "check-hugo-links-and-assets.py" not in text
    assert "regenerate-missing-vsa-images.py" not in text
