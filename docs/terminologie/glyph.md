---
slug: glyph
term: glyph
termType: concept
glossaryTerm: Glyph
glossaryText: "een zichtbaar grafisch teken dat de [renderer](@) tekent voor een VSA-markering (bijvoorbeeld een streep van een [hoogte-modifier](@) of een onderstreping van een [lengte-modifier](@)), los van de zangtekst zelf."
formPhrases:
  - glyph
  - glyphs
  - glyphmodel
glossaryNotes:
  - "Voorbeeld: `/` in `{/Hei_}` wordt als bovenglyph gerenderd; `_` als onderglyph."
  - "Pitch-markers en control-tokens kunnen eveneens als glyphs of layout-aanwijzingen worden weergegeven."
---

# Glyph

Een glyph is het zichtbare teken dat de [renderer](@) voor een VSA-markering
tekent (boven of onder de tekst), niet de lettertekens van het zangelement zelf.

| Wel                                        | Niet                                                   |
| ------------------------------------------ | ------------------------------------------------------ |
| Strepen, punten, connectors van modifiers  | De letters in `Hei` binnen `{/Hei_}`                   |
| Visuele weergave van een [pitch-marker](@) | De brontekens `/` of `_` als platte ASCII in de `.vsa` |

## Motivatie

Parser en validator werken op tokens; lezers zien strepen en punten. Het
glyphbegrip scheidt die visuele laag van de syntactische tokens, zodat
layout- en SVG-regels eenduidig te specificeren zijn.

## Gerelateerd / verder lezen

- [renderer](@), [hoogte-modifier](@), [lengte-modifier](@), [pitch-marker](@)
- Specificatie: [Rendering](../specification/rendering.md)
