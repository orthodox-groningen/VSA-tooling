---
slug: vsa-scope
term: vsa-scope
termType: concept
glossaryTerm: VSA-scope
glossaryText: "een tekstfragment dat met `{` begint, met `}` eindigt, geen whitespace binnen de accolades bevat en door de parser kan worden opgesplitst in optionele hoogte-modifier, verplicht zangelement en optionele lengte-modifier."
glossaryAlias: Scope
formPhrases:
  - vsa-scope
  - vsa-scopes
  - scope
  - scopes
glossaryNotes:
  - "Voorbeeld: `{/Hei_}` — hoogte-modifier `/`, zangelement `Hei`, lengte-modifier `_`."
  - "Lege `{}` of `{te kst}` (spatie) zijn geen geldige VSA-scope."
---

# VSA-scope

Een VSA-scope koppelt gezongen tekst aan modifiers, bijvoorbeeld `{/Hei_}`.

De parser gebruikt scopes om tekst en muzikale markeringen structureel te
herkennen; een lege scope of een scope met whitespace binnen de accolades
voldoet niet.

## Motivatie

Zonder scopes is er geen eenduidige eenheid “zangtekst + hoogte/lengte” voor
parser, validator en renderer. Het begrip is de kernbouwsteen van
[geldige VSA-notatie](@).

## Gerelateerd / verder lezen

- [hoogte-modifier](@), [lengte-modifier](@), [pitch-marker](@)
- Org-begrip notatie vs tooling: [vsa-notatie](@bron), [vsa-tooling](@bron)
- Specificatie: [syntax](../specification/syntax.md)
