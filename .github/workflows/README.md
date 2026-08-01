# GitHub Actions-workflows (VSA-tooling)

Overzicht van alle workflows in deze map: **wanneer** ze draaien, **waarvoor** je ze gebruikt, en wat je **lokaal** kunt doen in plaats daarvan.

Normatieve CI-architectuur: [docs/architecture/ci-reliability.md](../../docs/architecture/ci-reliability.md).

## Snel kiezen

| Ik wil…                                   | Workflow                    | Hoe starten                        |
| ----------------------------------------- | --------------------------- | ---------------------------------- |
| Controleren of code groen is (Windows)    | `vsa-ci.yml`                | Automatisch bij push/PR            |
| Controleren of de Hugo-site bouwt (Linux) | `site-build.yml`            | Automatisch bij push/PR            |
| Live preview van mijn branch bekijken     | `pages-preview.yml`         | Automatisch bij elke push          |
| Productie-site publiceren                 | `pages-demo.yml`            | Actions → handmatig Run workflow   |
| Release-wheel/sdist + demo-artifact maken | `release-artifacts.yml`     | Actions → handmatig + versienummer |
| Pages deploy vanuit een andere org-repo   | `pages-deploy-reusable.yml` | Alleen via `workflow_call`         |
| VSA renderen vanuit een andere org-repo   | `vsa-render-reusable.yml`   | Alleen via `workflow_call`         |

## Wat draait automatisch bij een push?

Op **elke push** (alle branches) starten typisch drie workflows parallel:

