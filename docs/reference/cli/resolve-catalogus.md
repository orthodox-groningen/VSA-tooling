# `vsa resolve-catalogus` — `zoek=`-includes oplossen naar catalogus-paden

Vervang `:::include <exporttype> zoek="…"` in een Markdownbestand door een
concreet catalogus-pad (`bron:…` of `lokaal:…`).

## Synopsis

```text
vsa resolve-catalogus [-h] [--content-root CONTENT_ROOT] [--bron-root BRON_ROOT]
                       [-o OUTPUT] [--dry-run] path
```

## Beschrijving

Sjablonen en sessie-Markdown mogen `:::include <exporttype> zoek="…"` bevatten
zonder al een concreet pad — bijvoorbeeld `:::include svg zoek="Kondakion" alt="Kondakion":::`.
`vsa resolve-catalogus` lost deze op naar een catalogus-pad door `catalogus zoek`
(uit de `catalogus`-package van de `bron`-repo) aan te roepen, en schrijft
een nieuwe versie van het bestand waarin `zoek="…"` is vervangen door
`bron:…` of `lokaal:…`.

**Harde regel:** een bestand met een nog-open `zoek=`-include mag niet door
[`vsa build-markdown`](build-markdown.md) — dat commando weigert het bestand
(behalve bij automatische resolve voor publishbare paden). Draai daarom
`vsa resolve-catalogus` als tussenstap vóór [`vsa validate`](validate.md) /
`vsa build-markdown` op sjablonen en sessies die niet automatisch worden
opgelost.

### Wat het commando doet

1. YAML-frontmatter parsen → `default.*` (bijv. `default.gelegenheid`,
   `default.gelegenheidstype`) levert zoekcontext.
2. Alle `:::include <svg|coria|mxl> zoek="…"`-regels vinden (niet binnen
   code fences).
3. Per unieke `zoek=`-waarde + context: één aanroep van `catalogus zoek`.
4. Bij een unieke match: vervang `zoek="…"` door `bron:…` of `lokaal:…`.
5. Bij ambiguïteit: fout (`AmbiguousError`) — review handmatig via
   `catalogus zoek --lijst` (interactieve review is gepland, nog niet
   geïmplementeerd).
6. Schrijf het opgeloste bestand.

Dit commando vereist de `catalogus`-package uit de `bron`-repo. Zonder die
package meldt het commando een fout dat `catalogus` niet beschikbaar is.

## Argumenten en opties

| Naam                          | Verplicht | Betekenis                                                                       | Default                                                                | Beperkingen                     |
| ----------------------------- | --------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------- |
| `path`                        | Ja        | Markdown-bestand met `zoek=`-includes.                                          | —                                                                      | Moet een bestaand bestand zijn. |
| `--content-root CONTENT_ROOT` | Nee       | Parochie content-source-root (met `lokaal/`-map), gebruikt voor lokale matches. | Auto-detectie: eerste bovenliggende map met een `lokaal/`-submap       | —                               |
| `--bron-root BRON_ROOT`       | Nee       | Root van de `bron`-repository (met `zangstukken/`).                             | Auto-detectie via `vendor/bron` of `..\bron`                           | —                               |
| `-o`, `--output OUTPUT`       | Nee       | Uitvoerbestand.                                                                 | Overschrijft `path` (of `<naam>.resolved.md` afhankelijk van workflow) | —                               |
| `--dry-run`                   | Nee       | Toon het resultaat zonder het bestand te schrijven.                             | Uit                                                                    | —                               |
| `-h`, `--help`                | Nee       | Toon hulp voor dit subcommando.                                                 | —                                                                      | —                               |

## Output

- **stdout**: `Opgelost: <n> unieke zoek= (<lijst>)` of
  `Geen zoek= includes gevonden.`; bij `--dry-run` extra de regel
  `(dry-run — bestand niet geschreven)`.
- **stderr**: waarschuwingen per regel, vorm
  `<path>:<regel>: WARNING: <code>: <uitleg>` (bijvoorbeeld
  `CATALOGUS-ZOEK-BRON-HINT` als een zoekterm zowel lokaal als in `bron`
  voorkomt).
