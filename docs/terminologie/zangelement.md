---
slug: zangelement
term: zangelement
termType: concept
glossaryTerm: Zangelement
glossaryText: "het verplichte tekstfragment binnen een [VSA-scope](@) waaraan optionele [hoogte-modifiers](@) en [lengte-modifiers](@) hangen; de gezongen lettergreep of tekst die bij de [muzikale posities](@) hoort."
formPhrases:
  - zangelement
  - zangelementen
glossaryNotes:
  - "Voorbeeld: in `{/Hei_}` is `Hei` het zangelement."
  - "Lege `{}` heeft geen zangelement en is geen geldige scope."
---

# Zangelement

Een zangelement is de gezongen tekst binnen een [VSA-scope](@) — verplicht, zonder
whitespace, en zonder modifiertekens.

Goede/valide voorbeelden van Zangelement zijn:
- `Hei` in `{/Hei_}`
- Meerdere lettergrepen als één tekstfragment in één [scope](@) (melisma deelt hetzelfde zangelement)

Geen goede/niet valide voorbeelden van Zangelement zijn:
- De [hoogte-modifier](@) `/` of [lengte-modifier](@) `_`
- Losse tekst buiten [scopes](@) (dat is ongescopte tekst, geen zangelement)

## Motivatie

Zonder dit begrip is er geen eenduidige koppeling tussen gezongen tekst en
[muzikale posities](@) binnen een [scope](@).

## Gerelateerd / verder lezen

- [vsa-scope](@), [modifier](@), [muzikale-positie](@)
- Specificatie: [Syntax](../specification/syntax.md), [Semantiek](../specification/semantics.md)
