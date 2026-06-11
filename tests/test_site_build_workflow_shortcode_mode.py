from pathlib import Path


def test_site_build_workflow_uses_shortcode_mode():
    text = Path(".github/workflows/site-build.yml").read_text(encoding="utf-8")

    assert "--output-mode shortcode" in text


def test_site_build_workflow_keeps_branch_aware_targets():
    text = Path(".github/workflows/site-build.yml").read_text(encoding="utf-8")

    assert "refs/heads/main" in text
    assert "target=production" in text
    assert "target=preview" in text
