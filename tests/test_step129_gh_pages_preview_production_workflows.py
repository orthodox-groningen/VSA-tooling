from pathlib import Path


PREVIEW = Path(".github/workflows/pages-preview.yml")
PRODUCTION = Path(".github/workflows/pages-demo.yml")


def test_preview_workflow_deploys_preview_directory_to_gh_pages():
    text = PREVIEW.read_text(encoding="utf-8")
    reusable = Path(".github/workflows/pages-deploy-reusable.yml").read_text(
        encoding="utf-8"
    )

    assert "pages-deploy-reusable.yml" in text
    assert "destination_dir: preview" in text
    assert "peaceiris/actions-gh-pages@v3" in reusable
    assert "publish_branch: gh-pages" in reusable


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
    reusable = Path(".github/workflows/pages-deploy-reusable.yml").read_text(
        encoding="utf-8"
    )

    assert "pages-deploy-reusable.yml" in text
    assert "artifact_name: pages-production-site" in text
    assert "peaceiris/actions-gh-pages@v3" in reusable
    assert "destination_dir: preview" not in text


def test_workflows_do_not_use_deploy_pages_artifacts():
    assert "actions/deploy-pages" not in PREVIEW.read_text(encoding="utf-8")
    assert "actions/deploy-pages" not in PRODUCTION.read_text(encoding="utf-8")
    assert "actions/upload-pages-artifact" not in PREVIEW.read_text(encoding="utf-8")
    assert "actions/upload-pages-artifact" not in PRODUCTION.read_text(encoding="utf-8")


def test_pages_workflows_share_gh_pages_concurrency_without_cancel():
    reusable = Path(".github/workflows/pages-deploy-reusable.yml").read_text(
        encoding="utf-8"
    )

    assert "group: pages-${{ inputs.concurrency_group }}" in reusable
    assert "cancel-in-progress: false" in reusable
    for path in (PREVIEW, PRODUCTION):
        text = path.read_text(encoding="utf-8")
        assert "pages-deploy-reusable.yml" in text
