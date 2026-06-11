---
title: "CLI: vsa blocks"
---

# CLI: `vsa blocks`

- [Home](../../../)
- [CLI overzicht](../)
- [Vorige: vsa svg](../svg/)
- [Volgende: vsa parse](../parse/)

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
