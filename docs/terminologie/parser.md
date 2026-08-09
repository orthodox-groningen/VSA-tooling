---
slug: parser
term: parser
termType: concept
glossaryTerm: Parser
glossaryText: "een component die [VSA](@)-brontekst of tokens volgens de grammatica omzet naar expliciete [AST](@) / [syntactische boom](@)-nodes, bronlocaties behoudt en geen semantische reparaties of renderlogica uitvoert."
formPhrases:
  - parser
  - parsers
---

# Parser

De parser bouwt de syntactische structuur van [VSA](@)-invoer. Semantische
controles horen bij de [validator](@); uitvoer voor gebruikers hoort bij de
[renderer](@).

Goede/valide voorbeelden van Parser zijn:
- Tokens → [AST](@) / [syntactische boom](@)
- Bronlocaties behouden

Geen goede/niet valide voorbeelden van Parser zijn:
- Semantische validatie
- SVG/MusicXML-uitvoer ([renderer](@))
