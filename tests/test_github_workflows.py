from pathlib import Path


WORKFLOW_DIR = Path(".github/workflows")
WORKFLOW_FILES = (
    "vsa-ci.yml",
    "docs-build.yml",
    "docs-pages.yml",
    "release-artifacts.yml",
    "pages-deploy-reusable.yml",
    "vsa-render-reusable.yml",
)


def test_workflows_readme_exists():
    readme = WORKFLOW_DIR / "README.md"
    assert readme.exists()
    text = readme.read_text(encoding="utf-8")
    for name in WORKFLOW_FILES:
        assert name in text


def test_each_workflow_has_header_comment():
    for name in WORKFLOW_FILES:
        text = (WORKFLOW_DIR / name).read_text(encoding="utf-8")
        assert text.startswith("#"), f"{name}: verwacht kopcommentaar"
        assert "name:" in text


def test_vsa_ci_workflow_exists():
    assert Path(".github/workflows/vsa-ci.yml").exists()


def test_docs_build_workflow_exists():
    assert Path(".github/workflows/docs-build.yml").exists()
    assert not Path(".github/workflows/site-build.yml").exists()


def test_removed_duplicate_workflows_are_gone():
    removed = (
        ".github/workflows/hugo.yml",
        ".github/workflows/build-target.yml",
        ".github/workflows/python-tests.yml",
        ".github/workflows/build-artifacts.yml",
        ".github/workflows/hugo-demo.yml",
        ".github/workflows/site-build.yml",
        ".github/workflows/pages-preview.yml",
        ".github/workflows/pages-demo.yml",
    )

    for path in removed:
        assert not Path(path).exists(), path


def test_docs_build_runs_on_push_and_pull_request():
    text = Path(".github/workflows/docs-build.yml").read_text(encoding="utf-8")

    assert "push:" in text
    assert "pull_request:" in text
    assert "mkdocs build" in text


def test_vsa_ci_uses_consumer_minimal():
    text = Path("scripts/ci.cmd").read_text(encoding="utf-8")
    assert "consumer-minimal" in text
    assert "hugo-demo" not in text


def test_vsa_ci_checks_out_bron_for_catalogus():
    text = Path(".github/workflows/vsa-ci.yml").read_text(encoding="utf-8")
    assert "repository: orthodox-groningen/bron" in text
    assert "path: vendor/bron" in text
    assert "scripts\\ci.cmd" in text


def test_docs_pages_cutover_targets():
    text = Path(".github/workflows/docs-pages.yml").read_text(encoding="utf-8")

    assert "destination_dir=preview" in text
    assert 'destination_dir="' in text or "destination_dir=" in text
    assert "https://orthodox-groningen.github.io/VSA-tooling/" in text
    assert "https://orthodox-groningen.github.io/VSA-tooling/preview/" in text
    assert "docs-preview" not in text
    assert 'destination_dir=docs"' not in text
    assert "destination_dir=docs," not in text
    assert 'echo "keep_files=true"' in text
    assert 'echo "keep_files=false"' in text
