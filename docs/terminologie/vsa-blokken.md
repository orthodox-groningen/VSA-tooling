---
slug: vsa-blokken
term: vsa-blokken
termType: concept
glossaryTerm: VSA-blok
glossaryText: "een tekstfragment in een Markdownbestand dat begint met `::: vsa-notatie` en eindigt met `:::`, beide aan het begin van een regel, met daartussen [VSA-notatie](@bron); typisch ontdekt en verwerkt door de [vsa-toolset](@) (o.a. `vsa blocks`, `vsa validate`, `vsa process`)."
formPhrases:
  - vsa-blok
  - vsa-blokken
  - VSA-blok
  - VSA-blokken
---

# VSA-blok

Een VSA-blok is het Markdown-omhulsel waarin [VSA-notatie](@bron) in documentatie of content-source staat:

```markdown
::: vsa-notatie
{tekst_}
:::
```

De openings- en sluitingsregels staan aan het begin van de regel. De inhoud
ertussen is [VSA-tekst](@) die de [parser](@) en [validator](@) verwerken.
Commando’s zoals `vsa blocks`, `vsa validate` en `vsa process` werken op zulke
blokken in `.md`-bestanden (naast losse `.vsa`-bestanden).
