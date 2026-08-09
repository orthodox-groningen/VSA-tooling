---
slug: laddergraad
term: laddergraad
termType: concept
glossaryTerm: Laddergraad
glossaryText: "een toonpositie op de ladder binnen een [do-context](@) (`do`, `re`, `mi`, …), optioneel chromatisch (`#`/`b`) en met octaafverschuiving (`do-1`); in een [vsa-template](@) de canonieke vorm van SATB-pitches."
formPhrases:
  - laddergraad
  - laddergraden
  - toonladdergraad
  - toonladdergraden
glossaryNotes:
  - "Voorbeeld bij `do: F4`, `mode: major`: `mi` = A4, `sol-1` = C4."
---

# Laddergraad

Een laddergraad noemt een toon **relatief** aan de [do-context](@), niet als
losse scientific pitch per stem.

| Status | Voorbeeld                                                    |
| ------ | ------------------------------------------------------------ |
| Ja     | `mi`, `fa`, `#re`, `do-1` in template-`pitches`              |
| Nee    | Alleen `A4` zonder `do`/`mode` als primaire templatewaarheid |

## Motivatie

Zelfde formule op een andere inzettoon: alleen `do` wijzigt; graden blijven.
Dat sluit aan op VSA, waar absolute toonhoogte ook via do-context komt.

## Gerelateerd / verder lezen

- [do-context](@), [vsa-template](@), [enkelvoudige-hoogte-modifier](@)
- Spec: [Syntax — Pitches](../specification-vsa-templates/syntax.md)
