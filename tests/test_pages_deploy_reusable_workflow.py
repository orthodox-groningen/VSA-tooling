from pathlib import Path


REUSABLE = Path(".github/workflows/pages-deploy-reusable.yml")
DOCS_PAGES = Path(".github/workflows/docs-pages.yml")


def test_pages_deploy_reusable_workflow_exists():
    assert REUSABLE.exists()


def test_pages_deploy_reusable_is_workflow_call():
    text = REUSABLE.read_text(encoding="utf-8")

    assert "workflow_call:" in text
    assert "artifact_name:" in text
    assert "publish_dir:" in text
    assert "url_prefix:" in text


def test_pages_deploy_reusable_uses_peaceiris_not_deploy_pages():
    text = REUSABLE.read_text(encoding="utf-8")

    assert "peaceiris/actions-gh-pages@v3" in text
    assert "publish_branch: gh-pages" in text
    assert "keep_files:" in text
    assert "actions/deploy-pages" not in text
    assert "actions/upload-pages-artifact" not in text


def test_pages_deploy_reusable_documents_pages_source_notice():
    text = REUSABLE.read_text(encoding="utf-8")

    assert "pages build and deployment" in text
    assert "Deploy from a branch" in text


def test_pages_deploy_reusable_has_concurrency_without_cancel():
    text = REUSABLE.read_text(encoding="utf-8")

    assert "cancel-in-progress: false" in text
    assert "concurrency:" in text


def test_pages_deploy_reusable_runs_publication_check():
    text = REUSABLE.read_text(encoding="utf-8")

    assert "check-publication-output.py" in text
    assert "skip_publication_check" in text


def test_pages_deploy_reusable_supports_subdirectory_and_root_deploy():
    text = REUSABLE.read_text(encoding="utf-8")

    assert "destination_dir != ''" in text
    assert "destination_dir == ''" in text


def test_docs_pages_uses_pages_deploy_reusable():
    text = DOCS_PAGES.read_text(encoding="utf-8")

    assert "pages-deploy-reusable.yml" in text
    assert "artifact_name: pages-docs-site" in text
    assert "upload-artifact@v4" in text
    assert "jobs:" in text
    assert "build:" in text
    assert "deploy:" in text
    assert "needs: build" in text


def test_docs_pages_main_deploys_root_preview_subdir():
    text = DOCS_PAGES.read_text(encoding="utf-8")

    assert 'url_prefix=/VSA-tooling/"' in text or "url_prefix=/VSA-tooling/" in text
    assert "url_prefix=/VSA-tooling/preview/" in text
    assert "destination_dir=preview" in text


def test_docs_pages_keep_files_bron_style_after_cutover():
    """main behoudt preview (true); preview vervangt schoon (false)."""
    text = DOCS_PAGES.read_text(encoding="utf-8")

    assert 'echo "keep_files=true"' in text
    assert 'echo "keep_files=false"' in text
    # Eén true (main) en één false (preview).
    assert text.count('echo "keep_files=true"') == 1
    assert text.count('echo "keep_files=false"') == 1
