"""TEv2 docs glossary alignment (bron-style glossary.md)."""

from pathlib import Path


def test_glossary_hrg_matches_saf_scopetag():
    glossary = Path("docs/glossary.md").read_text(encoding="utf-8")
    saf = Path("docs/saf.yaml").read_text(encoding="utf-8")
    assert '{% hrg="vsa-tooling" %}' in glossary
    assert "scopetag: vsa-tooling" in saf


def test_tev2_config_hrgt_targets_glossary_md():
    text = Path("docs/tev2-config.yaml").read_text(encoding="utf-8")
    assert "scopedir: ." in text
    assert '"glossary.md"' in text
    assert "terminologie/**/*.md" not in text
    assert "docs/terminologie" not in text


def test_prepare_and_docs_build_tev2_scripts_exist():
    assert Path("scripts/prepare-tev2-docs.py").exists()
    assert Path("scripts/docs-build-tev2.cmd").exists()
    assert Path("scripts/sort-glossary-table.py").exists()
    assert Path("scripts/check-tev2-termrefs.py").exists()
    assert not Path("scripts/mkdocs-glossary-index.py").exists()
    assert not Path("scripts/prepare-docs-glossary.cmd").exists()
    assert not Path("docs/terminologie/_index.template").exists()
    assert not Path("docs/terminologie/_index.md").exists()
    assert not Path("docs/terminologie/index.md").exists()


def test_mkdocs_nav_uses_glossary_md():
    text = Path("mkdocs.yml").read_text(encoding="utf-8")
    assert "Terminologie:" in text
    assert "glossary.md" in text
    assert "terminologie/index.md" not in text
    assert "terminologie/_index.md" not in text
    for workflow in (
        Path(".github/workflows/docs-pages.yml"),
        Path(".github/workflows/docs-build.yml"),
        Path("scripts/docs-build-tev2.cmd"),
    ):
        body = workflow.read_text(encoding="utf-8")
        assert "sort-glossary-table.py glossary.md" in body
        assert "mkdocs-glossary-index.py" not in body
        assert "_index.template" not in body


def test_tev2_config_uses_localize_navurl_in_hrgt_converters():
    text = Path("docs/tev2-config.yaml").read_text(encoding="utf-8")
    assert "{{localize navurl}}" in text
    assert "({{term}}.md)" not in text


def test_hrgt_converters_emit_abbr_and_alias_on_own_table_rows():
    """converter[1] must end with \\n so abbr/alias rows are not glued into one MD row."""
    text = Path("docs/tev2-config.yaml").read_text(encoding="utf-8")
    # YAML stores the trailing newline as the two chars \n inside the quoted string.
    assert "converter[1]:" in text
    assert ' |\\n"' in text or " |\\n'" in text or '|\\n"' in text
    assert "glossaryAbbr" in text
    assert "glossaryAlias" in text
    assert "Afkorting van" in text
    assert "Alias voor" in text


def test_saf_imports_bron_terms_before_local_with_exclude():
    text = Path("docs/saf.yaml").read_text(encoding="utf-8")
    assert "scopetag: bron" in text
    termselection = []
    in_termselection = False
    for ln in text.splitlines():
        if ln.strip() == "termselection:":
            in_termselection = True
            continue
        if not in_termselection:
            continue
        stripped = ln.strip()
        if stripped.startswith("- "):
            termselection.append(stripped[2:].strip().strip('"'))
        elif stripped.startswith("#") or not stripped:
            continue
        else:
            break
    assert termselection == ["*@bron", "*", "-excludeFromMRG[yes]"]


def test_docs_build_tev2_always_runs_mrg_import():
    text = Path("scripts/docs-build-tev2.cmd").read_text(encoding="utf-8")
    assert "mrg-import" in text
    assert "Skipping mrg-import locally" not in text
    assert 'TEV2_RUN_IMPORT"=="1"' not in text
