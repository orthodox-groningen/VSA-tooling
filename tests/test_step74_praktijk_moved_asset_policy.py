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


def test_asset_stem_is_based_on_actual_relative_path_not_hardcoded_prefix():
    mod = load_repair_module()
    root = Path("examples/hugo-demo/content-source")

    assert mod.asset_stem_for_markdown(root / "praktijk/donderdag.md", root) == "praktijk-donderdag"
    assert mod.asset_stem_for_markdown(root / "voorbeelden/rendering/spacing-diagnostiek.md", root) == "voorbeelden-rendering-spacing-diagnostiek"


def test_repair_script_can_handle_both_old_and_new_praktijk_locations():
    mod = load_repair_module()
    root = Path("examples/hugo-demo/content-source")

    old_path = root / "voorbeelden/praktijk/weekdagen/woensdag.md"
    new_path = root / "praktijk/weekdagen/woensdag.md"

    assert mod.asset_stem_for_markdown(old_path, root) != mod.asset_stem_for_markdown(new_path, root)
    assert mod.asset_stem_for_markdown(new_path, root) == "praktijk-weekdagen-woensdag"
