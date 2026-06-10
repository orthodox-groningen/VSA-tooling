---
title: "CLI: vsa process"
---

# CLI: `vsa process`

- [Home](/)
- [CLI overzicht](/voorbeelden/cli/)
- [Vorige: vsa parse](/voorbeelden/cli/parse/)
- [Volgende: vsa build-markdown](/voorbeelden/cli/build-markdown/)

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

## Gegenereerd bestand

```text
generated\vsa\valid-block-demo-block-1.svg
```

## Wanneer gebruik je dit?

Gebruik dit als je SVG-bestanden wilt controleren zonder Hugo Markdown te bouwen.
