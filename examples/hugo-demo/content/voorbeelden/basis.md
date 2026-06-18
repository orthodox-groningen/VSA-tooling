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
[:] {/Hei_}{/lig_} is de Heer. [\\:]
```

### SVG

<img class="vsa-notation" src="/vsa/voorbeelden-basis-block-1.svg" alt="VSA notatie">

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
