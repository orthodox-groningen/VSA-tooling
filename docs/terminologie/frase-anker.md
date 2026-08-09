---
slug: frase-anker
term: frase-anker
termType: concept
glossaryTerm: Frase-anker
glossaryText: "een label op een [template-event](@) (`e.st.`, `l.st.`, `vl.st.`) dat op het toonboekblad aangeeft welke tekstklemtoon (eerste / laatste / voorlaatste streek) op die noot hoort te vallen."
formPhrases:
  - frase-anker
  - frase-ankers
glossaryNotes:
  - "Op het blad vaak met pijl en afkorting `e. st.`, `l. st.`, `vl. st.`."
  - "Schrijf in docs ‘frase-anker’ (TermRef), niet los ‘anker’."
---

# Frase-anker

Een frase-anker koppelt een vaste noot in de formule aan een tekstuele
klemtoonpositie bij het mappen van [VSA](@)-tekst op een [vsa-template](@).

| Status | Voorbeeld                                         |
| ------ | ------------------------------------------------- |
| Ja     | `anchor: l.st.` op een cadens-[template-event](@) |
| Nee    | Een willekeurige maatstreep zonder bladlabel      |

## Motivatie

Zonder ankers weet tooling niet welke syllabe op welke cadensnoot moet landen
wanneer de tekst langer of korter is dan het “ideale” voorbeeld op het blad.

## Gerelateerd / verder lezen

- [template-event](@), [reciteertoon](@), [vsa-template](@)
- Spec: [Semantiek — Anchors](../specification-vsa-templates/semantics.md)
- Mapping: [Mapping VSA](../specification-vsa-templates/mapping-vsa.md)
