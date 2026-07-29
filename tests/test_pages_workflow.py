from pathlib import Path


WORKFLOW = Path(".github/workflows/pages-demo.yml")


def test_pages_workflow_exists():
    assert WORKFLOW.exists()


def test_pages_workflow_is_manual_only():
    text = WORKFLOW.read_text(encoding="utf-8")

    assert "workflow_dispatch:" in text
    assert "push:" not in text


def test_pages_workflow_deploys_production_root_to_gh_pages():
    text = WORKFLOW.read_text(encoding="utf-8")
    reusable = Path(".github/workflows/pages-deploy-reusable.yml").read_text(
        encoding="utf-8"
    )

    assert "pages-deploy-reusable.yml" in text
    assert "artifact_name: pages-production-site" in text
    assert "peaceiris/actions-gh-pages@v3" in reusable
    assert "publish_branch: gh-pages" in reusable
    assert "destination_dir: preview" not in text


def test_pages_workflow_preserves_existing_gh_pages_files():
    reusable = Path(".github/workflows/pages-deploy-reusable.yml").read_text(
        encoding="utf-8"
    )

    assert "keep_files:" in reusable


def test_pages_workflow_updates_navigation_before_terminology_generation():
    text = WORKFLOW.read_text(encoding="utf-8")

    navigation = "python scripts/update-nav-placeholders.py generated/hugo/content"
    terminology = "python scripts/tev2_hugo.py --content-root generated/hugo/content"
    assert navigation in text
    assert text.index(navigation) < text.index(terminology)
