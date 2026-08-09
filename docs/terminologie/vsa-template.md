---
slug: vsa-template
term: vsa-template
termType: concept
glossaryTerm: VSA-template
glossaryText: "een machineleesbaar YAML-document dat een formulematige liturgische melodie vastlegt (frasen, herhaling of vaste volgorde, [reciteertoon](@), ankers, SATB-[laddergraden](laddergraad@)) binnen een [do-context](@), bedoeld om later tekst uit [VSA](@) erop te mappen."
formPhrases:
  - vsa-template
  - vsa-templates
  - VSA-template
  - VSA-templates
  - melodietemplate
  - melodietemplates
glossaryNotes:
  - "Voorbeeld: tropaarmelodie toon 4 als YAML met cycle 1,2 en slotfrase laatste."
  - "Een vsa-template is geen [zangstuk](@bron); het is een herbruikbare formulebeschrijving."
---

# VSA-template

Een vsa-template beschrijft de **melodieformule** (zoals op een toonboekblad
zonder lyrics): welke [template-frasen](template-frase@) er zijn, in welke
volgorde ze worden herhaald of vastgezet, en welke noten/rollen SATB zingt.

| Status | Voorbeeld                                                                      |
| ------ | ------------------------------------------------------------------------------ |
| Ja     | YAML volgens de [vsa-templates-spec](../specification-vsa-templates/README.md) |
| Nee    | Een concreet [zangstuk](@bron) met volledige tekst in [VSA](@)                 |

## Motivatie

Zonder templates moet elke tekst de hele SATB-formule opnieuw coderen. Met
templates scheid je **formule** (herbruikbaar) van **tekst** (per zangstuk).

## Gerelateerd / verder lezen

- [template-frase](@), [template-event](@), [frase-anker](@), [reciteertoon](@), [do-context](@)
- Spec: [Doel en scope](../specification-vsa-templates/overview.md)
