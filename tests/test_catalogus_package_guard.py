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


def test_bootstrap_documents_bron_requirement():
    text = Path("scripts/bootstrap.cmd").read_text(encoding="utf-8")
    assert "vendor\\bron" in text or "vendor/bron" in text
    assert "PyPI" in text
