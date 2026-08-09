---
slug: do-context
term: do-context
termType: concept
glossaryTerm: Do-context
glossaryText: "de grondtooncontext waarbinnen relatieve toonhoogtebewegingen in [VSA-notatie](@bron) worden geïnterpreteerd; voor MusicXML-export of afspelen vastgelegd via blok-[metadata](@) (`do`, `mode`), niet via de zangtekst zelf."
glossaryAlias: Tooncontext
formPhrases:
  - do-context
  - do-contexts
  - tooncontext
  - tooncontexten
glossaryNotes:
  - "Voorbeeld: `do=\"F4\"` en `mode=\"major\"` in een [VSA-blok](@) of `.vsa`-frontmatter."
  - "Een begin-[pitch-marker](@) / [hoogte-markering](@) `[:]` betekent: start op de do-context."
---

# Do-context

De do-context / [tooncontext](@) is de grondtoon waartegen relatieve
[hoogte-modifiers](@) en [pitch-markers](@) / [hoogte-markeringen](@) worden
gerekend.

Goede/valide voorbeelden van Do-context zijn:
- `do` / `mode` in [metadata](@)
- Referentiepunt voor ladderstappen

Geen goede/niet valide voorbeelden van Do-context zijn:
- Een losse nootnaam in de zangtekst
- De absolute MIDI-tuning van een instrument

## Motivatie

Relatieve [VSA](@)-hoogte is zonder startpunt niet om te zetten naar absolute
toonhoogten (MusicXML, Coria). Visuele SVG-weergave kan zonder absolute
do-context; export en afspelen niet.

## Gerelateerd / verder lezen

- [metadata](@), [pitch-marker](@), [hoogte-modifier](@)
- Specificatie: [Semantiek — Do-context](../specification/semantics.md#do-context)
