"""TEv2 docs glossary alignment."""

from pathlib import Path


def test_terminologie_hrg_matches_saf_scopetag():
    template = Path("docs/terminologie/_index.template").read_text(encoding="utf-8")
    saf = Path("docs/saf.yaml").read_text(encoding="utf-8")
    assert '{% hrg="vsa-tooling" %}' in template
    assert "scopetag: vsa-tooling" in saf


def test_tev2_config_runs_from_generated_docs_root():
    text = Path("docs/tev2-config.yaml").read_text(encoding="utf-8")
    assert "scopedir: ." in text
    assert "terminologie/**/*.md" in text
    assert "docs/terminologie" not in text


def test_prepare_and_docs_build_tev2_scripts_exist():
    assert Path("scripts/prepare-tev2-docs.py").exists()
    assert Path("scripts/docs-build-tev2.cmd").exists()
    assert Path("scripts/sort-glossary-table.py").exists()
    assert Path("scripts/check-tev2-termrefs.py").exists()


def test_saf_imports_bron_scope():
    text = Path("docs/saf.yaml").read_text(encoding="utf-8")
    assert '"*@bron"' in text or "*@bron" in text
    assert "scopetag: bron" in text
