from pathlib import Path
import subprocess
import sys


MIGRATE = Path("scripts/migrate-index-navigation-placeholders.py")
UPDATE = Path("scripts/update-nav-placeholders.py")
APPLY = Path("scripts/apply-step79-explicit-nav-placeholders.py")
DOC = Path("docs/hugo-navigation-placeholders.md")
CONTENT = Path("examples/hugo-demo/content-source")


def test_step79_scripts_and_docs_exist():
    assert MIGRATE.exists()
    assert UPDATE.exists()
    assert APPLY.exists()
    assert DOC.exists()


def test_documentation_mentions_all_nav_markers():
    text = DOC.read_text(encoding="utf-8")

    for marker in [
        "VSA-NAV:HOME",
        "VSA-NAV:UP",
        "VSA-NAV:SIBLINGS",
        "VSA-NAV:CHILDREN",
        "VSA-NAV:PAGES",
    ]:
        assert marker in text


def test_migrate_index_navigation_placeholders_runs():
    result = subprocess.run(
        [sys.executable, str(MIGRATE)],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Stap 79" in result.stdout


def test_update_nav_placeholders_runs():
    result = subprocess.run(
        [sys.executable, str(UPDATE)],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "navigatie-placeholders" in result.stdout.lower()


def test_old_whole_index_generator_notes_removed_after_migration():
    offenders = []

    for index in CONTENT.rglob("_index.md"):
        text = index.read_text(encoding="utf-8")
        if "Gegenereerd door scripts/apply-step71" in text:
            offenders.append(str(index))
        if "Gegenereerd door scripts/apply-step75" in text:
            offenders.append(str(index))

    assert offenders == []


def test_index_pages_have_explicit_placeholders_after_migration():
    indexes = list(CONTENT.rglob("_index.md"))
    assert indexes

    offenders = []
    for index in indexes:
        text = index.read_text(encoding="utf-8")
        if "<!-- VSA-NAV:" not in text:
            offenders.append(str(index))

    assert offenders == []


def test_generated_nav_blocks_are_bounded():
    found = False

    for path in CONTENT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if "VSA-NAV-GENERATED:" in text:
            found = True
            assert "-START -->" in text
            assert "-END -->" in text

    assert found


def test_apply_step79_updates_build_script_if_present():
    build = Path("scripts/build-hugo.cmd")
    if not build.exists():
        return

    result = subprocess.run(
        [sys.executable, str(APPLY)],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0

    text = build.read_text(encoding="utf-8")
    assert "update-nav-placeholders.py" in text
    assert "update-index-navigation-blocks.py" not in text
