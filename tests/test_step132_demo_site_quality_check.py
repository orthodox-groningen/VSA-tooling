import subprocess
import sys
from pathlib import Path

SCRIPT = Path("scripts/check-demo-site-quality.py")


def test_demo_site_quality_script_exists():
    assert SCRIPT.exists()


def test_demo_site_quality_script_accepts_valid_preview_project_links(tmp_path: Path):
    site = tmp_path / "site"
    (site / "voorbeelden").mkdir(parents=True)
    (site / "vsa").mkdir(parents=True)
    (site / "index.html").write_text(
        '<a href="/VSA-tooling/preview/">Home</a>'
        '<a href="/VSA-tooling/preview/voorbeelden/">Voorbeelden</a>'
        '<img src="/VSA-tooling/preview/vsa/demo.svg">',
        encoding="utf-8",
    )
    (site / "voorbeelden" / "index.html").write_text("<html></html>", encoding="utf-8")
    (site / "vsa" / "demo.svg").write_text("<svg></svg>", encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--site-dir", str(site), "--mode", "preview"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "OK" in result.stdout


def test_demo_site_quality_script_rejects_root_preview_links(tmp_path: Path):
    site = tmp_path / "site"
    site.mkdir()
    (site / "index.html").write_text('<a href="/preview/">Fout</a>', encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--site-dir", str(site), "--mode", "preview"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 1
    assert "root-preview link" in result.stdout or "mist verwachte prefix" in result.stdout


def test_demo_site_quality_script_rejects_missing_internal_file(tmp_path: Path):
    site = tmp_path / "site"
    site.mkdir()
    (site / "index.html").write_text('<a href="ontbreekt/">Ontbreekt</a>', encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--site-dir", str(site), "--mode", "preview"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 1
    assert "ontbrekend bestand" in result.stdout
