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


def test_regenerate_script_exists():
    assert Path("scripts/regenerate-missing-vsa-images.py").exists()


def test_apply_step76_script_exists():
    assert Path("scripts/apply-step76-regenerate-missing-vsa-images.py").exists()


def test_html_to_content_source_for_moved_praktijk_page():
    mod = load_module()

    html = Path("examples/hugo-demo/public/praktijk/weekdagen/woensdag/index.html")
    expected = Path("examples/hugo-demo/content-source/praktijk/weekdagen/woensdag.md").resolve()

    assert mod.html_to_content_source(html).resolve() == expected


def test_html_to_content_source_for_nested_heiligen_page():
    mod = load_module()

    html = Path("examples/hugo-demo/public/praktijk/heiligen/nicolaas-van-myra/index.html")
    expected = Path("examples/hugo-demo/content-source/praktijk/heiligen/nicolaas-van-myra.md").resolve()

    assert mod.html_to_content_source(html).resolve() == expected


def test_img_regex_extracts_vsa_block_name():
    mod = load_module()

    html = '<img class="vsa-notation" src="/vsa/praktijk-weekdagen-woensdag-block-4.svg" alt="VSA notatie">'
    match = mod.IMG_RE.search(html)

    assert match is not None
    assert match.group("name") == "praktijk-weekdagen-woensdag"
    assert match.group("block") == "4"