1. **vsa-ci.yml** — Windows-tooling (`scripts\ci.cmd`)
2. **site-build.yml** — Linux Hugo-build (preview-config; op `main` productie-instellingen)
3. **pages-preview.yml** — bouwt en publiceert naar [preview-URL](https://orthodox-groningen.github.io/VSA-tooling/preview/)

De preview-URL toont altijd de **laatst gepushte** commit (welke branch dan ook). Zo kun je per branch controleren of die deployable is.

Handmatige workflows (`pages-demo`, `release-artifacts`) start je zelf in GitHub onder **Actions**.

---

## Workflows in detail

### `vsa-ci.yml` — VSA CI

| Veld        | Waarde                                                                        |
| ----------- | ----------------------------------------------------------------------------- |
| Trigger     | `push`, `pull_request`                                                        |
| Runner      | `windows-latest`                                                              |
| Doel        | Canonieke Windows-CI: pytest, bron-sync, `vsa validate`, `vsa build-markdown` |
| Publiceert  | Nee                                                                           |
| Lokaal      | `scripts\ci.cmd`                                                              |

Gebruik dit als referentie voor “is de tooling op Windows in orde?”. Draait geen volledige Hugo-site en geen Pages-deploy.

---

### `site-build.yml` — Site build

| Veld        | Waarde                                                                                                    |
| ----------- | --------------------------------------------------------------------------------------------------------- |
| Trigger     | `push`, `pull_request`                                                                                    |
| Runner      | `ubuntu-latest`                                                                                           |
| Doel        | Volledige site-pipeline zonder deploy: pytest, sync bron, validate, shortcode-build, MusicXML, TEv2, Hugo |
| Target      | Op `main`: productie-instellingen (`--minify`, bredere SVG); anders preview                               |
| Artefacten  | `site-preview` / `site-production`, plus content- en SVG-artifacts                                        |
| Publiceert  | Nee                                                                                                       |
| Lokaal      | `scripts\build-preview.cmd` of `scripts\build-production.cmd`                                             |

Gebruik dit om te verifiëren dat de Hugo-demo bouwt vóór je handmatig productie publiceert.

---

### `pages-preview.yml` — Deploy preview to GitHub Pages

| Veld        | Waarde                                                                              |
| ----------- | ----------------------------------------------------------------------------------- |
| Trigger     | `push` (alle branches)                                                              |
| Runner      | `ubuntu-latest`                                                                     |
| Doel        | Bouw preview-site en push naar `gh-pages:/preview/` (peaceiris, `keep_files: true`) |
| URL         | https://orthodox-groningen.github.io/VSA-tooling/preview/                           |
| Publiceert  | Ja (alleen map `preview/`)                                                          |
| Lokaal      | `scripts\build-preview.cmd` (zonder deploy)                                         |

Geen pytest (al gedekt door `vsa-ci` en `site-build`). Na build roept de deploy-job `pages-deploy-reusable.yml` aan.

---

### `pages-demo.yml` — Deploy Hugo demo to GitHub Pages (productie)

| Veld        | Waarde                                                                       |
| ----------- | ---------------------------------------------------------------------------- |
| Trigger     | `workflow_dispatch` (handmatig)                                              |
| Runner      | `ubuntu-latest`                                                              |
| Doel        | Productie-build + push naar `gh-pages:/` (root); map `preview/` blijft staan |
| URL         | https://orthodox-groningen.github.io/VSA-tooling/                            |
| Publiceert  | Ja (site-root)                                                               |
| Lokaal      | `scripts\build-production.cmd` (zonder deploy)                               |

Start alleen als `main` (of de te publiceren commit) al groen is op `vsa-ci` en `site-build`. Draait wél pytest vóór deploy.

**Starten:** Actions → *Deploy Hugo demo to GitHub Pages* → Run workflow.

---

### `release-artifacts.yml` — Release artifacts

| Veld        | Waarde                                                                        |
| ----------- | ----------------------------------------------------------------------------- |
| Trigger     | `workflow_dispatch` + invoer `version` (bijv. `0.1.0`)                        |
| Runner      | `ubuntu-latest`                                                               |
| Doel        | pytest, Python-package (`dist/`), gegenereerde demo-markdown/SVG als download |
| Publiceert  | Nee (alleen artifacts in Actions)                                             |
| Lokaal      | `python -m build` na `scripts\test.cmd`                                       |

Voor een release-tag of distributie buiten GitHub Pages.

**Starten:** Actions → *Release artifacts* → Run workflow → versie invullen.

---

### `pages-deploy-reusable.yml` — Reusable GitHub Pages deploy

| Veld          | Waarde                                                               |
| ------------- | -------------------------------------------------------------------- |
| Trigger       | `workflow_call` (niet handmatig)                                     |
| Doel          | Artifact downloaden, publicatiecheck, peaceiris-push naar `gh-pages` |
| Gebruikt door | `pages-preview.yml`, `pages-demo.yml`, `bron` (`docs-pages.yml`)     |

Niet zelf starten. Andere repo's kunnen deze workflow aanroepen; zie [reuse-vsa-tooling.md](../../docs/guides/reuse-vsa-tooling.md).

**Pages-instelling per repo:** Deploy from a branch → `gh-pages` → `/` (niet “GitHub Actions”).

---

### `vsa-render-reusable.yml` — Reusable VSA render

| Veld          | Waarde                                                                       |
| ------------- | ---------------------------------------------------------------------------- |
| Trigger       | `workflow_call` (niet handmatig)                                             |
| Doel          | `vsa validate` + `vsa build-markdown` + SVG; upload artifact `vsa-generated` |
| Gebruikt door | Toekomstige parochie-/koor-repo's in CI                                      |

Installeert `vsa-tool[rendering]` vanaf deze repo. Zie [reuse-vsa-tooling.md](../../docs/guides/reuse-vsa-tooling.md).

---

## Diagram (vereenvoudigd)

```text
push / pull_request
├── vsa-ci.yml          → pytest + validate (Windows)
├── site-build.yml      → Hugo-build + artifacts (Linux)
└── pages-preview.yml   → preview deploy → gh-pages:/preview/

handmatig
├── pages-demo.yml      → productie deploy → gh-pages:/
└── release-artifacts.yml → wheel/sdist + demo-artifacts

workflow_call (andere repo's)
├── pages-deploy-reusable.yml
└── vsa-render-reusable.yml
```

## Niet meer in gebruik (opgeruimd 2026-07)

`python-tests.yml`, `hugo-demo.yml`, `build-artifacts.yml`, `build-target.yml`, `hugo.yml` — vervangen door `vsa-ci.yml` en `site-build.yml`.
