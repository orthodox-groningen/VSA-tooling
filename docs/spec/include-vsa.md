# `@include-vsa` — VSA inline includes

Status: **geïmplementeerd** (`id=` / `lokaal=`); **`zoek=`** wacht op `catalogus.zoek` in bron.

Normatief zoek-contract: [bron — catalogus-zoek-api.md](https://github.com/orthodox-groningen/bron/blob/main/docs/specs/catalogus-zoek-api.md).

Verschil met markdown [`:::include`](../spec-vsa-document-samenstellen.md): transclusie
(aparte blokken/SVG) vs. **inline tekstsplice** in één notatiestroom. Brondocument
blijft **ongewijzigd**; expand is in-memory.

---

## Syntax (voorgesteld)

```text
refrein: @include-vsa zoek="Troparion"
refrein: @include-vsa id=troparion-geboorte-moeder-gods/obikhod/groningen
refrein: @include-vsa lokaal=troparion-geboorte-moeder-gods/obikhod/groningen
```

Parameters **`zoek=`**, **`id=`**, **`lokaal=`** — wederzijds exclusief; geen pad.

Alleen de substring `@include-vsa …` wordt vervangen; `refrein: ` blijft staan.
Lege regels aan begin/eind van de ingesloten body worden weggelaten.

---

## Catalogus / parochie-context

Zoeken draait met **`content-root`** = parochie content-source en optioneel
**`bron-root`**. **`lokaal/`** gaat vóór **`zangstukken/`** in bron — zie bron-spec
§ parochie-context.

| Parameter | Resolver |
| --------- | -------- |
| `zoek=` | `catalogus.zoek` (+ `ZoekContext` uit ouder-`.vsa` `default:`) |
| `id=` | `AliasIndex.resolve_vsa_path("id:…")` |
| `lokaal=` | `AliasIndex.resolve_vsa_path("lokaal:…")` |

---

## Ambiguïteit en waarschuwingen

| Uitkomst catalogus | `@include-vsa` / `vsa validate` |
| ------------------ | ------------------------------- |
| **`AmbiguousError`** (meerdere kandidaten) | **Fout** — geen expand |
| **`NotFoundError`** | **Fout** |
| **`ZoekResult`** met **`has_ook_in_bron`** | **Waarschuwing** — expand gaat door; auteur verifieert parochie-lokaal vs. bron |
| Eén match, geen bron-duplicaat | Geen waarschuwing |

**Auteur-workflow bij ambiguïteit:**

1. `catalogus zoek "…" --lijst --content-root … --bron-root …` (eventueel met `default.*`-flags).
2. Verfijn `zoek=` of `default.*` in ouder-`.vsa`.
3. Of schakel over naar **`@include-vsa lokaal=…`** / **`id=…`** na review.

Waarschuwingstekst (NL, indicatief): *«Ook gevonden in bron: … — controleer of
lokaal:… de bedoelde uitvoeringsvorm is.»*

---

## Context: `default:` in ouder-`.vsa`

Voor standalone samengestelde `.vsa`-bestanden (antifoon met ingesloten troparion):
`default.*` in **dezelfde** frontmatter als `@include-vsa`. Conventie:
[bron — zangstuk-formaat § parochie-samenstelling](https://github.com/orthodox-groningen/bron/blob/main/docs/specs/zangstuk-formaat.md).

Markdown-sessies gebruiken **`default.*`** in **`.md`**-frontmatter — zelfde
`ZoekContext`-sleutels, andere bronbestand-laag. Geen conflict; zie bron-spec
§ twee contextlagen.

---

## Implementatiestatus

| Onderdeel | Status |
| --------- | ------ |
| `expand_include_vsa` in [`include_vsa.py`](../../src/vsa/include_vsa.py) | **Geïmplementeerd** |
| `@include-vsa id=` / `lokaal=` | **Geïmplementeerd** |
| `@include-vsa zoek=` | **Gepland** (stub; `catalogus.zoek` nog niet live) |
| Integratie validate / svg / musicxml / build-markdown | **Geïmplementeerd** |
