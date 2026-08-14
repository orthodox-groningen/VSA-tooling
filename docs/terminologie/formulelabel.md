---
slug: formulelabel
term: formulelabel
termType: concept
glossaryTerm: Formulelabel
glossaryText: "een [frase-id](@) (bijv. `1`, `2`, `laatste`) of [frase-anker](@) (bijv. `e. st.`, `l. st.`) die wordt gebruikt door onze tooling; ze staan boven de notenbalk van een formulepartituur."
formPhrases:
  - formulelabel
  - formulelabels
  - formule-label
  - formule-labels
glossaryNotes:
  - "Alle formulelabels staan op dezelfde hoogte, boven de noten, zonder autoplace."
  - "Een [frase-anker](@) heeft daaronder nog een pijl die strak naar de betreffende noot wijst; die pijl is geen tweede label."
  - "Schrijf in docs ‘formulelabel’ (TermRef) als je het bladmerk als geheel bedoelt; gebruik [frase-id](@) of [frase-anker](@) als je het type bedoelt."
---

# Formulelabel

Op het toonboekblad (en in de MuseScore-weergave van een [vsa-template](@))
staan twee soorten labels boven de balk:

| Soort            | Voorbeeld                         | YAML                            |
| ---------------- | --------------------------------- | ------------------------------- |
| [frase-id](@)    | `1`, `2`, `laatste` (cirkel/vlak) | sleutel van `phrases:`          |
| [frase-anker](@) | `e. st.`, `l. st.`, `vl. st.`, `l. lgr.` | `anchor:` op een template-event |

Beide zijn **formulelabels**: dezelfde lettergrootte, dezelfde hoogte, boven
de noten. Bij een [frase-anker](@) hoort extra een **pijl onder** de afkorting, die
naar de noot wijst waar de klemtoon landt. Die pijl is hulpgrafiek, geen
apart label en geen aparte YAML-sleutel.

## Status

| Status | Voorbeeld                                                      |
| ------ | -------------------------------------------------------------- |
| Ja     | Cirkel `1` en `l. st.` op dezelfde hoogte; pijl onder `l. st.` |
| Nee    | Een fermata, een toonsoortaanduiding, lyrics                   |

## Motivatie

Zonder één term voor “alles wat als staff-text op de formule staat” lopen
layoutregels (zelfde hoogte, geen autoplace) en begrippen (id vs. anker) door
elkaar. Het formulelabel is het **bladmerk**; frase-id en frase-anker zijn de
**typen**.

## Gerelateerd / verder lezen

- [frase-id](@), [frase-anker](@), [template-frase](@), [vsa-template](@)
- Bibliotheek: [MuseScore-conventies](../specification-vsa-templates/library/README.md)
