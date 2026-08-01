# AGENTS.md

Richtlijnen voor AI-assistenten in
[orthodox-groningen/VSA-tooling](https://github.com/orthodox-groningen/VSA-tooling).

Organisatie-context (andere repo's, terminologie): zie
[bron/AGENTS.md](https://github.com/orthodox-groningen/bron/blob/main/AGENTS.md).

---

## Projectoverzicht

VSA-tooling is de **Python-toolchain** voor Vereenvoudigde Slavische Accentnotatie:

- parser en semantische validator;
- CLI (`vsa`): validate, parse, blocks, build-markdown, svg, musicxml, …;
- MkDocs-documentatie op GitHub Pages; presentatievoorbeeld in
  [VSA-demo](https://github.com/orthodox-groningen/VSA-demo);
- regressietests en GitHub Actions CI (inclusief herbruikbare render-workflow).

**Normatieve org-specs staan in `bron`** — link ernaar, dupliceer niet. Tool-specifieke
documentatie hoort in `docs/specification/`, `docs/guides/` en `docs/plans/`.

---

## Terminologie (orthodox-groningen)
 
Normatieve glossary:
[bron/docs/specs/terminologie.md](https://github.com/orthodox-groningen/bron/blob/main/docs/specs/terminologie.md)

Vier niveaus: `zangstuk-id` → `variant-id` → `uitvoeringsvorm-id` → `representatie-id`

Regels R1–R5 en documentatie-eigendom: zie
[documentatie-eigendom](https://github.com/orthodox-groningen/bron/blob/main/docs/specs/documentatie-eigendom.md)
en `.cursor/rules/orthodox-groningen-terminologie.mdc`.

**Vermijden:** `uv-id`, afkorting `uv`, **uitvoeringsalternatief**, impliciet `variant-id: standaard`.

---

## LLM Coding Guidelines

<!-- Gebaseerd op https://github.com/multica-ai/andrej-karpathy-skills -->

Gedragsrichtlijnen om veelvoorkomende LLM-fouten te verminderen. Bij triviale taken: gebruik je oordeel.

### 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:

- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them — don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

### 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

### 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

- Don't "improve" adjacent code, comments, or formatting.
- Match existing style, even if you'd do it differently.
- Remove orphans only from **your** changes; don't delete pre-existing dead code unless asked.

### 4. Goal-Driven Execution

Define verifiable success criteria (tests, validate, build) and loop until they pass.

---

## Ontwikkelomgeving

| Vereiste | Versie / tool                                                                     |
| -------- | --------------------------------------------------------------------------------- |
| Python   | ≥ 3.12                                                                            |
| venv     | `.venv` (via bootstrap)                                                           |
| Tests    | pytest                                                                            |
| Docs     | MkDocs Material (`requirements-docs.txt`)                                         |
| bron     | checkout onder `vendor/bron` of sibling `../bron` (CI; **catalogus**-pakket)      |

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
scripts\bootstrap.cmd
```

`bootstrap.cmd` installeert **catalogus** uit `vendor\bron` of `..\bron` vóór `vsa-tool`
(verplicht — PyPI heeft een andere package met dezelfde naam).

**Rendering (SVG):** `pip install -r requirements-rendering.txt` (Pillow, DejaVu in `assets/fonts/`).

**Commando's voor de gebruiker:** één kopieerbaar cmd-blok, Windows-paden (`\`), begin met `cd /d`.

---

## Build, lint en test

### Tests

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
scripts\test.cmd
```

Verbose: `scripts\test-verbose.cmd`

### Volledige CI lokaal

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
scripts\ci.cmd
```

Stappen: pytest → `vsa validate` + `build-markdown` op
`examples\consumer-minimal\content-source` → output in `generated\ci\`.

### VSA CLI (typisch)

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
call .venv\Scripts\activate
vsa validate examples\consumer-minimal\content-source
vsa build-markdown examples\consumer-minimal\content-source generated\ci\content generated\ci\static\vsa
```

### Voorbeeldconsumer (VSA-demo)

Presentatiesite: [VSA-demo](https://github.com/orthodox-groningen/VSA-demo).

```cmd
cd /d C:\Git\orthodox-groningen\VSA-demo
scripts\bootstrap.cmd
scripts\serve-hugo.cmd
```

Opruimen in deze repo: `scripts\clean.cmd`. Overzicht scripts: `scripts/README.md`.

### Documentatiesite (MkDocs)

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
scripts\docs-build-tev2.cmd
```

Of zonder TEv2 (alleen serve): `scripts\docs-serve.cmd`.
CI/deploy: `.github/workflows/docs-pages.yml` → TEv2 + `gh-pages:/` (`main`) of `/preview/`.

---

## Architectuur

```
src/vsa/                       # parser, validator, renderers, CLI
tests/                         # pytest
examples/minimal|regression|edge-cases|consumer-minimal/
docs/specification/            # Normatieve VSA-specificatie
docs/guides/                   # Taakgerichte handleidingen
docs/manuals/                  # MkDocs-handleidingen
docs/plans/                    # Plannen en toekomstvoorstellen
docs/history/                  # Ontwerpgeschiedenis (niet op Pages)
generated/                     # build-output — niet handmatig redigeren
vendor/bron/                   # bron-checkout (CI)
```

Specificatie: `docs/specification/`. Consumer-integratie: `docs/manuals/consumer-site.md`.
Hergebruik: `docs/guides/reuse-vsa-tooling.md`.

### Belangrijke grenzen

- Scripts mogen redactionele `content-source` niet herschrijven.
- Wijzig normatieve terminologie via PR op **bron**, niet in stubs hier.
- Afgeleide output hoort in `generated/` of consumer-`static/vsa`, niet in `bron`.

---

## Git commits

[Conventional Commits](https://www.conventionalcommits.org/). Typische scopes: `vsa`, `parser`, `svg`, `ci`, `docs`.

```
feat(vsa): voeg MusicXML-export voor compound-melisma toe
test(parser): regressie voor height-marker policy
```

**Maak alleen commits wanneer de gebruiker dat expliciet vraagt.**

---

## Pull requests

Gebruik **`gh` CLI**. Stel titel, body en `gh pr create`-commando **voor aan de gebruiker** vóór uitvoering.

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
git push -u origin HEAD
gh pr create --title "feat(vsa): korte beschrijving" --body "## Summary
- …

## Test plan
- [ ] vsa validate examples\consumer-minimal\content-source
- [ ] scripts\test.cmd
"
```

---

## CI/CD

Overzicht **wanneer welke workflow** draait: [.github/workflows/README.md](.github/workflows/README.md).

| Workflow                    | Doel                                                      |
| --------------------------- | --------------------------------------------------------- |
| `vsa-ci.yml`                | Windows: `scripts\ci.cmd` (pytest, consumer-minimal)      |
| `docs-build.yml`            | Linux: `mkdocs build --strict`                            |
| `docs-pages.yml`            | MkDocs docs → `/` of `/preview/` (elke push)              |
| `release-artifacts.yml`     | Release-package + consumer-minimal artifact (handmatig)   |
| `pages-deploy-reusable.yml` | Herbruikbare Pages-deploy voor org-repo's                 |
| `vsa-render-reusable.yml`   | Herbruikbaar VSA-renderen voor andere org-repo's          |

CI checkt `bron` uit naar `vendor/bron` (`ref: main`).

---

## Cursor-regels

| Regel                                 | Doel                             |
| ------------------------------------- | -------------------------------- |
| `orthodox-groningen-terminologie.mdc` | Glossary + R1–R5                 |
| `copy-pasteable-cli-commands.mdc`     | cmd-blokken voor gebruiker       |
| `markdown-table-layout.mdc`           | Tabel-alignment in markdown-bron |

Na bulk-tabellen: `python scripts/align_markdown_tables.py <pad>`.

---

## Extern hergebruik

```cmd
python -m pip install "vsa-tool[rendering] @ git+https://github.com/orthodox-groningen/VSA-tooling.git@main"
```

Zie `docs/guides/reuse-vsa-tooling.md`.
