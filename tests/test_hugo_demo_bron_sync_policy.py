"""Zorg dat hugo-demo builds overal bron-sync doen vóór build-markdown."""

from __future__ import annotations

from pathlib import Path

HUGO_DEMO_CONTENT = "examples/hugo-demo/content-source"

# Workflows die hugo-demo content bouwen of scripts\\ci.cmd aanroepen.
HUGO_DEMO_BUILD_WORKFLOWS = (
    "pages-demo.yml",
    "pages-preview.yml",
    "release-artifacts.yml",
    "site-build.yml",
    "vsa-ci.yml",
)

# Lokale scripts die build-markdown op hugo-demo draaien.
HUGO_DEMO_BUILD_SCRIPTS = (
    "scripts/ci.cmd",
    "scripts/build-hugo.cmd",
    "scripts/build-artifacts.cmd",
    "scripts/build-preview.cmd",
    "scripts/build-production.cmd",
    "scripts/serve-hugo.cmd",
)

SYNC_MARKERS = ("sync_bron_zondagen", "sync-bron-zondagen")
BRON_CHECKOUT_MARKER = "orthodox-groningen/bron"


def _uses_hugo_demo_build(text: str) -> bool:
    if "ci.cmd" in text:
        return True
    if HUGO_DEMO_CONTENT not in text:
        return False
    return "build-markdown" in text


def _has_sync_before_build(text: str) -> bool:
    if not any(marker in text for marker in SYNC_MARKERS):
        return False
    sync_at = min(text.find(marker) for marker in SYNC_MARKERS if marker in text)
    build_at = text.find("build-markdown")
    if build_at == -1:
        return True
    return sync_at < build_at


def test_hugo_demo_workflows_checkout_bron_and_sync_before_build():
    errors: list[str] = []

    for name in HUGO_DEMO_BUILD_WORKFLOWS:
        path = Path(".github/workflows") / name
        text = path.read_text(encoding="utf-8")
        if not _uses_hugo_demo_build(text):
            continue
        if BRON_CHECKOUT_MARKER not in text:
            errors.append(f"{name}: geen checkout van {BRON_CHECKOUT_MARKER}")
            continue
        workflow_sync = any(marker in text for marker in SYNC_MARKERS)
        ci_sync = False
        if "ci.cmd" in text:
            ci_text = Path("scripts/ci.cmd").read_text(encoding="utf-8")
            ci_sync = any(marker in ci_text for marker in SYNC_MARKERS)
        if not workflow_sync and not ci_sync:
            errors.append(f"{name}: geen sync_bron vóór build")
        elif workflow_sync and not _has_sync_before_build(text):
            errors.append(f"{name}: sync staat na build-markdown")

    assert not errors, "\n".join(errors)


def test_hugo_demo_build_scripts_sync_before_build_markdown():
    errors: list[str] = []

    for rel in HUGO_DEMO_BUILD_SCRIPTS:
        path = Path(rel)
        text = path.read_text(encoding="utf-8")
        if "build-markdown" not in text or HUGO_DEMO_CONTENT not in text.replace("\\", "/"):
            continue
        if not any(marker in text for marker in SYNC_MARKERS):
            errors.append(f"{rel}: geen sync-bron stap")
            continue
        if not _has_sync_before_build(text.replace("\\", "/")):
            errors.append(f"{rel}: sync staat na build-markdown")

    assert not errors, "\n".join(errors)


def test_sync_bron_script_exists():
    assert Path("scripts/sync_bron_zondagen.py").is_file()
    assert Path("scripts/sync-bron-zondagen.cmd").is_file()
