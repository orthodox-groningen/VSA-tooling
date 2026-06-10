from dataclasses import dataclass, field
from pathlib import Path
import tomllib


@dataclass
class RenderingConfig:
    max_line_width: float = 800.0


@dataclass
class HugoConfig:
    assets_url_prefix: str = "/vsa"
    output_mode: str = "img"


@dataclass
class VSAConfig:
    rendering: RenderingConfig = field(default_factory=RenderingConfig)
    hugo: HugoConfig = field(default_factory=HugoConfig)


def load_config(path: str | Path | None = None) -> VSAConfig:
    if path is None:
        path = Path("vsa.toml")
    else:
        path = Path(path)

    if not path.exists():
        return VSAConfig()

    data = tomllib.loads(path.read_text(encoding="utf-8"))

    rendering_data = data.get("rendering", {})
    hugo_data = data.get("hugo", {})

    output_mode = str(hugo_data.get("output-mode", "img"))

    if output_mode not in ["img", "shortcode"]:
        raise ValueError(
            "Ongeldige hugo.output-mode in vsa.toml. Gebruik 'img' of 'shortcode'."
        )

    return VSAConfig(
        rendering=RenderingConfig(
            max_line_width=float(
                rendering_data.get("max-line-width", 800.0)
            )
        ),
        hugo=HugoConfig(
            assets_url_prefix=str(
                hugo_data.get("assets-url-prefix", "/vsa")
            ),
            output_mode=output_mode,
        ),
    )
