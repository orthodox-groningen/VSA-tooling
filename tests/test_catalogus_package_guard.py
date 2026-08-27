"""Guard: catalogus moet uit orthodox-ronl/bron komen, niet PyPI-naamgenoot."""

from pathlib import Path


def test_catalogus_exposes_zoek_api():
    from catalogus import ZoekContext, zoek_met_roots

    assert ZoekContext is not None
    assert callable(zoek_met_roots)


def test_catalogus_is_not_pypi_breezy_registry():
    import catalogus

    # PyPI "catalogus" (Breezy) heeft Registry en geen ZoekContext.
    assert not hasattr(catalogus, "Registry")
    assert hasattr(catalogus, "ZoekContext")


def test_ensure_installs_catalogus_from_bron():
    text = Path("scripts/_ensure.py").read_text(encoding="utf-8")
    assert "vendor" in text
    assert "bron" in text
    assert "catalogus" in text
