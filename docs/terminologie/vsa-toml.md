---
slug: vsa-toml
term: vsa-toml
termType: concept
glossaryTerm: vsa.toml
glossaryText: "een projectconfiguratiebestand met de naam `vsa.toml` dat herkende [VSA](@)-toolinginstellingen bevat voor rendering, output of validatie."
glossaryAlias: Projectconfiguratie
formPhrases:
  - vsa.toml
  - vsa.toml-bestanden
  - projectconfiguratie
  - projectconfiguraties
---

# vsa.toml

`vsa.toml` / [projectconfiguratie](@) bundelt configuratie voor lokale
verwerking en buildstappen. Alleen instellingen die door de [VSA](@)-tooling
als configuratiesleutels worden gelezen, vallen onder dit begrip.

Goede/valide voorbeelden van vsa.toml zijn:
- Herkende sleutels in `vsa.toml`
- Stuurt rendering, output of [severity](@)

Geen goede/niet valide voorbeelden van vsa.toml zijn:
- Willekeurige TOML buiten de tool-contract
- Bron-[VSA-notatie](@bron) zelf
