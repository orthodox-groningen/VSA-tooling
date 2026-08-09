# Specificatie vsa-templates (draft)

**Status:** draft v0 (getoetst met voorbeelden + schema-toets; nog niet geïntegreerd
in de normatieve VSA 1.0-spec).

Deze map beschrijft **vsa-templates**: een YAML-formaat voor formulematige
melodieën (tropaar, stichier, vers, …) met frasen, herhaling, reciteertonnen,
optionele noten, ankers en SATB-posities.

## Relatie tot VSA 1.0

| Map                                              | Rol                                            |
| ------------------------------------------------ | ---------------------------------------------- |
| [`docs/specification/`](../specification/)       | Normatieve VSA 1.0 (tekst + relatieve melodie) |
| **`docs/specification-vsa-templates/`** (deze)   | Draft specificatie voor melodietemplates       |

Integratiepad: wanneer draft v0 stabiel is en glossarytermen in **bron** staan,
verhuizen relevante documenten naar `docs/specification/` (of een subsectie
daarvan) en opnemen in MkDocs-nav. Tot die tijd staat deze map in `not_in_nav`.

## Documenten

| Document                                                   | Inhoud                                              |
| ---------------------------------------------------------- | --------------------------------------------------- |
| [Doel en scope](overview.md)                               | Doel, niet-doelen, status                           |
| [Requirements-inventory](requirements-inventory.md)        | Feature-eisen uit toonboekbladen                    |
| [Metamodel](metamodel.md)                                  | Concepten en relaties                               |
| [Syntax](syntax.md)                                        | Canonieke YAML-vorm                                 |
| [Semantiek](semantics.md)                                  | Betekenis van frasen, recite, optionals, cycle      |
| [Validatie](validation.md)                                 | Geldigheidsregels                                   |
| [Mapping VSA](mapping-vsa.md)                              | Contract VSA-tekst ↔ template (experimenteel)       |
| [Voorbeelden](examples.md)                                 | Normatieve / toetsende voorbeelden                  |
| [Conformiteit](conformance.md)                             | Wanneer template / tool conform is                  |
| [Open punten](open-points.md)                              | Open vragen                                         |
| [Versionering](versioning.md)                              | Versiebeleid van deze draft                         |
| [JSON Schema](schema/vsa-template.schema.json)             | Structurele toetsing                                |

## Criteria draft v0 (getoetst)

Deze draft geldt als **v0** wanneer:

1. inventory, metamodel, syntax, semantiek, validation en conformance geschreven zijn;
2. ≥2 geldige voorbeelden (verschillend genre of toon) en ≥3 ongeldige cases bestaan;
3. het schema (via `tests/test_vsa_template_schema.py`) de valid-set accepteert en de invalid-set weigert;
4. `open-points.md` restvragen expliciet vastlegt;
5. dit README het integratiepad naar `docs/specification/` beschrijft.

## Bewust buiten scope (nu)

- MusicXML-/SVG-export uit templates;
- OMR / automatische pitch-extractie uit PDF;
- wijzigingen aan de VSA 1.0-parser.
