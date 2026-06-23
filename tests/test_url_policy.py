from pathlib import Path


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def test_no_github_server_url_in_pages_workflows():
    for path in [
        ".github/workflows/pages-demo.yml",
        ".github/workflows/pages-preview.yml",
    ]:
        text = read(path)
        assert "github.server_url" not in text
        assert "github.repository }}" not in text


def test_production_pages_workflow_builds_with_project_site_baseurl():
    text = read(".github/workflows/pages-demo.yml")

    assert '--baseURL "https://orthodox-groningen.github.io/VSA-tooling/"' in text


def test_preview_pages_workflow_builds_with_preview_baseurl():
    text = read(".github/workflows/pages-preview.yml")

    assert '--baseURL "https://orthodox-groningen.github.io/VSA-tooling/preview/"' in text


def test_preview_url_is_not_used_as_production_baseurl():
    text = read(".github/workflows/pages-demo.yml")

    assert "https://orthodox-groningen.github.io/VSA-tooling/preview/" not in text


def test_hugo_invocations_use_explicit_baseurl():
    production = read(".github/workflows/pages-demo.yml")
    preview = read(".github/workflows/pages-preview.yml")

    assert "--baseURL" in production
    assert "--baseURL" in preview


def test_pages_preview_and_production_use_github_pages_host():
    production = read(".github/workflows/pages-demo.yml")
    preview = read(".github/workflows/pages-preview.yml")

    assert "https://orthodox-groningen.github.io/VSA-tooling/" in production
    assert "https://orthodox-groningen.github.io/VSA-tooling/preview/" in preview


def test_pages_url_policy_uses_project_site_subpath():
    production = read(".github/workflows/pages-demo.yml")
    preview = read(".github/workflows/pages-preview.yml")

    assert "https://orthodox-groningen.github.io/VSA-tooling/" in production
    assert "https://orthodox-groningen.github.io/VSA-tooling/preview/" in preview
