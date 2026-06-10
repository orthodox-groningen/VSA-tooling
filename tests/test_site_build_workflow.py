from pathlib import Path


def test_site_build_workflow_exists():
    assert Path(".github/workflows/site-build.yml").exists()


def test_site_build_workflow_detects_main_as_production():
    text = Path(".github/workflows/site-build.yml").read_text(encoding="utf-8")

    assert "GITHUB_REF" in text
    assert "refs/heads/main" in text
    assert "target=production" in text
    assert "target=preview" in text


def test_site_build_workflow_runs_on_push_and_pr():
    text = Path(".github/workflows/site-build.yml").read_text(encoding="utf-8")

    assert "push:" in text
    assert "pull_request:" in text


def test_site_build_workflow_uploads_preview_or_production_artifacts():
    text = Path(".github/workflows/site-build.yml").read_text(encoding="utf-8")

    assert "site-${{ steps.target.outputs.target }}" in text
    assert "generated-content-${{ steps.target.outputs.target }}" in text
    assert "generated-svg-${{ steps.target.outputs.target }}" in text


def test_site_build_workflow_uses_different_production_settings():
    text = Path(".github/workflows/site-build.yml").read_text(encoding="utf-8")

    assert "max_line_width=900" in text
    assert "--minify" in text
