import subprocess
import sys
from pathlib import Path


def test_publication_check_script_accepts_project_prefixed_links(tmp_path: Path):
    site = tmp_path / "site"
    (site / "vsa").mkdir(parents=True)
    (site / "voorbeelden").mkdir(parents=True)

    (site / "index.html").write_text(
        '<a href="/VSA-tooling/preview/voorbeelden/">Voorbeelden</a>'
        '<img src="/VSA-tooling/preview/vsa/demo.svg">',
        encoding="utf-8",
    )
    (site / "voorbeelden" / "index.html").write_text("<html></html>", encoding="utf-8")
    (site / "vsa" / "demo.svg").write_text("<svg></svg>", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            "scripts/check-publication-output.py",
            "--site-dir",
            str(site),
            "--url-prefix",
            "/VSA-tooling/preview/",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "OK" in result.stdout


def test_publication_check_script_rejects_missing_project_prefix(tmp_path: Path):
    site = tmp_path / "site"
    site.mkdir()
    (site / "index.html").write_text(
        '<a href="/preview/voorbeelden/">Fout</a>',
        encoding="utf-8",
    )

    result = subprocess.run(
        [
            sys.executable,
            "scripts/check-publication-output.py",
            "--site-dir",
            str(site),
            "--url-prefix",
            "/VSA-tooling/preview/",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 1
    assert "mist URL-prefix" in result.stdout


def test_publication_check_script_allows_bron_sibling_site_links(tmp_path: Path):
    """TEv2 localize maakt bron-navurls tot /bron/terms/… op hetzelfde github.io-host."""
    site = tmp_path / "site"
    site.mkdir()
    (site / "index.html").write_text(
        '<a href="/bron/terms/exporttype">exporttype</a>'
        '<a href="/VSA-tooling/preview/terminologie/">lokaal</a>',
        encoding="utf-8",
    )
    (site / "terminologie").mkdir()
    (site / "terminologie" / "index.html").write_text("<html></html>", encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            "scripts/check-publication-output.py",
            "--site-dir",
            str(site),
            "--url-prefix",
            "/VSA-tooling/preview/",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stdout
    assert "OK" in result.stdout


def test_docs_pages_preview_uses_project_preview_url_and_publication_check():
    workflow = Path(".github/workflows/docs-pages.yml").read_text(encoding="utf-8")
    reusable = Path(".github/workflows/pages-deploy-reusable.yml").read_text(
        encoding="utf-8"
    )

    assert "https://orthodox-groningen.github.io/VSA-tooling/preview/" in workflow
    assert "url_prefix=/VSA-tooling/preview/" in workflow
    assert "check-publication-output.py" in reusable
    # Feature-branch builds moeten hun eigen check-script gebruiken (niet @main).
    assert "github.sha" in reusable
    assert "vsa_tooling_ref: ${{ github.sha }}" in workflow


def test_docs_pages_production_uses_project_url_and_publication_check():
    workflow = Path(".github/workflows/docs-pages.yml").read_text(encoding="utf-8")
    reusable = Path(".github/workflows/pages-deploy-reusable.yml").read_text(
        encoding="utf-8"
    )

    assert "https://orthodox-groningen.github.io/VSA-tooling/" in workflow
    assert "url_prefix=/VSA-tooling/" in workflow
    assert "check-publication-output.py" in reusable


def test_reusable_workflow_installs_vsa_tool_from_repository():
    workflow = Path(".github/workflows/vsa-render-reusable.yml").read_text(encoding="utf-8")

    assert "workflow_call:" in workflow
    assert "git+https://github.com/orthodox-groningen/VSA-tooling.git" in workflow
    assert "vsa build-markdown" in workflow
    assert "vsa validate" in workflow
