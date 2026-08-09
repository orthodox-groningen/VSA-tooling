---
slug: validator
term: validator
termType: concept
glossaryTerm: Validator
glossaryText: "een component die een geparseerde [AST](@) / [syntactische boom](@) of [VSA](@)-invoer toetst aan semantische en normatieve regels en overtredingen als [diagnostics](@) / [diagnostische meldingen](@) rapporteert zonder ze stilzwijgend te repareren."
formPhrases:
  - validator
  - validators
---

# Validator

De validator controleert of [VSA](@)-invoer inhoudelijk voldoet aan de regels
die na parsing gelden. Waar mogelijk verzamelt de validator meerdere
onafhankelijke [diagnostics](@) in een run.

Goede/valide voorbeelden van Validator zijn:
- [Diagnostics](@) / [diagnostische meldingen](@) rapporteren
- Semantische toets na de [parser](@)

Geen goede/niet valide voorbeelden van Validator zijn:
- Stilzwijgend repareren van de [AST](@)
- Tokens omzetten naar [AST](@)
