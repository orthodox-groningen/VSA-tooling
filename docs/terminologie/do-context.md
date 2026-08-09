---
slug: do-context
term: do-context
termType: concept
glossaryTerm: Do-context
glossaryText: "de grondtooncontext waarbinnen relatieve toonhoogtebewegingen in [VSA](@) en in een [vsa-template](@) worden geïnterpreteerd; voor export of afspelen vastgelegd via `do` en `mode`, niet via de zangtekst zelf."
formPhrases:
  - do-context
  - do-contexts
  - tooncontext
  - tooncontexten
glossaryNotes:
  - "Voorbeeld: blokmetadata `do=\"F4\"` en `mode=\"major\"`; begin-[pitch-marker](@) `[:]` betekent start op de do-context."
---

# Do-context

De do-context (ook: tooncontext) is de grondtoon waartegen relatieve
hoogtebewegingen en [laddergraden](laddergraad@) worden gelezen.

| Status | Voorbeeld                                                     |
| ------ | ------------------------------------------------------------- |
| Ja     | `do` + `mode` in VSA-blokmetadata of in een [vsa-template](@) |
| Nee    | Absolute toonhoogte “ergens in de tekst” zonder die context   |

## Motivatie

Zonder gedeelde do-context zijn relatieve notatie (VSA) en formulebladen
(templates) niet eenduidig naar klinkende tonen te mappen.

## Gerelateerd / verder lezen

- [pitch-marker](@), [enkelvoudige-hoogte-modifier](@), [vsa-template](@), [laddergraad](@)
- Specificatie: [Semantiek — Do-context](../specification/semantics.md#55-do-context)
