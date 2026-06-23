from pathlib import Path


PREVIEW = Path(".github/workflows/pages-preview.yml")
PRODUCTION = Path(".github/workflows/pages-demo.yml")


def test_preview_workflow_deploys_preview_directory_to_gh_pages():
    text = PREVIEW.read_text(encoding="utf-8")

    assert "peaceiris/actions-gh-pages@v3" in text
    assert "publish_branch: gh-pages" in text
    assert "destination_dir: preview" in text
    assert "keep_files: true" in text


def test_preview_workflow_uses_preview_baseurl():
    text = PREVIEW.read_text(encoding="utf-8")

    assert '--baseURL "https://orthodox-groningen.github.io/VSA-tooling/preview/"' in text


def test_production_workflow_remains_manual():
    text = PRODUCTION.read_text(encoding="utf-8")

    assert "workflow_dispatch:" in text
    assert "push:" not in text


def test_production_workflow_deploys_root_to_gh_pages():
    text = PRODUCTION.read_text(encoding="utf-8")

    assert "peaceiris/actions-gh-pages@v3" in text
    assert "publish_branch: gh-pages" in text
    assert "publish_dir: generated/site" in text
    assert "destination_dir: preview" not in text


def test_workflows_do_not_use_deploy_pages_artifacts():
    assert "actions/deploy-pages" not in PREVIEW.read_text(encoding="utf-8")
    assert "actions/deploy-pages" not in PRODUCTION.read_text(encoding="utf-8")
