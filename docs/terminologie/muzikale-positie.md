---
slug: muzikale-positie
term: muzikale-positie
termType: concept
glossaryTerm: Muzikale positie
glossaryText: "de kleinste muzikale eenheid binnen [VSA-notatie](@bron): één relatieve toonhoogtebeweging (één [enkelvoudige hoogte-modifier](@)), één duur (één [enkelvoudige lengte-modifier](@)) en een koppeling aan één zangelement in een [VSA-scope](@)."
formPhrases:
  - muzikale positie
  - muzikale posities
glossaryNotes:
  - "Voorbeeld: `{/tekst_}` bevat één muzikale positie (hoogte `/`, zangelement `tekst`, duur `_`)."
  - "Samengestelde modifiers met `&`, zoals `{/&/tekst_&-} leveren meerdere muzikale posities binnen één scope (melisma)."
---

# Muzikale positie

Een muzikale positie is de kleinste muzikale eenheid in [VSA-notatie](@bron):
één hoogtebeweging, één duur en één zangelement.

| Wel                                                    | Niet                                                  |
| ------------------------------------------------------ | ----------------------------------------------------- |
| Eén EHM + één ELM + zangelement in een [scope](@)      | Losse tekst buiten scopes                             |
| Elke `&`-gescheiden stap in een samengestelde modifier | Een hele melodie of [zangstuk](@bron) als één eenheid |

## Motivatie

Zonder dit begrip is er geen eenduidige eenheid om hoogte, duur en tekst aan
elkaar te koppelen voor [validator](@) en [renderer](@) (melisma, MusicXML,
SVG-kolommen).

## Gerelateerd / verder lezen

- [modifier](@), [hoogte-modifier](@), [lengte-modifier](@), [vsa-scope](@)
- Specificatie: [Semantiek — Muzikale positie](../specification/semantics.md#muzikale-positie)
