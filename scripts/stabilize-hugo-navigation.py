from __future__ import annotations

from pathlib import Path
import re
import shutil
import subprocess
import sys

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from repo_root import find_repo_root


ROOT = find_repo_root(Path(__file__).resolve())
CONTENT_ROOT = ROOT / "examples" / "hugo-demo" / "content-source"
OBSOLETE_EXAMPLES_EXAMPLES = ROOT / "examples" / "examples"

OLD_GENERATOR_NOTES = [
    "<!-- Gegenereerd door scripts/apply-step71-hugo-index-navigation.py -->",
    "<!-- Gegenereerd door scripts/apply-step75-navigation-praktijk-moved.py -->",
]

OLD_BLOCKS = [
    re.compile(r"\n*<!-- VSA-INDEX-NAV-START -->.*?<!-- VSA-INDEX-NAV-END -->\n*", re.DOTALL),
    re.compile(r"\n*<!-- VSA-SITE-NAV-START -->.*?<!-- VSA-SITE-NAV-END -->\n*", re.DOTALL),
    re.compile(r"\n*<!-- VSA-NAV-START -->.*?<!-- VSA-NAV-END -->\n*", re.DOTALL),
]


def main() -> None:
    if not CONTENT_ROOT.exists():
        print(f"Niet gevonden: {CONTENT_ROOT}")
        raise SystemExit(1)

    changed = []

    for path in sorted(CONTENT_ROOT.rglob("*.md")):
        original = path.read_text(encoding="utf-8")
        text = clean_old_navigation_artifacts(original)

        if path.name.lower() == "_index.md":
            text = ensure_index_placeholders(path, text)

        if path == CONTENT_ROOT / "zondag" / "_index.md":
            text = ensure_nav_exclude_frontmatter(text)

        if text != original:
            path.write_text(text.rstrip() + "\n", encoding="utf-8")
            changed.append(path)

    if OBSOLETE_EXAMPLES_EXAMPLES.exists():
        shutil.rmtree(OBSOLETE_EXAMPLES_EXAMPLES)
        print(f"Verwijderd: {OBSOLETE_EXAMPLES_EXAMPLES.relative_to(ROOT)}")

    run_script(ROOT / "scripts" / "update-nav-placeholders.py")

    print("Stap 82: Hugo navigatie gestabiliseerd.")
    if changed:
        print("Aangepaste content:")
        for path in changed:
            print(f"- {path.relative_to(ROOT)}")
    else:
        print("Geen contentwijzigingen nodig.")


def clean_old_navigation_artifacts(text: str) -> str:
    for note in OLD_GENERATOR_NOTES:
        text = text.replace(note, "")
    for pattern in OLD_BLOCKS:
        text = pattern.sub("\n", text)
    return re.sub(r"\n{4,}", "\n\n\n", text)


def ensure_index_placeholders(path: Path, text: str) -> str:
    if "<!-- VSA-NAV:" in text:
        return text
    return insert_after_first_heading(text, placeholder_block_for_index(path))


def placeholder_block_for_index(path: Path) -> str:
    lines = []
    if path.parent != CONTENT_ROOT:
        lines.extend([
            "<!-- VSA-NAV:HOME -->",
            "<!-- VSA-NAV:UP -->",
            "",
            "<!-- VSA-NAV:SIBLINGS -->",
            "",
        ])
    lines.extend([
        "<!-- VSA-NAV:CHILDREN -->",
        "",
        "<!-- VSA-NAV:PAGES -->",
    ])
    return "\n".join(lines)


def ensure_nav_exclude_frontmatter(text: str) -> str:
    if "vsa_nav_exclude:" in text:
        return text

    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        for index in range(1, len(lines)):
            if lines[index].strip() == "---":
                lines.insert(index, "vsa_nav_exclude: true")
                return "\n".join(lines) + "\n"

    return "---\nvsa_nav_exclude: true\n---\n\n" + text


def insert_after_first_heading(text: str, block: str) -> str:
    lines = text.splitlines()
    in_frontmatter = bool(lines and lines[0].strip() == "---")

    for index, line in enumerate(lines):
        if in_frontmatter and index > 0 and line.strip() == "---":
            in_frontmatter = False
            continue

        if not in_frontmatter and line.startswith("# "):
            return "\n".join(lines[: index + 1]) + "\n\n" + block + "\n\n" + "\n".join(lines[index + 1:])

    return block + "\n\n" + text


def run_script(script: Path) -> None:
    result = subprocess.run([sys.executable, str(script)], cwd=ROOT, text=True)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()
