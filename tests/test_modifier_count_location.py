from pathlib import Path

from vsa.validation_runner import validate_file


def test_modifier_count_mismatch_points_to_scope_location(tmp_path: Path):
    path = tmp_path / "edge-cases.md"
    path.write_text(
        r"""::: vsa-notatie
[:] Scharen
jubelen en zich ver{\blij_&~&~}{\den_},
:::
""",
        encoding="utf-8",
    )

    result = validate_file(path)

    assert not result.ok

    message = result.messages[0]

    assert message.code == "VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH"
    assert message.line == 3
    assert message.column > 15
