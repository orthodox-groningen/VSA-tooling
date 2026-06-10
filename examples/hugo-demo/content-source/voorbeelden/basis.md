---
title: "Basisvoorbeelden"
---

# Basisvoorbeelden

- [Home](/)
- [Voorbeelden](/voorbeelden/)
- [Volgende: Multiline](/voorbeelden/multiline/)

## Voorbeeld 1

### Invoer

```text
[:] {/Hei_}{/lig_} is de Heer. [:]
```

### SVG

::: vsa-notatie
[:] {/Hei_}{/lig_} is de Heer. [:]
:::

### Wat gebeurt hier?

| Onderdeel | Betekenis |
|------------|-----------|
| `[:]` | pitch-marker |
| `{/Hei_}` | scope met modifier |
| `is de Heer.` | gewone tekst |

## Commando

```cmd
vsa svg examples\minimal\050_svg_demo.vsa output.svg
```

## Verwachte output

```text
SVG geschreven naar: output.svg
```
