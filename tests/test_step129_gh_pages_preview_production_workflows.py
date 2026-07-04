from pathlib import Path


PREVIEW = Path(".github/workflows/pages-preview.yml")
PRODUCTION = Path(".github/workflows/pages-demo.yml")


def test_preview_workflow_deploys_preview_directory_to_gh_pages():
    text = PREVIEW.read_text(encoding="utf-8")

    assert "actions/upload-pages-artifact@v3" in text
    assert "actions/deploy-pages@v4" in text
    assert "pages-site/preview/" in text


def test_preview_workflow_uses_preview_baseurl():
    text = PREVIEW.read_text(encoding="utf-8")

    assert '--baseURL "https://orthodox-groningen.github.io/VSA-tooling/preview/"' in text


def test_preview_workflow_updates_navigation_placeholders():
    text = PREVIEW.read_text(encoding="utf-8")

    assert "update-nav-placeholders.py generated/preview/content" in text


def test_production_workflow_remains_manual():
    text = PRODUCTION.read_text(encoding="utf-8")

    assert "workflow_dispatch:" in text
    assert "push:" not in text


def test_production_workflow_deploys_root_to_gh_pages():
    text = PRODUCTION.read_text(encoding="utf-8")

    assert "actions/upload-pages-artifact@v3" in text
    assert "actions/deploy-pages@v4" in text
    assert "generated/site/" in text


def test_workflows_share_pages_deploy_permissions_and_concurrency():
    for path in (PREVIEW, PRODUCTION):
        text = path.read_text(encoding="utf-8")
        assert "pages: write" in text
        assert "id-token: write" in text
        assert "group: pages-vsa-tooling" in text
