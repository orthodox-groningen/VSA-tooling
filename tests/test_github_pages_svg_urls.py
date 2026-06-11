from pathlib import Path


def test_vsa_shortcode_strips_leading_slash_before_relurl():
    text = Path("examples/hugo-demo/layouts/shortcodes/vsa.html").read_text(encoding="utf-8")

    assert 'replaceRE "^/" "" $src' in text
    assert 'src="{{ $src | relURL }}"' in text


def test_vsa_shortcode_still_uses_lazy_loading_and_class():
    text = Path("examples/hugo-demo/layouts/shortcodes/vsa.html").read_text(encoding="utf-8")

    assert 'class="vsa-notation"' in text
    assert 'loading="lazy"' in text
