---
title: "CLI: vsa blocks"
---

# CLI: `vsa blocks`

- [Home](/)
- [CLI overzicht](/voorbeelden/cli/)
- [Vorige: vsa svg](/voorbeelden/cli/svg/)
- [Volgende: vsa parse](/voorbeelden/cli/parse/)

## Waarvoor gebruik je dit?

Gebruik `vsa blocks` om te zien hoeveel VSA-blokken in een Markdownbestand staan.

## Input Markdown

````markdown
::: vsa-notatie
[:] {/Hei_}{/lig_} is de Heer. [\\:]
:::
````

## Commando

```cmd
vsa blocks examples\minimal\valid-block-demo.md
```

## Verwachte output

```text
1 VSA-blok(ken) gevonden
```

## Met JSON

```cmd
vsa blocks examples\minimal\valid-block-demo.md --json
```

Dan zie je onder andere:

```text
start_line
end_line
metadata
body
ast
```

## Wanneer nuttig?

Gebruik dit als een Markdownbestand niet lijkt te worden verwerkt en je wilt controleren of de VSA-blokken worden herkend.
