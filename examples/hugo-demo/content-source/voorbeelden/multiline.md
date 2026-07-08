---
title: "Multiline"
---

# Multiline

Een voorbeeld waarin een langere VSA-regel automatisch over meerdere regels kan worden gezet.

{{< navbuttons
    "Vorige: Basis | ../basis/"
    "Voorbeelden | ../"
    "Volgende: Fouten | ../fouten/"
>}}

## Invoer

```text
[:] {/Hei_}{/lig_} is de Heer en Hij is heilig en wonderbaar in al Zijn werken. [//:]
```

## Resultaat

::: vsa-notatie
[:] {/Hei_}{/lig_} is de Heer en Hij is heilig en wonderbaar in al Zijn werken. [//:]
:::

## Commando

```cmd
vsa svg examples\minimal\100_multiline_demo.vsa output.svg --max-line-width 400
```

## Uitleg

De renderer breekt regels automatisch af als ze te breed worden.
