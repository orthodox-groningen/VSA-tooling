---
slug: frase-anker
term: frase-anker
termType: concept
glossaryTerm: Frase-anker
glossaryText: "een label op een [template-event](@) (`e.st.`, `l.st.`, `vl.st.`, `l.lgr.`) dat op het toonboekblad aangeeft welke tekstklemtoon (eerste / laatste / voorlaatste streek, of start van het slotmelisma op de laatste lettergreep) op die noot hoort te vallen."
formPhrases:
  - frase-anker
  - frase-ankers
glossaryNotes:
  - "Op het blad: afkorting `e. st.`, `l. st.`, `vl. st.`, `l. lgr.` als [formulelabel](@), met een pijl **onder** de afkorting die naar de noot wijst."
  - "`l.lgr.` wijst naar het begin van een slotmelisma: die noot en alle noten erna in de frase horen bij de laatste lettergreep."
  - "De YAML-waarde is zonder spaties (`l.st.`); op het blad mét spaties (`l. st.`)."
  - "Schrijf in docs ‘frase-anker’ (TermRef), niet los ‘anker’."
---

# Frase-anker

Een frase-anker koppelt een vaste noot in de formule aan een tekstuele
klemtoonpositie bij het mappen van [VSA](@)-tekst op een [vsa-template](@).
Op het blad staat de afkorting als [formulelabel](@) (`l. st.`), met een
pijl **onder** de afkorting die naar de noot wijst.

| Status | Voorbeeld                                         |
| ------ | ------------------------------------------------- |
| Ja     | `anchor: l.st.` op een cadens-[template-event](@) |
| Nee    | Een willekeurige maatstreep zonder bladlabel      |

## Motivatie

Zonder ankers weet tooling niet welke syllabe op welke cadensnoot moet landen
wanneer de tekst langer of korter is dan het “ideale” voorbeeld op het blad.

## Gerelateerd / verder lezen

- [template-event](@), [frase-id](@), [formulelabel](@), [reciteertoon](@), [vsa-template](@)
- Spec: [Semantiek — Anchors](../specification-vsa-templates/semantics.md)
- Mapping: [Mapping VSA](../specification-vsa-templates/mapping-vsa.md)
