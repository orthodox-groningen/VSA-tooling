from pathlib import Path


def test_vsa_ci_workflow_exists():
    assert Path(".github/workflows/vsa-ci.yml").exists()


def test_site_build_workflow_exists():
    assert Path(".github/workflows/site-build.yml").exists()


def test_removed_duplicate_workflows_are_gone():
    removed = (
        ".github/workflows/hugo.yml",
        ".github/workflows/build-target.yml",
        ".github/workflows/python-tests.yml",
        ".github/workflows/build-artifacts.yml",
        ".github/workflows/hugo-demo.yml",
    )

    for path in removed:
        assert not Path(path).exists(), path


def test_site_build_runs_on_push_and_pull_request():
    text = Path(".github/workflows/site-build.yml").read_text(encoding="utf-8")

    assert "push:" in text
    assert "pull_request:" in text
