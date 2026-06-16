from __future__ import annotations

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "examples" / "hugo-demo" / "public"

HREF_RE = re.compile(r'\bhref="([^"]+)"')
IMG_RE = re.compile(r'<img\b[^>]*\bsrc="([^"]+)"[^>]*>')


def main() -> None:
    if not PUBLIC.exists():
        print(f"Niet gevonden: {PUBLIC}")
        print("Draai eerst scripts\\build-hugo.cmd")
        raise SystemExit(2)

    offenders = []

    for html in sorted(PUBLIC.rglob("*.html")):
        text = html.read_text(encoding="utf-8", errors="ignore")

        for link in HREF_RE.findall(text):
            if should_skip_link(link):
                continue
            if not resolve_public_link(html, link):
                offenders.append(f"{html.relative_to(ROOT)} href={link}")

        for src in IMG_RE.findall(text):
            if should_skip_link(src):
                continue
            if not resolve_public_link(html, src):
                offenders.append(f"{html.relative_to(ROOT)} img={src}")

    if offenders:
        print("Kapotte links/assets:")
        for offender in offenders:
            print(f"- {offender}")
        raise SystemExit(1)

    print("Alle gecontroleerde Hugo links/assets bestaan.")


def should_skip_link(link: str) -> bool:
    return (
        link.startswith("#")
        or link.startswith("http://")
        or link.startswith("https://")
        or link.startswith("mailto:")
        or link.startswith("tel:")
        or link == ""
    )


def resolve_public_link(html: Path, link: str) -> bool:
    clean = link.split("#", 1)[0].split("?", 1)[0]

    if clean.startswith("/"):
        candidate = PUBLIC / clean.lstrip("/")
    else:
        candidate = html.parent / clean

    if candidate.exists():
        return True

    if clean.endswith("/"):
        return (candidate / "index.html").exists()

    if candidate.suffix == "":
        return (candidate / "index.html").exists()

    return False


if __name__ == "__main__":
    main()
