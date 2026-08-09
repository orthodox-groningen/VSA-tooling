---
slug: renderer
term: renderer
termType: concept
glossaryTerm: Renderer
glossaryText: "een component die een gevalideerde [AST](@) / [syntactische boom](@) of daarvan afgeleid layoutmodel omzet naar concrete uitvoer, zoals SVG, JSON, Markdown, [hugo-output](@) of MusicXML, zonder de [AST](@) semantisch te wijzigen."
formPhrases:
  - renderer
  - renderers
---

# Renderer

Een renderer maakt uitvoer uit de gevalideerde [VSA](@)-structuur. De renderer
verandert de [AST](@) niet en beslist niet alsnog of syntactische of
semantische invoer geldig is.

Goede/valide voorbeelden van Renderer zijn:
- SVG, JSON, Markdown, [hugo-output](@), MusicXML
- Lees gevalideerde [AST](@) / [syntactische boom](@)

Geen goede/niet valide voorbeelden van Renderer zijn:
- Semantische reparatie van de [AST](@)
- Vervangt [parser](@) of [validator](@)
