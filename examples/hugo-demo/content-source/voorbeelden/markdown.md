---
title: "Markdown en Hugo"
---

# Markdown en Hugo

Een voorbeeld van VSA in Markdown en de output die de Hugo-demo gebruikt.

{{< navbuttons
    "Vorige: Fouten | ../fouten/"
    "Voorbeelden | ../"
    "Volgende: CLI | ../cli/"
>}}

## Invoer

````markdown
::: vsa-notatie
[:] {/Hei_}{/lig_} is de Heer. [//:]
:::
````

## Commando

```cmd
vsa build-markdown examples\hugo-demo\content-source generated\content examples\hugo-demo\static\vsa
```

## Resultaat

Als de demo-site met shortcode-output wordt gebouwd, komt er in de gegenereerde Markdown ongeveer dit te staan:

```go-html-template
{{</* vsa src="/vsa/demo-block-1.svg" */>}}
```

Let op: in deze documentatie is de shortcode expres ontsnapt met `/* ... */`, zodat Hugo hem niet uitvoert in het codeblok.

Zonder escaping zou Hugo proberen de shortcode echt te renderen.

De gegenereerde SVG ziet er in de pagina zo uit:

::: vsa-notatie
[:] {/Hei_}{/lig_} is de Heer. [//:]
:::

## Uitleg

| Type | Voorbeeld |
|------|------------|
| gegenereerde Markdown | `generated\content\...` |
| gegenereerde SVG | `examples\hugo-demo\static\vsa\...` |
