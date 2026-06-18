
from pathlib import Path


BUILD = Path("scripts/build-hugo.cmd")


def test_build_hugo_cmd_exists():
    assert BUILD.exists()


def test_build_hugo_cmd_has_no_excessive_blank_lines():
    text = BUILD.read_text(encoding="utf-8")
    assert "\n\n\n" not in text.replace("\r\n", "\n")


def test_build_hugo_cmd_does_not_insert_python_inside_hugo_command():
    lines = BUILD.read_text(encoding="utf-8").splitlines()

    for index, line in enumerate(lines):
        if line.strip() == "hugo ^":
            block = "\n".join(lines[index:index + 5])
            assert "python scripts" not in block
            assert "--source examples\\hugo-demo ^" in block
            assert "--contentDir ..\\..\\generated\\hugo\\content ^" in block
            assert "--destination ..\\..\\generated\\site" in block
            return

    raise AssertionError("hugo ^ block not found")


def test_linkchecker_is_not_called_from_build_hugo_yet():
    text = BUILD.read_text(encoding="utf-8")
    assert "check-hugo-links-and-assets.py" not in text
    assert "regenerate-missing-vsa-images.py" not in text