- **Bestand**: het opgeloste Markdown-bestand wordt geschreven naar `--output`
  of, zonder die optie, teruggeschreven naar `path` — behalve bij `--dry-run`.

## Exit status

| Exitcode | Betekenis                                                               |
| -------- | ----------------------------------------------------------------------- |
| `0`      | Alle `zoek=`-includes opgelost (of geen includes gevonden).             |
| `1`      | Bestand niet gevonden, lege `zoek=`, ambiguïteit, of geen unieke match. |

## Voorbeelden — succes

Voorbeeldinvoer (sessie-Markdown met `zoek=`, zie
[parochie-lokaal-vsa.md](../../guides/parochie-lokaal-vsa.md)):

```markdown
---
default:
  gelegenheid: geboorte-moeder-gods
  gelegenheidstype: vast-feest
---

### Kondakion

:::include svg zoek="Kondakion" alt="Kondakion":::
:::include coria zoek="Kondakion" label="Oefenen" mode="auto":::
```

Commando:

```cmd
vsa resolve-catalogus content-source\samenstellingen\geboorte-moeder-gods.md ^
  --content-root content-source ^
  --bron-root ..\bron
```

Verwachte output:

```text
Opgelost: 1 unieke zoek= (Kondakion)
```

Resultaat in het (overschreven) bestand:

```markdown
:::include svg bron:kondak-geboorte-moeder-gods/kondak-geboorte-moeder-gods/liturgikon alt="Kondakion":::
:::include coria bron:kondak-geboorte-moeder-gods/kondak-geboorte-moeder-gods/liturgikon label="Oefenen" mode="auto":::
```

Met `--dry-run` blijft het bronbestand ongewijzigd en verschijnt extra:

```text
(dry-run — bestand niet geschreven)
```

## Voorbeelden — falen

Een lege `zoek=`-waarde:

```markdown
:::include svg zoek="" alt="x":::
```

Verwachte output (stderr):

```text
content-source\bad.md:1: Lege zoek= waarde in include.
```

Exitcode: `1`. Fix: vul een niet-lege zoekterm in.

Zonder content-root of bron-root vindbaar (geen `lokaal/`-map in een
bovenliggende map en geen `vendor/bron`/`../bron`):

```text
Geen content-root of bron-root; geef --content-root en/of --bron-root op.
```

Exitcode: `1`. Fix: geef `--content-root` en/of `--bron-root` expliciet op.

Bij ambiguïteit (meerdere zangstukken matchen dezelfde zoekterm + context)
stopt het commando met een foutmelding van `catalogus zoek`. Fix: gebruik
`catalogus zoek --lijst` (in de `bron`-repo) om de kandidaten te bekijken en
verfijn de zoekterm of `default.*`-context.

## Relatie tot `catalogus` CLI

| Tool                                                       | Rol                                                                 |
| ---------------------------------------------------------- | ------------------------------------------------------------------- |
| `catalogus zoek "Kondakion" --default-gelegenheid …`       | Lage-niveau API — één zoekactie.                                    |
| `catalogus index validate`                                 | Index controleren vóór bulk-resolve.                                |
| `vsa resolve-catalogus`                                    | Markdown-processor die `catalogus zoek` per `zoek=`-regel aanroept. |

## Zie ook

- [`vsa build-markdown`](build-markdown.md) — volgende stap in de pipeline; weigert open `zoek=`.
- [`vsa validate`](validate.md) — draai na resolve om het opgeloste bestand te controleren.
- Handleiding: [parochie-lokaal-vsa.md](../../guides/parochie-lokaal-vsa.md)
- Bron-contract (normatief): [catalogus-samenstelling-zangstuk.md](https://github.com/orthodox-groningen/bron/blob/main/docs/specs/catalogus-samenstelling-zangstuk.md), [catalogus-cli](https://github.com/orthodox-groningen/bron/blob/main/docs/reference/catalogus-cli.md)
