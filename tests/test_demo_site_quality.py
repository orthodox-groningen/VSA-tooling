from pathlib import Path

from vsa.validation_runner import validate_path


def test_hugo_demo_structure_exists():
    assert Path("examples/hugo-demo").exists()


def test_hugo_demo_has_content_source():
    assert Path("examples/hugo-demo/content-source").exists()


def test_hugo_demo_has_layouts():
    assert Path("examples/hugo-demo/layouts").exists()


def test_hugo_demo_has_static_directory():
    assert Path("examples/hugo-demo/static").exists()


def test_hugo_demo_content_validates():
    result = validate_path("examples/hugo-demo/content-source")

    assert result.ok, [message.message_nl for message in result.messages]
