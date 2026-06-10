---
title: "CLI: vsa svg"
---

# CLI: `vsa svg`

- [Home](/)
- [CLI overzicht](/voorbeelden/cli/)
- [Vorige: vsa validate](/voorbeelden/cli/validate/)
- [Volgende: vsa blocks](/voorbeelden/cli/blocks/)

## Waarvoor gebruik je dit?

Gebruik `vsa svg` om één `.vsa` bestand om te zetten naar één `.svg` afbeelding.

## Input

```text
[:] {/Hei_}{/lig_} is de Heer. [\\:]
```

## Commando

```cmd
vsa svg examples\minimal\valid-demo.vsa output.svg
```

## Verwachte output

```text
SVG geschreven naar: output.svg
```

## Gegenereerde SVG

::: vsa-notatie
[:] {/Hei_}{/lig_} is de Heer. [\\:]
:::

## Foutafhandeling

Als dit commando faalt, draai eerst:

```cmd
vsa validate examples\minimal\valid-demo.vsa
```
