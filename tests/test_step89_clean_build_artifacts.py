from pathlib import Path


BUILD = Path("scripts/build-hugo.cmd")
CLEAN = Path("scripts/clean-hugo-build-artifacts.py")


def test_clean_build_script_exists():
    assert CLEAN.exists()


def test_build_hugo_cmd_is_compact():
    text = BUILD.read_text(encoding="utf-8").replace("\r\n", "\n")
    assert "\n\n\n" not in text


def test_build_hugo_cmd_has_safe_hugo_block():
    lines = BUILD.read_text(encoding="utf-8").splitlines()

    for index, line in enumerate(lines):
        if line.strip() == "hugo ^":
            block = "\n".join(lines[index:index + 4])
            assert "python scripts" not in block
            assert "--source examples\\hugo-demo ^" in block
            assert "--contentDir ..\\..\\generated\\hugo\\content ^" in block
            assert "--destination ..\\..\\generated\\site" in block
            return

    raise AssertionError("hugo ^ block not found")


def test_build_hugo_cmd_does_not_call_linkchecker_yet():
    text = BUILD.read_text(encoding="utf-8")
    assert "check-hugo-links-and-assets.py" not in text
    assert "regenerate-missing-vsa-images.py" not in text


def test_build_hugo_cmd_refreshes_public_from_generated_site():
    text = BUILD.read_text(encoding="utf-8")
    assert "xcopy /e /i /y generated\\site examples\\hugo-demo\\public >nul" in text
