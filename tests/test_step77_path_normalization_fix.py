from pathlib import Path
from importlib.util import module_from_spec, spec_from_file_location


def load_module():
    path = Path("scripts/regenerate-missing-vsa-images.py")
    spec = spec_from_file_location("regenerate_missing_vsa_images", path)
    module = module_from_spec(spec)
    assert spec is not None
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_html_to_content_source_accepts_relative_path():
    mod = load_module()

    html = Path("examples/hugo-demo/public/praktijk/weekdagen/woensdag/index.html")
    expected = Path("examples/hugo-demo/content-source/praktijk/weekdagen/woensdag.md").resolve()

    assert mod.html_to_content_source(html).resolve() == expected


def test_html_to_content_source_accepts_absolute_path():
    mod = load_module()

    html = Path("examples/hugo-demo/public/praktijk/weekdagen/woensdag/index.html").resolve()
    expected = Path("examples/hugo-demo/content-source/praktijk/weekdagen/woensdag.md").resolve()

    assert mod.html_to_content_source(html).resolve() == expected


def test_html_to_content_source_returns_none_outside_public():
    mod = load_module()

    assert mod.html_to_content_source(Path("docs/todo.md")) is None
