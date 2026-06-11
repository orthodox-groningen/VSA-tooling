from pathlib import Path


def read(path):
    return Path(path).read_text(encoding="utf-8")


def test_hugo_default_baseurl_is_root_for_local_use():
    text = read("examples/hugo-demo/hugo.toml")

    assert 'baseURL = "/"' in text


def test_pages_workflow_uses_github_pages_url_not_github_server_url():
    text = read(".github/workflows/pages-demo.yml")

    assert "github.server_url" not in text
    assert "github.repository }}" not in text
    assert "github.repository_owner" in text
    assert "github.event.repository.name" in text
    assert "github.io" in text


def test_pages_workflow_builds_with_pages_baseurl():
    text = read(".github/workflows/pages-demo.yml")

    assert '--baseURL "https://${{ github.repository_owner }}.github.io/${{ github.event.repository.name }}/"' in text


def test_local_scripts_use_root_baseurl():
    for script in [
        "scripts/serve-hugo.cmd",
        "scripts/build-preview.cmd",
        "scripts/build-production.cmd",
    ]:
        text = read(script)

        assert "--baseURL /" in text


def test_site_build_artifact_workflow_uses_root_baseurl():
    text = read(".github/workflows/site-build.yml")

    assert "--baseURL /" in text


def test_base_template_uses_relurl_for_navigation_and_css():
    text = read("examples/hugo-demo/layouts/_default/baseof.html")

    assert "relURL" in text
    assert 'href="{{ "voorbeelden/' in text
    assert 'href="/voorbeelden/' not in text
    assert 'href="/css/site.css"' not in text


def test_shortcode_strips_leading_slash_before_relurl():
    text = read("examples/hugo-demo/layouts/shortcodes/vsa.html")

    assert 'replaceRE "^/" "" $src' in text
    assert 'src="{{ $src | relURL }}"' in text
