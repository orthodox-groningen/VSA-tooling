from vsa.diagnostics import DiagnosticCollection


def test_add_diagnostic():
    diagnostics = DiagnosticCollection()

    diagnostics.add(
        code="TEST",
        message_nl="Testmelding",
        line=1,
        column=5,
    )

    assert diagnostics.has_errors()

    assert diagnostics.items[0].code == "TEST"
