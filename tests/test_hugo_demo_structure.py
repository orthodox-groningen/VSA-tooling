from pathlib import Path


def test_hugo_demo_contains_hugo_config():
    assert Path("examples/hugo-demo/hugo.toml").exists()


def test_hugo_demo_contains_layouts():
    assert Path(
        "examples/hugo-demo/layouts/_default/baseof.html"
    ).exists()


def test_hugo_demo_contains_content_source():
    assert Path(
        "examples/hugo-demo/content-source"
    ).exists()


def test_github_actions_workflow_exists():
    assert Path(
        ".github/workflows/hugo.yml"
    ).exists()
