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
            if (candidate / "pyproject.toml").exists() and (
                candidate / "src" / "vsa"
            ).exists():
                return candidate
        return Path(__file__).resolve().parents[1]


ROOT = find_repo_root(Path(__file__).resolve())
PUBLIC = ROOT / "examples" / "hugo-demo" / "public"


def main() -> None:
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
        print(f"Verwijderd: {PUBLIC.relative_to(ROOT)}")
    else:
        print(f"Niet aanwezig: {PUBLIC.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
