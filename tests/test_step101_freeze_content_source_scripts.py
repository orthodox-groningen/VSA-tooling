from pathlib import Path
import re


SCRIPTS = Path("scripts")


FORBIDDEN_WRITES = [
    "examples/hugo-demo/content-source",
    "examples\\hugo-demo\\content-source",
]


def read_script(name: str) -> str:
    return (SCRIPTS / name).read_text(encoding="utf-8", errors="ignore")


def test_build_hugo_has_no_trailing_commands_after_endlocal():
    text = read_script("build-hugo.cmd").replace("\r\n", "\n")
    assert text.rstrip().endswith("endlocal")
    assert "endlocal\npython" not in text
    assert "update-nav-placeholders.py generated\\hugo\\content" in text


def test_retry_cmd_is_obsolete():
    text = read_script("retry.cmd").lower()
    assert "verouderd" in text
    assert "scripts\\test.cmd" in text


def test_known_content_source_mutators_are_obsolete():
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
    ]

    for name in names:
        text = read_script(name).lower()
        assert "verouderd" in text
        assert "wijzigt geen bestanden meer" in text


def test_update_helpers_do_not_default_to_content_source():
    for name in ["update-nav-placeholders.py", "update-spacing-diagnostics-metadata.py"]:
        text = read_script(name)
        for forbidden in FORBIDDEN_WRITES:
            assert forbidden not in text


def test_marker_only_update_preserves_manual_markdown(tmp_path):
    import importlib.util
    import sys

    script = SCRIPTS / "update-nav-placeholders.py"
    spec = importlib.util.spec_from_file_location("update_nav_placeholders", script)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    root = tmp_path / "content"
    directory = root / "praktijk" / "weekdagen"
    directory.mkdir(parents=True)
    page = directory / "_index.md"
    page.write_text(
        """---
title: "Weekdagen"
---

| [Home](../../) | [Omhoog](../) |

## Antifonen

- [Antifonen - weekdagen](antifonen/)

<!-- VSA-NAV:PAGES -->
<!-- VSA-NAV-GENERATED:PAGES-START -->
oud
<!-- VSA-NAV-GENERATED:PAGES-END -->
""",
        encoding="utf-8",
    )
    (directory / "maandag.md").write_text('---\ntitle: "Maandag"\n---\n', encoding="utf-8")

    updated = module.update_file_text(page.read_text(encoding="utf-8"), page, root)

    assert 'title: "Weekdagen"' in updated
    assert "| [Home](../../) | [Omhoog](../) |" in updated
    assert "## Antifonen" in updated
    assert "- [Antifonen - weekdagen](antifonen/)" in updated
    assert "oud" not in updated
    assert "- [Maandag](maandag/)" in updated
