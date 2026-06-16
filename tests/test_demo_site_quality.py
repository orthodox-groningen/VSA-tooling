from pathlib import Path


def test_hugo_demo_structure_exists():
    assert Path("examples/hugo-demo").exists()


def test_hugo_demo_has_content_source():
    assert Path("examples/hugo-demo/content-source").exists()


def test_hugo_demo_has_layouts():
    assert Path("examples/hugo-demo/layouts").exists()


def test_hugo_demo_has_static_directory():
    assert Path("examples/hugo-demo/static").exists()


def test_hugo_demo_practice_files_are_checked_separately():
    assert Path("examples/hugo-demo/content-source").exists()
    assert Path("examples/hugo-demo/content-source/praktijk").exists()
