from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import urlparse

import yaml


ROOT = Path(__file__).resolve().parents[1]
BASE_CONFIG = ROOT / "examples" / "hugo-demo" / "tev2-config.yaml"
GLOSSARY_DIR = ROOT / "examples" / "hugo-demo" / "tev2-glossaries"


def posix_path(path: Path) -> str:
    return path.as_posix()


def run(command: list[str]) -> None:
    print("+ " + " ".join(command), flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


def normalize_url_prefix(prefix: str) -> str:
    if not prefix.startswith("/"):
        prefix = "/" + prefix
    if not prefix.endswith("/"):
        prefix += "/"
    return prefix


def prefixed_navurl(navurl: str, url_prefix: str) -> str:
    parsed = urlparse(navurl)
    path = parsed.path if parsed.scheme else navurl
    path = "/" + path.lstrip("/")
    if url_prefix == "/":
        prefixed_path = path
    else:
        prefixed_path = f"{url_prefix.rstrip('/')}{path}"
    return f"http://localhost:1313{prefixed_path}"


def rewrite_mrg_navurls(url_prefix: str) -> None:
    for path in sorted(GLOSSARY_DIR.glob("mrg.vsa*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        changed = False
        for entry in data.get("entries", []):
            navurl = entry.get("navurl")
            if not navurl:
                continue
            updated = prefixed_navurl(navurl, url_prefix)
            if updated != navurl:
                entry["navurl"] = updated
                changed = True
        if changed:
            path.write_text(
                yaml.safe_dump(data, sort_keys=False, allow_unicode=True),
                encoding="utf-8",
            )


def build_config(content_root: Path, temp_dir: Path) -> Path:
    config = yaml.safe_load(BASE_CONFIG.read_text(encoding="utf-8"))
    content_pattern = posix_path(content_root)

    config["hrgt"]["input"] = [
        f"{content_pattern}/glossarium.md",
        f"{content_pattern}/terminologie/**/*.md",
    ]
    config["trrt"]["input"] = [f"{content_pattern}/**/*.md"]

    config_path = temp_dir / "tev2-config.yaml"
    config_path.write_text(
        yaml.safe_dump(config, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    return config_path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run TEv2 glossary generation and TermRef resolution for Hugo output."
    )
    parser.add_argument(
        "--content-root",
        type=Path,
        default=Path("generated/hugo/content"),
        help="Generated Hugo Markdown content root. Defaults to generated/hugo/content.",
    )
    parser.add_argument(
        "--url-prefix",
        default="/",
        help="Public URL path prefix for generated TEv2 links. Defaults to /.",
    )
    args = parser.parse_args()
    url_prefix = normalize_url_prefix(args.url_prefix)

    content_root = args.content_root
    if not content_root.is_absolute():
        content_root = ROOT / content_root
    content_root = content_root.resolve()

    if not content_root.is_dir():
        print(f"ERROR: generated Hugo content root not found: {content_root}", file=sys.stderr)
        return 1

    generated_root = ROOT / "generated"
    generated_root.mkdir(exist_ok=True)

    npx = shutil.which("npx.cmd") or shutil.which("npx")
    if not npx:
        print("ERROR: npx not found. Run npm install/npm ci first.", file=sys.stderr)
        return 1

    with tempfile.TemporaryDirectory(prefix="tev2-hugo-", dir=generated_root) as temp_name:
        config_path = build_config(content_root.relative_to(ROOT), Path(temp_name))

        print()
        print("=== TEv2 terminology for Hugo demo ===")
        print()
        print("[TEv2 1/4] Generate machine-readable glossary")
        run([npx, "mrgt", "-c", str(config_path)])
        rewrite_mrg_navurls(url_prefix)

        print()
        print("[TEv2 2/4] Generate human-readable glossary fragments")
        run([npx, "hrgt", "-c", str(config_path)])

        print()
        print("[TEv2 3/4] Resolve term references in generated Hugo markdown")
        run([npx, "trrt", "-c", str(config_path)])

        print()
        print("[TEv2 4/4] Verify all generated TermRefs were resolved")
        run([sys.executable, "scripts/check-tev2-termrefs.py", str(content_root)])

    print()
    print("TEv2 processing complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
