from pathlib import Path
from importlib.util import module_from_spec, spec_from_file_location


def load_repair_module():
    path = Path("scripts/repair-vsa-image-refs.py")
    spec = spec_from_file_location("repair_vsa_image_refs", path)
    module = module_from_spec(spec)
    assert spec is not None
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_repair_script_exists():
    assert Path("scripts/repair-vsa-image-refs.py").exists()


def test_nested_markdown_asset_stem_for_moved_praktijk_tree():
    mod = load_repair_module()
    content_dir = Path("examples/hugo-demo/content-source")
    path = content_dir / "praktijk/weekdagen/woensdag.md"

    assert mod.asset_stem_for_markdown(path, content_dir) == "praktijk-weekdagen-woensdag"


def test_nested_markdown_asset_stem_for_legacy_voorbeelden_tree():
    mod = load_repair_module()
    content_dir = Path("examples/hugo-demo/content-source")
    path = content_dir / "voorbeelden/praktijk/weekdagen/woensdag.md"

    assert mod.asset_stem_for_markdown(path, content_dir) == "voorbeelden-praktijk-weekdagen-woensdag"


def test_public_html_asset_stem_for_moved_praktijk_tree():
    mod = load_repair_module()
    public_dir = Path("examples/hugo-demo/public")
    path = public_dir / "praktijk/weekdagen/woensdag/index.html"

    assert mod.asset_stem_for_public_html(path, public_dir) == "praktijk-weekdagen-woensdag"


def test_public_html_asset_stem_for_legacy_voorbeelden_tree():
    mod = load_repair_module()
    public_dir = Path("examples/hugo-demo/public")
    path = public_dir / "voorbeelden/praktijk/weekdagen/woensdag/index.html"

    assert mod.asset_stem_for_public_html(path, public_dir) == "voorbeelden-praktijk-weekdagen-woensdag"


def test_rewrite_wrong_img_ref_to_expected_moved_nested_ref():
    mod = load_repair_module()

    html = '<img class="vsa-notation" src="/vsa/voorbeelden-praktijk-donderdag-block-1.svg" alt="VSA notatie">'
    fixed = mod.rewrite_img_refs(html, "praktijk-weekdagen-woensdag")

    assert '/vsa/praktijk-weekdagen-woensdag-block-1.svg' in fixed
    assert "donderdag" not in fixed


def test_apply_step72_script_exists():
    assert Path("scripts/apply-step72-fix-nested-vsa-image-refs.py").exists()
