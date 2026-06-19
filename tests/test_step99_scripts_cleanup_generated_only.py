from pathlib import Path


def read(path: str) -> str:
    return Path("scripts", path).read_text(encoding="utf-8").replace("\r\n", "\n")


def test_build_hugo_does_not_update_content_source_directly():
    text = read("build-hugo.cmd")

    assert "update-nav-placeholders.py generated\\hugo\\content" in text
    assert "update-spacing-diagnostics-metadata.py generated\\hugo\\content\\voorbeelden\\rendering\\spacing-diagnostiek.md" in text
    assert "update-nav-placeholders.py examples\\hugo-demo\\content-source" not in text
    assert "update-spacing-diagnostics-metadata.py examples\\hugo-demo\\content-source" not in text


def test_retry_cmd_is_obsolete_if_present():
    path = Path("scripts/retry.cmd")
    if path.exists():
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
        assert "obsolete" in text or "verouderd" in text
