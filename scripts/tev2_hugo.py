from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
BASE_CONFIG = ROOT / "examples" / "hugo-demo" / "terminology-config.yaml"


def posix_path(path: Path) -> str:
    return path.as_posix()


def run(command: list[str]) -> None:
    print("+ " + " ".join(command), flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


def build_config(content_root: Path, temp_dir: Path) -> Path:
    config = yaml.safe_load(BASE_CONFIG.read_text(encoding="utf-8"))
    content_pattern = posix_path(content_root)

    config["hrgt"]["input"] = [
        f"{content_pattern}/glossarium.md",
        f"{content_pattern}/terminologie/**/*.md",
    ]
    config["trrt"]["input"] = [f"{content_pattern}/**/*.md"]

    config_path = temp_dir / "terminology-config.yaml"
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
    args = parser.parse_args()

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
