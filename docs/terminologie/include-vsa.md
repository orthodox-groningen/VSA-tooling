---
slug: include-vsa
term: include-vsa
termType: concept
glossaryTerm: "@include-vsa"
glossaryText: "een string die met `@include-vsa` begint, precies één ondersteunde resolverparameter bevat (`zoek=`, `id=` of `lokaal=`) en tijdens verwerking door de body van het doelbestand wordt vervangen."
glossaryAlias: VSA-inline-include
formPhrases:
  - "@include-vsa"
  - "@include-vsa-directives"
  - vsa-inline-include
  - vsa-inline-includes
glossaryNotes:
  - "Voorbeeld: `refrein: @include-vsa zoek=\"Troparion\"` — alleen de `@include-vsa …`-substring wordt vervangen."
---

# @include-vsa

`@include-vsa` vervangt alleen de directive-substring door VSA-bronmateriaal
tijdens verwerking. Omringende tekst in dezelfde regel blijft bestaan.

Voorbeeld:

```text
refrein: @include-vsa lokaal=cherubijnenhymne/kastorski/groningen/groningen-vsa
```

## Motivatie

Zo kun je herbruikbare VSA-fragmenten (refreinen, gedeelde regels) één keer
onderhouden en op meerdere plaatsen includen, zonder de omringende regeltekst
te verliezen.

## Gerelateerd / verder lezen

- Referentie: [include-vsa](../reference/include-vsa.md)
- Org: [representatie](@bron), [samenstelling](@bron) — context waarin includes
  in publicatieketens voorkomen
