from pathlib import Path
import re
import subprocess
import sys


SCRIPT = Path("scripts/apply-step71-hugo-index-navigation.py")
CONTENT_ROOT = Path("examples/hugo-demo/content-source")


def test_step71_script_exists():
    assert SCRIPT.exists()


def test_step71_script_runs():
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "Stap 71" in result.stdout


def test_no_old_injected_vsa_nav_blocks():
    offenders = []

    for path in CONTENT_ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        if "VSA-NAV-START" in text or "VSA-NAV-END" in text:
            offenders.append(str(path))

    assert offenders == []


def test_relevant_index_pages_exist_after_apply():
    expected = [
        CONTENT_ROOT / "_index.md",
        CONTENT_ROOT / "voorbeelden" / "_index.md",
        CONTENT_ROOT / "voorbeelden" / "praktijk" / "_index.md",
        CONTENT_ROOT / "voorbeelden" / "rendering" / "_index.md",
    ]

    for path in expected:
        if path.parent.exists():
            assert path.exists()


def test_generated_index_links_resolve_to_source_paths():
    offenders = []

    for path in CONTENT_ROOT.rglob("_index.md"):
        text = path.read_text(encoding="utf-8")

        if "Gegenereerd door scripts/apply-step71" not in text and "VSA-SITE-NAV-START" not in text:
            continue

        for link in re.findall(r"\]\(([^)]+)\)", text):
            if link.startswith(("http://", "https://", "#", "mailto:")):
                continue

            target = resolve_source_link(path.parent, link)
            if target is None:
                offenders.append(f"{path}: {link}")

    assert offenders == []


def resolve_source_link(base_dir: Path, link: str):
    clean = link.split("#", 1)[0].split("?", 1)[0]

    if clean in {"", "./"}:
        return base_dir

    target_dir = (base_dir / clean).resolve()

    try:
        target_dir.relative_to(CONTENT_ROOT.resolve())
    except ValueError:
        return None

    if target_dir.exists():
        return target_dir

    # pretty URL path foo/ maps to foo.md or foo/_index.md
    no_slash = Path(str(target_dir).rstrip("\\/"))
    candidates = [
        no_slash.with_suffix(".md"),
        no_slash / "_index.md",
    ]

    for candidate in candidates:
        if candidate.exists():
            return candidate

    return None
