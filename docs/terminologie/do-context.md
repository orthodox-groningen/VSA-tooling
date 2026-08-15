---
slug: do-context
term: do-context
termType: concept
glossaryTerm: Do-context
glossaryText: "de grondtooncontext waarbinnen relatieve toonhoogtebewegingen in [VSA-notatie](@bron) en in een [vsa-template](@) worden geïnterpreteerd; voor MusicXML-export of afspelen vastgelegd via blok-[metadata](@) (`do`, `mode`), niet via de zangtekst zelf."
glossaryAlias: Tooncontext
formPhrases:
  - do-context
  - do-contexts
  - tooncontext
  - tooncontexten
glossaryNotes:
  - "Voorbeeld: `do=\"F4\"` en `mode=\"major\"` in een [VSA-blok](@), `.vsa`-frontmatter, of een [vsa-template](@)."
  - "Een begin-[pitch-marker](@) / [hoogte-markering](@) `[:]` betekent: start op de do-context."
---

# Do-context

De do-context / [tooncontext](@) is de grondtoon waartegen relatieve
[hoogte-modifiers](@) en [pitch-markers](@) / [hoogte-markeringen](@) worden
gerekend — en waartegen [laddergraden](laddergraad@) in een [vsa-template](@)
worden gelezen.

| Status | Voorbeeld                                                                   |
| ------ | --------------------------------------------------------------------------- |
| Ja     | `do` / `mode` in [metadata](@) of in een [vsa-template](@)                  |
| Nee    | Een losse nootnaam in de zangtekst; absolute MIDI-tuning van een instrument |

## Motivatie

Relatieve [VSA](@)-hoogte is zonder startpunt niet om te zetten naar absolute
toonhoogten (MusicXML, Coria). Hetzelfde geldt voor formulebladen als
[vsa-template](@). Visuele SVG-weergave kan zonder absolute do-context; export
en afspelen niet.

## Gerelateerd / verder lezen

- [metadata](@), [pitch-marker](@), [hoogte-modifier](@), [vsa-template](@), [laddergraad](@)
- Specificatie: [Semantiek — Do-context](../specification/semantics.md#55-do-context)
