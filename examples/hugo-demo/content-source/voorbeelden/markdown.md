---
title: "Markdown en Hugo"
---

# Markdown en Hugo

- [Home](../../)
- [Vorige: Fouten](../fouten/)
- [Volgende: CLI](../cli/)

## Bron-Markdown

````markdown
::: vsa-notatie
[:] {/Hei_}{/lig_} is de Heer. [\\:]
:::
````

## Commando

```cmd
vsa build-markdown examples\hugo-demo\content-source generated\content examples\hugo-demo\static\vsa
```

## Gegenereerde Markdown

```go-html-template
{{< vsa src="/vsa/demo-block-1.svg" >}}
```

## Gegenereerde SVG

::: vsa-notatie
[:] {/Hei_}{/lig_} is de Heer. [\\:]
:::

## Wat wordt waar opgeslagen?

| Type | Voorbeeld |
|------|------------|
| gegenereerde Markdown | `generated\content\...` |
| gegenereerde SVG | `examples\hugo-demo\static\vsa\...` |
