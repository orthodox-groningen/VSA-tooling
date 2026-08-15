# Versionering

Deze draft volgt een eigen versielabel los van VSA 1.0.

| Label      | Betekenis                                      |
| ---------- | ---------------------------------------------- |
| `draft-v0` | Eerste getoetste specificatie + voorbeelden    |
| `draft-vN` | Latere breaking of clarificerende drafts       |
| `1.0`      | Pas na integratie in `docs/specification/`     |

Het veld `spec_version` in een template-YAML moet overeenkomen met het label
van de specificatie waartegen het is geschreven (nu: `draft-v0`).

Breaking wijzigingen aan YAML-vorm of semantiek verhogen het draft-nummer en
worden in `open-points.md` / release notes van de branch vermeld.
