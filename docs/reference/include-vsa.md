# `@include-vsa` referentie

Status: geïmplementeerd voor `id=`, `lokaal=` en `zoek=`.

## Syntax

```vsa
refrein: @include-vsa zoek="Troparion"
refrein: @include-vsa id=troparion-geboorte-moeder-gods/troparion-geboorte-moeder-gods/liturgikon
refrein: @include-vsa lokaal=cherubijnenhymne/kastorski/groningen/groningen-vsa
```

## Parameters

| Parameter | Bron                                  | Opmerking                    |
| --------- | ------------------------------------- | ---------------------------- |
| `id=`     | Catalogus; beide herkomsten           | Lokaal wint bij conflict     |
| `lokaal=` | Catalogus; parochie `lokaal/`         | Lokale bron                  |
| `zoek=`   | `catalogus.zoek` + `ZoekContext`      | Context uit ouder-`.vsa`     |

De parameters zijn wederzijds exclusief.

Alleen de substring `@include-vsa ...` wordt vervangen; tekst ervoor blijft staan.

## Resolve-contract

| Uitkomst catalogus                 | Gedrag bij `@include-vsa` / `vsa validate` |
| ---------------------------------- | ------------------------------------------ |
| Geen match                         | Fout                                       |
| Meerdere matches                   | Fout (`AmbiguousError`)                    |
| Eén match + `ook_gevonden_in_bron` | Waarschuwing; build mag doorgaan           |

## Expand

De doel-`.vsa` wordt gelezen, frontmatter wordt gestript en de body wordt in-memory ingevoegd.

Het brondocument wordt niet gewijzigd.

## Ambiguïteit oplossen

1. Draai [`catalogus zoek --lijst`](https://orthodox-ronl.github.io/bron/reference/catalogus-cli/#catalogus-zoek) met dezelfde context.
2. Verfijn `zoek=` of `default.*` in de ouder-`.vsa`.
3. Schakel na review over naar `@include-vsa lokaal=...` of `id=...`.

## Implementatiestatus

| Onderdeel                                             | Status             |
| ----------------------------------------------------- | ------------------ |
| `expand_include_vsa`                                  | Geïmplementeerd    |
| `@include-vsa id=`                                    | Geïmplementeerd    |
| `@include-vsa lokaal=`                                | Geïmplementeerd    |
| `@include-vsa zoek=`                                  | Geïmplementeerd    |
| Integratie validate / svg / musicxml / build-markdown | Geïmplementeerd    |
