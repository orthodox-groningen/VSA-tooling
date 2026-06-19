from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))


def main() -> None:
    try:
        from vsa.text_metrics import DEFAULT_FONT_FAMILY, get_font_metrics, using_real_font_metrics
    except Exception as exc:
        print("FOUT: fontmetrics konden niet worden geladen.")
        print(str(exc))
        raise SystemExit(1)

    metrics = get_font_metrics(20, DEFAULT_FONT_FAMILY)
    print("Font metrics check:")
    print(f"font family  : {DEFAULT_FONT_FAMILY}")
    print(f"backend      : {metrics.backend}")
    print(f"real metrics : {using_real_font_metrics()}")

    if not using_real_font_metrics():
        print()
        print("FOUT: real font metrics zijn niet actief.")
        print("Controleer:")
        print("- .venv\\Scripts\\python.exe wordt gebruikt")
        print("- Pillow is geïnstalleerd in de venv")
        print("- assets\\fonts\\DejaVuSans.ttf bestaat")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
