# GitHub Actions-workflows (VSA-tooling)

Overzicht van alle workflows in deze map: **wanneer** ze draaien, **waarvoor** je ze gebruikt, en wat je **lokaal** kunt doen in plaats daarvan.

## Snel kiezen

| Ik wil…                                   | Workflow                    | Hoe starten                        |
| ----------------------------------------- | --------------------------- | ---------------------------------- |
| Controleren of code groen is (Windows)    | `vsa-ci.yml`                | Automatisch bij push/PR            |
| Controleren of MkDocs bouwt (Linux)       | `docs-build.yml`            | Automatisch bij push/PR            |
| Live preview van de Hugo-demo             | `pages-preview.yml`         | Automatisch bij elke push          |
| Documentatiesite (MkDocs) publiceren      | `docs-pages.yml`            | Automatisch bij elke push          |
| Productie Hugo-demo publiceren            | `pages-demo.yml`            | Actions → handmatig Run workflow   |
| Release-wheel/sdist + smoke-artifact      | `release-artifacts.yml`     | Actions → handmatig + versienummer |
| Pages deploy vanuit een andere org-repo   | `pages-deploy-reusable.yml` | Alleen via `workflow_call`         |
| VSA renderen vanuit een andere org-repo   | `vsa-render-reusable.yml`   | Alleen via `workflow_call`         |

## Wat draait automatisch bij een push?

1. **vsa-ci.yml** — Windows: pytest + validate/build-markdown op `examples/consumer-minimal`
2. **docs-build.yml** — Linux: `mkdocs build --strict`
3. **pages-preview.yml** — Hugo-preview → `/preview/` (tot uitkleed-fase 4)
4. **docs-pages.yml** — MkDocs → `/docs/` of `/docs-preview/`

Handmatig: `pages-demo`, `release-artifacts`.

---

## Workflows in detail

### `docs-pages.yml` — Deploy documentation (MkDocs)

| Veld       | Waarde                                                             |
| ---------- | ------------------------------------------------------------------ |
| Trigger    | `push` (alle branches)                                             |
| Runner     | `ubuntu-latest`                                                    |
| Doel       | `mkdocs build --strict` → Pages `/docs/` of `/docs-preview/`       |
| Publiceert | Ja (`pages-deploy-reusable`, `keep_files: true`)                   |
| Lokaal     | `scripts\docs-serve.cmd`                                           |

### `vsa-ci.yml` — VSA CI

| Veld       | Waarde                                                                      |
| ---------- | --------------------------------------------------------------------------- |
| Trigger    | `push`, `pull_request`                                                      |
| Runner     | `windows-latest`                                                            |
| Doel       | `scripts\ci.cmd`: pytest + consumer-minimal validate/build-markdown         |
| Publiceert | Nee                                                                         |
| Lokaal     | `scripts\ci.cmd`                                                            |

### `docs-build.yml` — Docs build (MkDocs smoke)

| Veld       | Waarde                                |
| ---------- | ------------------------------------- |
| Trigger    | `push`, `pull_request`                |
| Runner     | `ubuntu-latest`                       |
| Doel       | `mkdocs build --strict` (geen deploy) |
| Publiceert | Nee                                   |
| Lokaal     | `scripts\docs-serve.cmd`              |

Vervangt de voormalige Hugo-`site-build.yml`.

### `pages-preview.yml` / `pages-demo.yml`

Hugo-demo Pages (tijdelijk tot fase 4 van uitkleden). Presentatiemodel:
[VSA-demo](https://github.com/orthodox-groningen/VSA-demo).

### `release-artifacts.yml`

pytest + wheel/sdist + build van `examples/consumer-minimal`.

### `pages-deploy-reusable.yml` / `vsa-render-reusable.yml`

Ongewijzigd herbruikbaar voor org-repo's. Zie [reuse-vsa-tooling.md](../../docs/guides/reuse-vsa-tooling.md).

---

## Diagram

```text
push / pull_request
├── vsa-ci.yml          → pytest + consumer-minimal (Windows)
├── docs-build.yml      → mkdocs --strict (Linux)
├── pages-preview.yml   → Hugo preview → gh-pages:/preview/  (tot fase 4)
└── docs-pages.yml      → MkDocs → gh-pages:/docs/ of /docs-preview/

handmatig
├── pages-demo.yml      → Hugo productie (tot fase 4)
└── release-artifacts.yml → wheel/sdist + consumer-minimal artifact
```
