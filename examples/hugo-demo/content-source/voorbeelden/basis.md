---
title: "Basisvoorbeelden"
---

# Basisvoorbeelden

- [Home](../../)
- [Voorbeelden](../)
- [Volgende: Multiline](../multiline/)

## Voorbeeld 1

### Invoer

```text
[:] {/Hei_}{/lig_} is de Heer. [//:]
```

### SVG

::: vsa-notatie
[:] {/Hei_}{/lig_} is de Heer. [//:]
:::

### Wat gebeurt hier?

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
