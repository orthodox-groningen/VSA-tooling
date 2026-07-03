# Parochie-lokaal — VSA-tooling

**Algemene handleiding (canoniek):** [bron/docs/manuals/parochie-lokaal-zangstukken.md](https://github.com/orthodox-groningen/bron/blob/main/docs/manuals/parochie-lokaal-zangstukken.md)

Terminologie: [bron/docs/specs/terminologie.md](https://github.com/orthodox-groningen/bron/blob/main/docs/specs/terminologie.md).

Dit document beschrijft alleen wat **specifiek voor VSA-tooling en de Hugo-demo** geldt.

---

## Demo-voorbeeld

```text
examples/hugo-demo/content-source/lokaal/antifoon-1-weekdagen/
```

---

## VSA-includes in samenstellingen

### Opgelost catalogus-pad (fase 3)

**Logische id** — aliassen per segment toegestaan:

```markdown
:::include svg id:antifoon-1-weekdagen/liturgikon-weekdagen/Hemelum alt="1e antifoon (Hemelum)":::
```

Prefix `lokaal:` of `bron:` beperkt de zoekscope; `id:` doorzoekt beide (lokaal heeft voorrang bij conflicten).

**Relatief pad** (backward compatible):

```markdown
:::include svg "../../lokaal/antifoon-1-weekdagen/liturgikon-weekdagen/hemelum/repr/hemelum.vsa" alt="1e antifoon (Hemelum)":::
```

### `:::include` met `zoek=` (catalogus)

Status: **gepland** — resolve-stap vóór build.

Normatief contract (bron): [catalogus-samenstelling-zangstuk.md](https://github.com/orthodox-groningen/bron/blob/main/docs/specs/catalogus-samenstelling-zangstuk.md).

Handleiding Rene: [sjabloon schrijven](https://github.com/orthodox-groningen/bron/blob/main/docs/manuals/catalogus/sjabloon-schrijven.md).

#### Bedoeld gedrag

1. Sjabloon of sessie-markdown bevat `:::include <exporttype> zoek="Troparion" …` —
   nog **geen** pad.
2. Frontmatter **`default.*`** levert context (`gelegenheid` in de **sessie**,
   `gelegenheidstype` in het sjabloon).
3. **`vsa resolve-catalogus`** roept **`catalogus zoek`** aan per unieke
   `zoek=`-waarde (+ exporttypes blijven aparte regels).
4. Uitvoer: dezelfde regels met **`bron:…`** / **`lokaal:…`** i.p.v. `zoek=`.
5. Pas daarna **`vsa build-markdown`** / Hugo.

**Harde regel:** open `zoek=` in een bestand dat door build-markdown gaat → **fout**.

#### Voorbeeld (invoer — sessie)

```markdown
---
default:
  gelegenheid: geboorte-moeder-gods
  gelegenheidstype: vast-feest
  uitvoeringsvorm: Groningen
---

### Kondakion

:::include svg zoek="Kondakion" alt="Kondakion":::
:::include coria zoek="Kondakion" label="Oefenen" mode="auto":::
```

#### Voorbeeld (uitvoer na resolve)

```markdown
:::include svg bron:troparion-geboorte-moeder-gods/obikhod/groningen alt="Kondakion":::
:::include coria bron:troparion-geboorte-moeder-gods/obikhod/groningen label="Oefenen" mode="auto":::
```

#### Exporttypes

| Exporttype | Status | Opmerking |
| ---------- | ------ | --------- |
| `svg` | gepland / deels | Notatie inline |
| `coria` | gepland / deels | Oefenlink |
| `mxl` | gepland | Download MusicXML |
| `mp3-player` | **gepland** | Audio-inline — contract nog in bron |

Meerdere regels met **dezelfde** `zoek=` → één catalogus-zoekactie, meerdere includes.

#### Implementatie-notities

- Parser: uitbreiding `markdown_include.py` — herken `zoek="…"` i.p.v. pad;
  weiger resolve in `build-markdown`.
- Resolve: nieuw commando **`vsa resolve-catalogus`** (of subcommando van `build-markdown --resolve-only`).
- Afhankelijkheid: `catalogus` uit bron-repo (`catalogus zoek` — nog te bouwen).

---

## `vsa resolve-catalogus`

Status: **gepland**.

Doel: markdown met **`zoek=`** omzetten naar markdown met **catalogus-pad** —
**verplichte tussenstap** vóór `vsa validate` / `vsa build-markdown` op sjablonen
en sessies.

### Bedoelde syntax

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
vsa resolve-catalogus examples\hugo-demo\content-source\samenstellingen\geboorte-moeder-gods-2026.md ^
  --content-root examples\hugo-demo\content-source ^
  --bron-root ..\bron
```

| Flag | Betekenis |
| ---- | --------- |
| `<pad.md>` | Invoer (sessie of sjabloon met `zoek=`) |
| `--content-root` | Parochie content-source (met `lokaal/`) |
| `--bron-root` | Bron-repository (`zangstukken/`) |
| `--output` | Optioneel ander uitvoerbestand; default: overschrijven invoer of `.resolved.md` |
| `--dry-run` | Alleen rapport, geen schrijven |
| `--interactive` | Review bij ambiguïteit (GUI later) |

### Wat het commando doet

1. Yaml-frontmatter parsen → **`default.*`**.
2. Alle `:::include … zoek="…"` regels vinden (niet in code fences).
3. Per `zoek=` + context: **`catalogus zoek`** (bron-package).
4. Bij unieke match: vervang `zoek="…"` door `bron:…` / `lokaal:…`.
5. Bij ambiguïteit: fout of interactieve keuze.
6. Schrijf opgelost bestand.

### Relatie tot `catalogus` CLI

| Tool | Rol |
| ---- | --- |
| `catalogus zoek "Kondakion" --default-gelegenheid …` | Lage API — één zoekactie |
| `catalogus index validate` | Index controleren vóór bulk-resolve |
| **`vsa resolve-catalogus`** | Markdown-processor voor Rene — roept `catalogus zoek` aan |

Zie [bron — catalogus CLI](https://github.com/orthodox-groningen/bron/blob/main/docs/reference/catalogus-cli.md).

### Pipeline (doel)

```text
sjabloon.md (zoek=, geen gelegenheid)
    → sessie.md (+ default.gelegenheid)
    → vsa resolve-catalogus
    → sessie-opgelost.md (bron:/lokaal:)
    → vsa validate
    → vsa build-markdown
    → Hugo
```

GUI (later): dezelfde stappen — resolve vóór preview/export.

---

## Overige markdown

Inline (kort fragment):

```markdown
::: vsa-notatie
…
:::
```

**Opmerking:** annotaties in `.vsa` als `<!-- … -->` (HTML-comment), niet als `[//:]` — dat laatste is een hoogte-markering.

---

## Build-pipeline (VSA-tooling)

| Stap | Parochie-lokaal |
| ---- | ---------------- |
| Sync bron | Niet nodig — bestanden in git |
| **`vsa resolve-catalogus`** | **Gepland** — verplicht als `zoek=` aanwezig |
| `vsa validate` | Deelt `content-source` recursief |
| `build-markdown` | Includes op pad / catalogus-pad — **geen** open `zoek=` |
| Hugo | Ongewijzigd |

Lokaal bouwen (vandaag — zonder `zoek=`):

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
scripts\build-hugo.cmd
scripts\serve-hugo.cmd
```

---

## Hugo-demo structuur

Zie [hugo-site-structure.md](hugo-site-structure.md) voor `lokaal/` naast `praktijk/` en `voorbeelden/`.
