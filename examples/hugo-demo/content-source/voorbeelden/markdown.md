---
title: "Markdown en Hugo"
---

# Markdown en Hugo

- [Home](/)
- [Vorige: Fouten](/voorbeelden/fouten/)
- [Volgende: CLI](/voorbeelden/cli/)

## Bron-Markdown

````markdown
::: vsa-notatie
[:] {/Hei_}{/lig_} is de Heer. [:]
:::
````

## Commando

```cmd
vsa build-markdown examples\hugo-demo\content-source generated\content generated\static\vsa
```

## Gegenereerde Markdown

```html
<img class="vsa-notation" src="/vsa/demo-block-1.svg" alt="VSA notatie">
```

## Gegenereerde SVG

::: vsa-notatie
[:] {/Hei_}{/lig_} is de Heer. [:]
:::

## Wat wordt waar opgeslagen?

| Type | Voorbeeld |
|------|------------|
| gegenereerde Markdown | `generated\content\...` |
| gegenereerde SVG | `generated\static\vsa\...` |
