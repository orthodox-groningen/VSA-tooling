---
slug: frase-id
term: frase-id
termType: concept
glossaryTerm: Frase-id
glossaryText: "de machineleesbare id van een [template-frase](@) in een [vsa-template](@) (`1`, `2`, `laatste`, …); op het toonboekblad het cijfer of woord in een cirkel of vierkant boven de eerste noot van die frase."
formPhrases:
  - frase-id
  - frase-ids
glossaryNotes:
  - "De id is `1`, `2`, `laatste`, enzovoort — ongeacht of het blad een cirkel of een vierkant toont."
  - "Op het blad is de frase-id een [formulelabel](@); in YAML is het de sleutel van `phrases:`."
  - "Schrijf in docs ‘frase-id’ (TermRef), niet los ‘id’ of ‘frase-nummer’."
---

# Frase-id

Elke [template-frase](@) in een [vsa-template](@) heeft één frase-id. Die id is
tegelijk:

- de **YAML-sleutel** onder `phrases:` (`1`, `2`, `laatste`, …);
- het **zichtbare label** op het toonboekblad (cijfer of woord in cirkel of
  vierkant) boven de eerste noot van die frase.

De **vorm** van het kader (cirkel vs. vierkant) is geen extra id: een vierkant
`2` is nog steeds frase-id `2`. Optionele noten binnen de frase staan tussen
haakjes; dat verandert de frase-id niet.

## Status

| Status | Voorbeeld                                                           |
| ------ | ------------------------------------------------------------------- |
| Ja     | `phrases.laatste` en het woord *laatste* in een cirkel              |
| Nee    | Een maatnummer, een [frase-anker](@) (`l. st.`), of een herhaalhaak |

## Motivatie

Zonder een stabiele frase-id kunnen `cycle`, mapping naar [VSA](@) en de
partituurweergave niet naar dezelfde melodische blokken wijzen.

## Gerelateerd / verder lezen

- [template-frase](@), [formulelabel](@), [frase-anker](@), [vsa-template](@)
- Spec: [Semantiek](../specification-vsa-templates/semantics.md)
- Bibliotheek: [MuseScore-conventies](../specification-vsa-templates/library/README.md)
