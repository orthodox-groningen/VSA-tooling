"""Parochie-lokaal zangmateriaal in hugo-demo content-source."""

from pathlib import Path

from vsa.markdown_builder import build_markdown_site
from vsa.validation_runner import validate_path

HUGO_CONTENT = Path("examples/hugo-demo/content-source")
LOKAAL_VSA = (
    HUGO_CONTENT
    / "lokaal/antifoon-1-weekdagen/liturgikon-weekdagen/hemelum/repr/hemelum.vsa"
)
HEMELUM_MD = HUGO_CONTENT / "praktijk/weekdagen/antifonen-hemelum.md"


def test_lokaal_hemelum_vsa_exists():
    assert LOKAAL_VSA.is_file()


def test_lokaal_manifest_files_exist():
    base = HUGO_CONTENT / "lokaal/antifoon-1-weekdagen/liturgikon-weekdagen"
    assert (base / "variant.yaml").is_file()
    assert (base / "hemelum/uitvoeringsvorm.yaml").is_file()


def test_validate_content_source_includes_lokaal():
    result = validate_path(HUGO_CONTENT)
    assert result.ok, [m.message_nl for m in result.messages if not result.ok]


def test_antifonen_hemelum_references_lokaal_include():
    text = HEMELUM_MD.read_text(encoding="utf-8")
    assert "lokaal/antifoon-1-weekdagen" in text
    assert ":::include svg" in text
    assert "hemelum.vsa" in text


def test_build_markdown_generates_svg_for_lokaal_include(tmp_path: Path):
    input_dir = tmp_path / "content-source"
    output_dir = tmp_path / "content-generated"
    assets_dir = tmp_path / "static" / "vsa"

    page_dir = input_dir / "praktijk" / "weekdagen"
    page_dir.mkdir(parents=True)
    vsa_src = (
        input_dir
        / "lokaal/antifoon-1-weekdagen/liturgikon-weekdagen/hemelum/repr/hemelum.vsa"
    )
    vsa_src.parent.mkdir(parents=True)
    vsa_src.write_text(LOKAAL_VSA.read_text(encoding="utf-8"), encoding="utf-8")

    (page_dir / "demo.md").write_text(
        ':::include svg "../../lokaal/antifoon-1-weekdagen/liturgikon-weekdagen/hemelum/repr/hemelum.vsa":::\n',
        encoding="utf-8",
    )

    result = build_markdown_site(input_dir, output_dir, assets_dir)

    assert len(result.svg_files) == 1
    rewritten = (output_dir / "praktijk" / "weekdagen" / "demo.md").read_text(encoding="utf-8")
    assert '<img class="vsa-notation"' in rewritten
