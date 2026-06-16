from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]

CONTENT_DIRS = [
    ROOT / "examples" / "hugo-demo" / "content",
    ROOT / "examples" / "hugo-demo" / "content-source",
]

PUBLIC_DIR = ROOT / "examples" / "hugo-demo" / "public"

IMG_RE = re.compile(
    r'(<img\b[^>]*\bclass="[^"]*\bvsa-notation\b[^"]*"[^>]*\bsrc=")'
    r'([^"]*?/vsa/[^"]*?block-(\d+)\.svg)'
    r'("[^>]*>)'
)


def main() -> None:
    changed = []

    for content_dir in CONTENT_DIRS:
        if content_dir.exists():
            changed.extend(repair_markdown_tree(content_dir))

    if PUBLIC_DIR.exists():
        changed.extend(repair_public_html_tree(PUBLIC_DIR))

    print("Stap 72: VSA image refs gecontroleerd.")
    if changed:
        print("Aangepast:")
        for path in changed:
            print(f"- {path.relative_to(ROOT)}")
    else:
        print("Geen wijzigingen nodig.")


def repair_markdown_tree(content_dir: Path) -> list[Path]:
    changed = []

    for path in sorted(content_dir.rglob("*.md")):
        original = path.read_text(encoding="utf-8")
        stem = asset_stem_for_markdown(path, content_dir)
        text = rewrite_img_refs(original, stem)

        if text != original:
            path.write_text(text, encoding="utf-8")
            changed.append(path)

    return changed


def repair_public_html_tree(public_dir: Path) -> list[Path]:
    changed = []

    for path in sorted(public_dir.rglob("*.html")):
        original = path.read_text(encoding="utf-8")
        stem = asset_stem_for_public_html(path, public_dir)

        if stem is None:
            continue

        text = rewrite_img_refs(original, stem)

        if text != original:
            path.write_text(text, encoding="utf-8")
            changed.append(path)

    return changed


def rewrite_img_refs(text: str, expected_stem: str) -> str:
    def repl(match: re.Match[str]) -> str:
        prefix, _old_src, block_number, suffix = match.groups()
        return f'{prefix}/vsa/{expected_stem}-block-{block_number}.svg{suffix}'

    return IMG_RE.sub(repl, text)


def asset_stem_for_markdown(path: Path, content_dir: Path) -> str:
    rel = path.relative_to(content_dir).with_suffix("")
    parts = list(rel.parts)

    if parts and parts[-1].lower() in {"index", "_index"}:
        parts = parts[:-1]

    return "-".join(safe_slug(part) for part in parts if part)


def asset_stem_for_public_html(path: Path, public_dir: Path) -> str | None:
    rel = path.relative_to(public_dir)

    if rel.parts and rel.parts[0] == "vsa":
        return None

    if rel.name.lower() == "index.html":
        parts = rel.parent.parts
    else:
        parts = rel.with_suffix("").parts

    if not parts:
        return None

    return "-".join(safe_slug(part) for part in parts if part)


def safe_slug(value: str) -> str:
    return value.replace("_", "-").replace(" ", "-").lower()


if __name__ == "__main__":
    main()
