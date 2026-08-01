# GitHub Actions-workflows (VSA-tooling)

Overzicht van alle workflows in deze map: **wanneer** ze draaien, **waarvoor** je ze gebruikt, en wat je **lokaal** kunt doen in plaats daarvan.

## Snel kiezen

| Ik wil…                                 | Workflow                    | Hoe starten                        |
| --------------------------------------- | --------------------------- | ---------------------------------- |
| Controleren of code groen is (Windows)  | `vsa-ci.yml`                | Automatisch bij push/PR            |
| Controleren of MkDocs bouwt (Linux)     | `docs-build.yml`            | Automatisch bij push/PR            |
| Documentatiesite (MkDocs) publiceren    | `docs-pages.yml`            | Automatisch bij elke push          |
| Release-wheel/sdist + smoke-artifact    | `release-artifacts.yml`     | Actions → handmatig + versienummer |
| Pages deploy vanuit een andere org-repo | `pages-deploy-reusable.yml` | Alleen via `workflow_call`         |
| VSA renderen vanuit een andere org-repo | `vsa-render-reusable.yml`   | Alleen via `workflow_call`         |

## Wat draait automatisch bij een push?

1. **vsa-ci.yml** — Windows: checkout `bron` → bootstrap → pytest + consumer-minimal
2. **docs-build.yml** — Linux: `mkdocs build --strict`
3. **docs-pages.yml** — MkDocs → `/` (`main`) of `/preview/` (andere branches)

Handmatig: `release-artifacts`.

---

## Workflows in detail

### `docs-pages.yml` — Deploy documentation (MkDocs)

| Veld       | Waarde                                                                              |
| ---------- | ----------------------------------------------------------------------------------- |
| Trigger    | `push` (alle branches)                                                              |
| Runner     | `ubuntu-latest`                                                                     |
| Doel       | `mkdocs build --strict` → Pages `/` (`main`) of `/preview/`                         |
| Publiceert | Ja (`pages-deploy-reusable`; `keep_files: false` op main, `true` op preview)        |
| Lokaal     | `scripts\docs-serve.cmd`                                                            |

### `vsa-ci.yml` — VSA CI

| Veld       | Waarde                                                              |
| ---------- | ------------------------------------------------------------------- |
| Trigger    | `push`, `pull_request`                                              |
| Runner     | `windows-latest`                                                    |
| Doel       | Checkout `bron` + `scripts\ci.cmd` (pytest, consumer-minimal)       |
| Publiceert | Nee                                                                 |
| Lokaal     | `scripts\ci.cmd` (vereist sibling `..\bron` of `vendor\bron`)       |

### `docs-build.yml` — Docs build (MkDocs smoke)

| Veld       | Waarde                                |
| ---------- | ------------------------------------- |
| Trigger    | `push`, `pull_request`                |
| Runner     | `ubuntu-latest`                       |
| Doel       | `mkdocs build --strict` (geen deploy) |
| Publiceert | Nee                                   |
| Lokaal     | `scripts\docs-serve.cmd`              |

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
└── docs-pages.yml      → MkDocs → gh-pages:/ of /preview/

handmatig
└── release-artifacts.yml → wheel/sdist + consumer-minimal artifact
```
