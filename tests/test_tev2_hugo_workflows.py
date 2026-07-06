from pathlib import Path
import re


HUGO_WORKFLOWS = [
    ".github/workflows/pages-demo.yml",
    ".github/workflows/pages-preview.yml",
    ".github/workflows/site-build.yml",
]


def test_tev2_hugo_script_exists():
    assert Path("scripts/tev2_hugo.py").exists()


def test_hugo_workflows_install_and_run_tev2_before_hugo_build():
    for workflow in HUGO_WORKFLOWS:
        text = Path(workflow).read_text(encoding="utf-8")

        assert "npm ci" in text
        assert "scripts/tev2_hugo.py" in text
        hugo_command = re.search(r"(?m)^\s+hugo\s", text)
        assert hugo_command is not None
        assert text.index("scripts/tev2_hugo.py") < hugo_command.start()


def test_pages_workflows_pass_public_url_prefix_to_tev2():
    preview = Path(".github/workflows/pages-preview.yml").read_text(encoding="utf-8")
    production = Path(".github/workflows/pages-demo.yml").read_text(encoding="utf-8")

    assert (
        "python scripts/tev2_hugo.py --content-root generated/preview/content "
        "--url-prefix /VSA-tooling/preview/"
    ) in preview
    assert (
        "python scripts/tev2_hugo.py --content-root generated/hugo/content "
        "--url-prefix /VSA-tooling/"
    ) in production
