from pathlib import Path
import re


DEMO_MD = list(Path("examples/hugo-demo/content-source").rglob("*.md"))


def test_demo_markdown_does_not_use_root_absolute_internal_links():
    for path in DEMO_MD:
        text = path.read_text(encoding="utf-8")

        bad_links = re.findall(r"\]\(/(?!vsa/)[^)]+", text)

        assert bad_links == [], f"{path}: {bad_links}"


def test_base_template_uses_relurl_for_navigation_and_css():
    text = Path("examples/hugo-demo/layouts/_default/baseof.html").read_text(encoding="utf-8")

    assert "relURL" in text
    assert 'href="{{ "voorbeelden/' in text
    assert 'href="/voorbeelden/' not in text
    assert '/css/site.css' not in text


def test_vsa_shortcode_uses_relurl_for_images():
    text = Path("examples/hugo-demo/layouts/shortcodes/vsa.html").read_text(encoding="utf-8")

    assert "relURL" in text
    assert 'src="{{ $src | relURL }}"' in text


def test_demo_scripts_use_shortcode_output_for_subpath_safe_assets():
    for script in [
        "scripts/build-preview.cmd",
        "scripts/build-production.cmd",
        "scripts/serve-hugo.cmd",
    ]:
        text = Path(script).read_text(encoding="utf-8")

        assert "--output-mode shortcode" in text


def test_responsive_css_uses_full_width_on_small_screens():
    text = Path("examples/hugo-demo/static/css/site.css").read_text(encoding="utf-8")

    assert "width: 100%" in text
    assert "max-width: none" in text
    assert "env(safe-area-inset-left)" in text
    assert "@media (max-width: 600px)" in text
