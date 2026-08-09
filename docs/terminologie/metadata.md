---
slug: metadata
term: metadata
termType: concept
glossaryTerm: Metadata
glossaryText: "gegevens die als gestructureerde blokparameters of YAML-frontmatter bij [VSA](@)-bronmateriaal staan, verwerking of identificatie sturen en zelf niet tot de zichtbare [VSA-notatie](@bron) behoren."
formPhrases:
  - metadata
  - metadata-items
---

# Metadata

Metadata kan in blokmetadata of frontmatter staan en stuurt validatie,
rendering, export of identificatie zonder zelf als gezongen tekst of
[VSA](@)-token te worden weergegeven. Voorbeeld: `do` / `mode` voor de
[do-context](@) / [tooncontext](@).

Goede/valide voorbeelden van Metadata zijn:
- Blokparameters / YAML-frontmatter
- Stuurt [validator](@) / [renderer](@) / export

Geen goede/niet valide voorbeelden van Metadata zijn:
- Zangelement of [modifier](@) in een [scope](@)
- Zichtbare [glyphs](@) in SVG
