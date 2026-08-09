---
slug: geldige-vsa-notatie
term: geldige-vsa-notatie
termType: concept
glossaryTerm: geldige VSA-notatie
glossaryText: "[VSA-notatie](@bron) die de [validator](@) (`vsa validate`) accepteert: syntactisch en semantisch in orde volgens de actieve [severity](@) / [ernstniveau](@)-regels (syntaxfouten zijn altijd hard)."
formPhrases:
  - geldige VSA-notatie
  - geldige vsa-notatie
  - geldige VSA
  - geldige vsa
---

# Geldige VSA-notatie

**Geldige VSA-notatie** is [VSA-notatie](@bron) die
[`vsa validate`](../reference/cli/validate.md) accepteert.
De [validator](@) controleert syntax en semantiek; syntaxfouten blijven altijd
fouten, semantische [diagnostics](@) / [diagnostische meldingen](@) kunnen via
[vsa.toml](@) / [projectconfiguratie](@) als [severity](@) / [ernstniveau](@)
`warning` worden behandeld.

Goede/valide voorbeelden van Geldige VSA-notatie zijn:
- Geaccepteerd door `vsa validate`
- Syntax hard; semantiek via [severity](@)

Geen goede/niet valide voorbeelden van Geldige VSA-notatie zijn:
- Spreektaal “VSA klopt” zonder validatie
- Stilzwijgend “gerepareerde” bron

Gebruik deze term in plaats van spreektaal zoals “VSA klopt”. Een
[vsa-bestand](@bron) bevat per definitie geldige VSA-notatie; in een
[VSA-blok](@) of losse [VSA-tekst](@) kan de notatie nog ongeldig zijn totdat
validatie slaagt.
