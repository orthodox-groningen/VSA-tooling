# `@include-vsa` — VSA inline includes

Status: **geïmplementeerd** (`id=` / `lokaal=` / **`zoek=`**).

Normatief zoek-contract (bron): [catalogus-zoek-api.md](https://github.com/orthodox-groningen/bron/blob/main/docs/specs/catalogus-zoek-api.md).

---

## Syntax

In VSA-notatie (één regel):

```vsa
refrein: @include-vsa zoek="Troparion"
refrein: @include-vsa id=troparion-geboorte-moeder-gods/troparion-geboorte-moeder-gods/liturgikon
refrein: @include-vsa lokaal=cherubijnenhymne/kastorski/groningen/groningen-vsa
```

Parameters **`zoek=`**, **`id=`**, **`lokaal=`** — wederzijds exclusief; geen pad.

Alleen de substring `@include-vsa …` wordt vervangen; `refrein: ` blijft staan.

---

## Resolve

| Parameter | Bron |
| --------- | ---- |
| `id=` | `catalogus` — beide herkomsten; lokaal wint bij conflict |
| `lokaal=` | `catalogus` — parochie `lokaal/` |
| `zoek=` | `catalogus.zoek` (+ `ZoekContext` uit ouder-`.vsa` `default:`) |

Expand: lees doel-`.vsa`, strip frontmatter, splice body **in-memory** (brondocument ongewijzigd).

| Uitkomst catalogus | `@include-vsa` / `vsa validate` |
| ------------------ | ------------------------------- |
| Geen match | **Fout** |
| Meerdere matches | **Fout** (`AmbiguousError`) |
| Eén match + `ook_gevonden_in_bron` | **Waarschuwing** (build mag doorgaan) |

Bij ambiguïteit:

1. `catalogus zoek --lijst` met dezelfde context.
2. Verfijn `zoek=` of `default.*` in ouder-`.vsa`.
3. Of schakel over naar **`@include-vsa lokaal=…`** / **`id=…`** na review.

---

## Context (`default.*`)

`default.*` in **dezelfde** frontmatter als `@include-vsa`. Conventie:

- **`zoek=`** in sjablonen/sessies: liturgische rol in de zoekstring; feest in `default.gelegenheid`.
- **`@include-vsa zoek=`** in `.vsa`: context uit **ouder**-`.vsa` frontmatter.

Zie [catalogus-zoek-api — twee contextlagen](https://github.com/orthodox-groningen/bron/blob/main/docs/specs/catalogus-zoek-api.md).

---

## Implementatiestatus

| Onderdeel | Status |
| --------- | ------ |
| `expand_include_vsa` in [`include_vsa.py`](../../src/vsa/include_vsa.py) | **Geïmplementeerd** |
| `@include-vsa id=` / `lokaal=` | **Geïmplementeerd** |
| `@include-vsa zoek=` | **Geïmplementeerd** |
| Integratie validate / svg / musicxml / build-markdown | **Geïmplementeerd** |
