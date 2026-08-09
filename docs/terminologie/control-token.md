---
slug: control-token
term: control-token
termType: concept
isa: bracket-directive
glossaryTerm: Control-token
glossaryText: "een [bracket-directive](@) / [bracket-token](@) waarvan de tokenwaarde een ondersteunde control-tokenvorm is, zoals `[*]`, `[/]`, `[*?]` of `[/?]`, en die niet als [pitch-marker](@) / [hoogte-markering](@) wordt geparseerd."
formPhrases:
  - control-token
  - control-tokens
---

# Control-token

Een [bracket-directive](@) geldt als control-token wanneer bracket-dispatch de
tokenwaarde herkent als ondersteunde structurele of renderergerichte
aanwijzing en niet als [pitch-marker](@). De abstracte betekenis wordt door de
[parser](@) vastgelegd; de concrete visuele uitvoering kan per [renderer](@)
verschillen.

Goede/valide voorbeelden van Control-token zijn:
- `[*]`, `[/]`, `[*?]`, `[/?]`
- Structurele / renderergerichte aanwijzing

Geen goede/niet valide voorbeelden van Control-token zijn:
- `[/:]` of `[:]` ([pitch-marker](@))
- Ongeldige of onbekende bracket-inhoud
