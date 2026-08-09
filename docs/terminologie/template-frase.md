---
slug: template-frase
term: template-frase
termType: concept
glossaryTerm: Template-frase
glossaryText: "een genaamde melodische eenheid binnen een [vsa-template](@) (bijv. id `1`, `2`, `1a` of `laatste`), opgebouwd uit geordende [template-events](template-event@)."
formPhrases:
  - template-frase
  - template-frasen
glossaryNotes:
  - "Op toonboekbladen vaak als omcirkeld cijfer of label `laatste`."
  - "Schrijf in docs bij voorkeur ‘template-frase’ (TermRef), niet los ‘frase’."
---

# Template-frase

Een template-frase is één herbruikbaar melodisch blok in een [vsa-template](@).

| Status | Voorbeeld                                                      |
| ------ | -------------------------------------------------------------- |
| Ja     | Frase `1` met open → recite → cadens; frase `laatste` als slot |
| Nee    | Een losse maatstreep of een enkele noot zonder frase-id        |

## Motivatie

Formulezang wisselt vaste blokken af (`||: 1, 2 :|| laatste` of een vaste
`sequence`). Zonder expliciete frase-ids is die structuur niet machineleesbaar.

## Gerelateerd / verder lezen

- [vsa-template](@), [template-event](@), [frase-anker](@)
- Spec: [Metamodel](../specification-vsa-templates/metamodel.md)
