# Specificatie

Deze map bevat de geconsolideerde specificatie van VSA.

De specificatie beschrijft wat de notatie en tooling moeten betekenen. Architectuurkeuzes, implementatiegeschiedenis en gebruikershandleidingen staan buiten deze map.

## Documenten

| Document          | Inhoud                                                            |
| ----------------- | ----------------------------------------------------------------- |
| `overview.md`     | doel, scope, terminologie en status                               |
| `syntax.md`       | VSA-syntax, bloksyntax, modifiers, pitchmarkers en EBNF           |
| `semantics.md`    | muzikale betekenis van scopes, modifiers, posities en tooncontext |
| `validation.md`   | validatieregels, foutcategorieën en severity-model                |
| `directives.md`   | control tokens, comments, includes en document-samenstelling      |
| `rendering.md`    | SVG-rendering, glyphmodel, layout, configuratie en export         |
| `cli.md`          | CLI-contract voor gebruikers- en buildcommando's                  |
| `traceability.md` | herkomst van de geconsolideerde onderdelen                        |

## Status

Deze map is een geconsolideerde `docs-v2`-specificatie op basis van de bestaande documentatie in `docs/`.

Bij inhoudelijke twijfel blijft de bestaande VSA-specificatie de primaire bron totdat deze map expliciet als vervanging wordt vastgesteld.
