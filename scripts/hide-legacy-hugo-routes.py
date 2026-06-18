from __future__ import annotations

from pathlib import Path
import re
import sys

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

try:
    from repo_root import find_repo_root
except Exception:
    def find_repo_root(start: Path | None = None) -> Path:
        current = (start or Path.cwd()).resolve()
        for candidate in [current, *current.parents]:
            if (candidate / "examples" / "hugo-demo").exists():
                return candidate
        return Path(__file__).resolve().parents[1]


ROOT = find_repo_root(Path(__file__).resolve())
CONTENT = ROOT / "examples" / "hugo-demo" / "content-source"

TOP_LEVEL_PRAKTIJK_LEGACY = re.compile(
    r"^(tropaar-toon-\d+|kondak-toon-\d+|zondag-toon-\d+)\.md$",
    re.IGNORECASE,
)


def main() -> None:
    if not CONTENT.exists():
        print(f"Niet gevonden: {CONTENT}")
        raise SystemExit(1)

    changed = []

    for path in sorted(CONTENT.rglob("*.md")):
        if not is_legacy_source(path):
            continue

        original = path.read_text(encoding="utf-8")
        text = ensure_frontmatter_bool(original, "draft", True)
        text = ensure_frontmatter_bool(text, "vsa_nav_exclude", True)

        if text != original:
            path.write_text(text.rstrip() + "\n", encoding="utf-8")
            changed.append(path)

    if changed:
        print("Legacy Hugo-routes verborgen:")
        for path in changed:
            print(f"- {path.relative_to(ROOT)}")
    else:
        print("Geen legacy Hugo-route wijzigingen nodig.")


def is_legacy_source(path: Path) -> bool:
    rel = path.relative_to(CONTENT)
    parts = rel.parts

    if len(parts) >= 2 and parts[0].lower() == "zondag":
        return True

    if len(parts) >= 3 and parts[0].lower() == "voorbeelden" and parts[1].lower() == "praktijk":
        return True

    if len(parts) == 2 and parts[0].lower() == "praktijk" and TOP_LEVEL_PRAKTIJK_LEGACY.match(parts[1]):
        return True

    return False


def ensure_frontmatter_bool(text: str, key: str, value: bool) -> str:
    value_text = "true" if value else "false"
    lines = text.splitlines()

    if lines and lines[0].strip() == "---":
        end = None
        for index in range(1, len(lines)):
            if lines[index].strip() == "---":
                end = index
                break

        if end is not None:
            key_re = re.compile(rf"^\s*{re.escape(key)}\s*:", re.IGNORECASE)
            for index in range(1, end):
                if key_re.match(lines[index]):
                    lines[index] = f"{key}: {value_text}"
                    return "\n".join(lines) + "\n"

            lines.insert(end, f"{key}: {value_text}")
            return "\n".join(lines) + "\n"

    return f"---\n{key}: {value_text}\n---\n\n{text}"


if __name__ == "__main__":
    main()
