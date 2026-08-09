---
slug: diagnostic
term: diagnostic
termType: concept
glossaryTerm: Diagnostic
glossaryText: "een melding die door [parser](@) of [validator](@) wordt geproduceerd en ten minste een foutcode, [severity](@) / [ernstniveau](@), bronlocatie en uitleg of context bij een vastgestelde afwijking bevat."
glossaryAlias: Diagnostische melding
formPhrases:
  - diagnostic
  - diagnostics
  - diagnostische melding
  - diagnostische meldingen
---

# Diagnostic

Een diagnostic / [diagnostische melding](@) beschrijft wat de tooling in de
invoer heeft gevonden en hoe ernstig dat is. Een losse logregel zonder code,
locatie of [severity](@) is in deze terminologie geen diagnostic.

Goede/valide voorbeelden van Diagnostic zijn:
- Foutcode + [severity](@) / [ernstniveau](@) + bronlocatie
- Output van [parser](@) of [validator](@)

Geen goede/niet valide voorbeelden van Diagnostic zijn:
- Losse logregel zonder code
- Stilzwijgende reparatie
