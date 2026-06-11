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
class ValidationConfig:
    severity: dict[str, str] = field(default_factory=dict)


@dataclass
class VSAConfig:
    rendering: RenderingConfig = field(default_factory=RenderingConfig)
    hugo: HugoConfig = field(default_factory=HugoConfig)
    validation: ValidationConfig = field(default_factory=ValidationConfig)


def load_config(path: str | Path | None = None) -> VSAConfig:
    config = VSAConfig()

    if path is None:
        return config

    path = Path(path)

    if not path.exists():
        return config

    data = tomllib.loads(path.read_text(encoding="utf-8"))

    rendering = data.get("rendering", {})
    hugo = data.get("hugo", {})
    validation = data.get("validation", {})

    if "max-line-width" in rendering:
        config.rendering.max_line_width = float(rendering["max-line-width"])

    if "assets-url-prefix" in hugo:
        config.hugo.assets_url_prefix = str(hugo["assets-url-prefix"])

    if "output-mode" in hugo:
        config.hugo.output_mode = _normalize_output_mode(hugo["output-mode"])

    severity = validation.get("severity", {})

    if isinstance(severity, dict):
        config.validation.severity = {
            str(code): _normalize_severity(value)
            for code, value in severity.items()
        }

    return config


def _normalize_output_mode(value):
    value = str(value).strip().lower()

    if value not in {"img", "shortcode"}:
        raise ValueError(
            f"Onbekende output-mode: {value}. Gebruik 'img' of 'shortcode'."
        )

    return value


def _normalize_severity(value):
    value = str(value).strip().lower()

    if value not in {"error", "warning"}:
        raise ValueError(
            f"Onbekende severity: {value}. Gebruik 'error' of 'warning'."
        )

    return value
