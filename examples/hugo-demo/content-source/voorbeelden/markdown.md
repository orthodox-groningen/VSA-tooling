---
title: "Markdown en Hugo"
---

# Markdown en Hugo

- [Home]({{< navbuttons 
    "Weekdagen  | ../weekdagen/"
    "Zondagen   | ../zondagen/"
    "Feesteigen | ../feesteigen/"
>}})
- [Vorige: Fouten](../fouten/)
- [Volgende: CLI](../cli/)

## Bron-Markdown

````markdown
::: vsa-notatie
[:] {/Hei_}{/lig_} is de Heer. [//:]
:::
````

## Commando

```cmd
vsa build-markdown examples\hugo-demo\content-source generated\content examples\hugo-demo\static\vsa
```

## Gegenereerde Markdown

Als de demo-site met shortcode-output wordt gebouwd, komt er in de gegenereerde Markdown ongeveer dit te staan:

```go-html-template
{{</* vsa src="/vsa/demo-block-1.svg" */>}}
```

Let op: in deze documentatie is de shortcode expres ontsnapt met `/* ... */`, zodat Hugo hem niet uitvoert in het codeblok.

Zonder escaping zou Hugo proberen de shortcode echt te renderen.

## Gegenereerde SVG

::: vsa-notatie
[:] {/Hei_}{/lig_} is de Heer. [//:]
:::

## Wat wordt waar opgeslagen?

| Type | Voorbeeld |
|------|------------|
| gegenereerde Markdown | `generated\content\...` |
| gegenereerde SVG | `examples\hugo-demo\static\vsa\...` |
