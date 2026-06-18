from __future__ import annotations

from pathlib import Path
import shutil
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

TARGETS = [
    ROOT / "generated" / "hugo" / "content",
    ROOT / "generated" / "hugo" / "static" / "vsa",
    ROOT / "generated" / "site",
    ROOT / "examples" / "hugo-demo" / "content",
    ROOT / "examples" / "hugo-demo" / "static" / "vsa",
    ROOT / "examples" / "hugo-demo" / "public",
]


def main() -> None:
    removed = []

    for target in TARGETS:
        if target.exists():
            shutil.rmtree(target)
            removed.append(target.relative_to(ROOT))

    if removed:
        print("Verwijderd:")
        for path in removed:
            print(f"- {path}")
    else:
        print("Geen bestaande build artifacts gevonden.")


if __name__ == "__main__":
    main()
