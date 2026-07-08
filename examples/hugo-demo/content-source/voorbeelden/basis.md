---
title: "Basis"
---

# Basis

Een klein voorbeeld van VSA-invoer en de SVG-rendering die daaruit ontstaat.

{{< navbuttons
    "Voorbeelden | ../"
    "Volgende: Multiline | ../multiline/"
>}}

## Invoer

```text
[:] {/Hei_}{/lig_} is de Heer. [//:]
```

## Resultaat

::: vsa-notatie
[:] {/Hei_}{/lig_} is de Heer. [//:]
:::

## Uitleg

| Onderdeel | Betekenis |
|------------|-----------|
| `[:]` | openings-pitch-marker |
| `{/Hei_}` | scope met modifier |
| `is de Heer.` | gewone tekst |
| `[\\:]` | afsluitende pitch-marker |

## Commando

```cmd
vsa svg examples\minimal\valid-demo.vsa output.svg
```

## Verwachte output

```text
SVG geschreven naar: output.svg
```
