from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore").replace("\r\n", "\n")


def test_gitignore_marks_generated_hugo_content_as_build_output():
    text = read(ROOT / ".gitignore")
    required = [
        "generated/",
        "examples/hugo-demo/content/",
        "examples/hugo-demo/public/",
        "examples/hugo-demo/static/vsa/",
        "examples/hugo-demo/.hugo_build.lock",
    ]

    for item in required:
        assert item in text


def test_build_hugo_reads_content_source_but_updates_only_generated_content():
    text = read(SCRIPTS / "build-hugo.cmd")

    assert r"examples\hugo-demo\content-source" in text
    assert r"update-nav-placeholders.py generated\hugo\content" in text
    assert r"update-spacing-diagnostics-metadata.py generated\hugo\content\voorbeelden\rendering\spacing-diagnostiek.md" in text
    assert r"update-nav-placeholders.py examples\hugo-demo\content-source" not in text
    assert r"update-spacing-diagnostics-metadata.py examples\hugo-demo\content-source" not in text
    assert text.rstrip().endswith("endlocal")


def test_retry_cmd_is_obsolete_and_points_to_test_cmd():
    retry = SCRIPTS / "retry.cmd"
    if not retry.exists():
        return

    text = read(retry).lower()
    assert "verouderd" in text or "obsolete" in text
    assert r"scripts\test.cmd" in text


def test_known_one_time_content_mutators_are_obsolete_or_absent():
    names = [
        "apply-step68-todo-and-navigation.py",
        "revert-step68-navigation.py",
        "apply-step71-hugo-index-navigation.py",
        "apply-step75-navigation-praktijk-moved.py",
        "migrate-index-navigation-placeholders.py",
        "stabilize-hugo-navigation.py",
        "update-index-navigation-blocks.py",
        "hide-legacy-hugo-routes.py",
        "repair-vsa-image-refs.py",
        "fix-praktijk-navigation.cmd",
    ]

    for name in names:
        path = SCRIPTS / name
        if not path.exists():
            continue
        text = read(path).lower()
        assert "verouderd" in text or "obsolete" in text
        assert "wijzigt geen bestanden meer" in text or "geen bestanden" in text or name.endswith(".cmd")


def test_update_scripts_do_not_default_to_content_source():
    forbidden = ["examples/hugo-demo/content-source", "examples\\hugo-demo\\content-source"]
    for name in ["update-nav-placeholders.py", "update-spacing-diagnostics-metadata.py"]:
        text = read(SCRIPTS / name)
        for needle in forbidden:
            assert needle not in text


def test_no_tests_depend_on_obsolete_apply_scripts():
    offenders = []
    pattern = re.compile(r"apply-step\d+|repair_vsa_image_refs|update_index_navigation_blocks")
    for path in (ROOT / "tests").glob("test*.py"):
        if path.name == "test_repo_hygiene.py":
            continue
        text = read(path)
        if pattern.search(text):
            offenders.append(path.name)

    assert offenders == []
