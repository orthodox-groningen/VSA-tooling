# Specificatie vsa-templates (draft)

**Status:** draft v0 (getoetst met voorbeelden + schema-toets).

Deze map is de specificatie van [vsa-templates](vsa-template@): YAML voor
formulematige melodieën met [template-frasen](template-frase@), herhaling of
vaste volgorde, [reciteertonen](reciteertoon@), [frase-ankers](frase-anker@) en
SATB-[laddergraden](laddergraad@) binnen een [do-context](@).

Lees eerst het **idee**: [Doel en scope](overview.md).

## Relatie tot VSA 1.0

| Map                                            | Rol                                                 |
| ---------------------------------------------- | --------------------------------------------------- |
| [`docs/specification/`](../specification/)     | Normatieve [VSA](@) 1.0 (tekst + relatieve melodie) |
| **`docs/specification-vsa-templates/`** (deze) | Draft-spec voor melodietemplates                    |

Integratie in de VSA 1.0-tree volgt zodra glossary/org-termen en mapping stabiel
zijn. Tool-termen staan al in `docs/terminologie/` (zie [glossary](../glossary.md)).

## Documenten

| Document                                            | Inhoud                                         |
| --------------------------------------------------- | ---------------------------------------------- |
| [Doel en scope](overview.md)                        | Idee, niet-doelen, TermRefs                    |
| [Requirements-inventory](requirements-inventory.md) | Feature-eisen uit toonboekbladen               |
| [Metamodel](metamodel.md)                           | Concepten en relaties                          |
| [Syntax](syntax.md)                                 | Canonieke YAML-vorm                            |
| [Semantiek](semantics.md)                           | Betekenis cycle/sequence/recite/ankers         |
| [Validatie](validation.md)                          | Geldigheidsregels                              |
| [Mapping VSA](mapping-vsa.md)                       | Contract VSA-tekst ↔ template (experimenteel)  |
| [Rendering-valkuilen](rendering-pitfalls.md)        | Probleem → oorzaak → regel (MSCZ/MXL/instance) |
| [Voorbeelden](examples.md)                          | Library + invalid cases                        |
| [Library](library/README.md)                        | Werkmappen per genre × toon                    |
| [Conformiteit](conformance.md)                      | Wanneer template/tool conform is               |
| [Open punten](open-points.md)                       | Open vragen                                    |
| [Versionering](versioning.md)                       | Versiebeleid van deze draft                    |
| [JSON Schema](schema/vsa-template.schema.json)      | Structurele toetsing                           |

## Criteria draft v0 (getoetst)

1. Inventory, metamodel, syntax, semantiek, validation en conformance geschreven;
2. ≥2 geldige voorbeelden (verschillend genre/toon) en ≥3 ongeldige cases;
3. Schema-/documenttoets via `tests/test_vsa_template_schema.py` groen;
4. Open punten expliciet;
5. Begrippen via curated texts + TermRefs leesbaar op de docs-site.

## Bewust buiten scope (nu)

- MusicXML-/SVG-export uit templates;
- OMR / automatische pitch-extractie uit PDF;
- wijzigingen aan de VSA 1.0-[parser](@).
