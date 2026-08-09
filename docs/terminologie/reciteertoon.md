---
slug: reciteertoon
term: reciteertoon
termType: concept
glossaryTerm: Reciteertoon
glossaryText: "een [template-event](@) (of bladnotatie) waarop een variabel aantal syllaben op hetzelfde SATB-akkoord wordt gezongen; in een [vsa-template](@) gemarkeerd als `role: recite`."
formPhrases:
  - reciteertoon
  - reciteertonnen
glossaryNotes:
  - "Op het blad vaak als breve of ‘box’-nootkop; dat is geen aparte VSA-[ELM](enkelvoudige-lengte-modifier@), maar de recite-rol."
  - "In YAML: `role: recite`."
---

# Reciteertoon

De reciteertoon is het flexibele middenstuk van veel formulefrasen: de tekst
kan kort of lang zijn, de toonhoogte blijft gelijk.

| Status | Voorbeeld                                                          |
| ------ | ------------------------------------------------------------------ |
| Ja     | Breve-akkoord op het blad; `role: recite` met duur `~` per syllabe |
| Nee    | Een vaste cadensnoot met precies één syllabe en anker `l.st.`      |

## Motivatie

Formulezang moet ongelijke tekstlengtes op dezelfde melodie kunnen zetten.
De reciteertoon is daarvoor het rekmechanisme.

## Gerelateerd / verder lezen

- [template-event](@), [frase-anker](@), [enkelvoudige-lengte-modifier](@)
- Spec: [Semantiek — Recite](../specification-vsa-templates/semantics.md)
