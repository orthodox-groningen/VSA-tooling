from pathlib import Path


def test_base_template_has_viewport_meta():
    text = Path("examples/hugo-demo/layouts/_default/baseof.html").read_text(encoding="utf-8")

    assert 'name="viewport"' in text
    assert "width=device-width" in text


def test_base_template_links_site_css():
    text = Path("examples/hugo-demo/layouts/_default/baseof.html").read_text(encoding="utf-8")

    assert "css/site.css" in text
    assert "relURL" in text


def test_responsive_css_exists():
    assert Path("examples/hugo-demo/static/css/site.css").exists()


def test_responsive_css_contains_mobile_breakpoints():
    text = Path("examples/hugo-demo/static/css/site.css").read_text(encoding="utf-8")

    assert "@media (max-width: 600px)" in text
    assert "@media (max-width: 900px)" in text
    assert "max-width: 100%" in text
    assert "overflow-x: auto" in text


def test_shortcode_uses_lazy_loading_and_responsive_class():
    text = Path("examples/hugo-demo/layouts/shortcodes/vsa.html").read_text(encoding="utf-8")

    assert 'class="vsa-notation"' in text
    assert 'loading="lazy"' in text
