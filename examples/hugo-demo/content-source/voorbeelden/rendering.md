---
title: "Rendering"
---

# Rendering

- [Home](/)
- [Vorige: CLI](/voorbeelden/cli/)
- [Voorbeelden-overzicht](/voorbeelden/)

## SVG renderer

De renderer zet de parserstructuur om naar SVG.

## Voorbeeld

::: vsa-notatie
[:] {/Hei_}{/lig_} is de Heer. [:]
:::

## Huidige status

| Onderdeel | Status |
|------------|--------|
| multiline rendering | aanwezig |
| automatische afbreking | aanwezig |
| SVG-export | aanwezig |
| MusicXML-export | nog niet aanwezig |
| definitieve typografie | nog in ontwikkeling |

## Waarom regressietests?

Kleine layoutwijzigingen kunnen rendering breken.

Daarom bestaan:

```text
tests/
examples/regression/
```
