---
slug: template-event
term: template-event
termType: concept
glossaryTerm: Template-event
glossaryText: "de kleinste muzikale stap in een [template-frase](@): een rol (open, [reciteertoon](@), cadens, link), een duur als [enkelvoudige lengte-modifier](enkelvoudige-lengte-modifier@), en SATB-[laddergraden](laddergraad@)."
formPhrases:
  - template-event
  - template-events
glossaryNotes:
  - "Optioneel: `optional: true` (haakjesnoot) of een [frase-anker](@)."
  - "Schrijf in docs ‘template-event’, niet los ‘event’."
---

# Template-event

Een template-event is één gelijktijdig SATB-akkoord (of stap) binnen een
[template-frase](@).

| Status | Voorbeeld                                                               |
| ------ | ----------------------------------------------------------------------- |
| Ja     | Recite op `mi/do/sol-1/do-1` met duur `~`; cadensnoot met anker `l.st.` |
| Nee    | Alleen een tekstsyllabe zonder melodische rol in het template           |

## Motivatie

Homofone formules bewegen stemmen synchroon; het event is de gedeelde
tijdlijnpositie waarop mapping later syllaben legt.

## Gerelateerd / verder lezen

- [template-frase](@), [reciteertoon](@), [frase-anker](@), [laddergraad](@), [enkelvoudige-lengte-modifier](@)
- Spec: [Syntax](../specification-vsa-templates/syntax.md)
