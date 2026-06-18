---
title: "CLI: vsa process"
---

# CLI: `vsa process`

- [Home](../../../)
- [CLI overzicht](../)
- [Vorige: vsa parse](../parse/)
- [Volgende: vsa build-markdown](../build-markdown/)

## Waarvoor gebruik je dit?

Gebruik `vsa process` als je Markdown met VSA-blokken hebt en alleen SVG-bestanden wilt genereren.

## Input Markdown

````markdown
::: vsa-notatie
[:] {/Hei_}{/lig_} is de Heer. [\\:]
:::
````

## Commando

```cmd
vsa process examples\minimal\valid-block-demo.md generated\vsa
```

## Verwachte output

```text
1 SVG-bestand(en) gegenereerd
- generated\vsa\valid-block-demo-block-1.svg
```
