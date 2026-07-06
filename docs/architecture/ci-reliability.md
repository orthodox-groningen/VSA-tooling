# CI-betrouwbaarheid (VSA-tooling)

Strategie om GitHub Actions-fouten te verminderen. Doel: **falen vóór deploy**,
**één publicatiemechanisme**, **geen dubbel werk op dezelfde push**.

**Workflow-keuze (praktisch):** [.github/workflows/README.md](../../.github/workflows/README.md).

## 1. Scheiding build vs. publicatie

| Laag                | Workflows                              | Doel                                                                      |
| ------------------- | -------------------------------------- | ------------------------------------------------------------------------- |
| Tests / validatie   | `vsa-ci.yml`, `site-build.yml`         | Regressie, bron-sync, validate, Hugo-build zonder deploy                  |
| Preview deploy      | `pages-preview.yml`                    | Sync → validate → build → peaceiris push naar `gh-pages:/preview/`        |
| Productie deploy    | `pages-demo.yml` (handmatig)           | Zelfde pipeline, push naar `gh-pages:/`                                   |
| Release (handmatig) | `release-artifacts.yml`                | Python-package + demo-artifact bij release                                |

Preview-deploy draait op **elke push** (alle branches): de gedeelde URL
`gh-pages:/preview/` toont steeds de laatst gepushte commit, zodat je per branch
kunt controleren of die deployable is. Parallelle validatie zonder deploy loopt via
`site-build.yml` (Linux) en `vsa-ci.yml` (Windows).

Verwijderde dubbele workflows (2026-07): `python-tests.yml`, `hugo-demo.yml`,
`build-artifacts.yml`, `build-target.yml`, `hugo.yml`.

## 2. Eén GitHub Pages-mechanisme

**Canonieke instelling** (repo Settings → Pages):

```text
Source: Deploy from a branch
Branch: gh-pages
Folder: /
```

**Niet gebruiken:** “GitHub Actions” + `actions/deploy-pages` naast peaceiris. Dat gaf:

- dubbele `pages build and deployment`-runs;
- intermittente `Deployment failed, try again later`.

Publicatie = `peaceiris/actions-gh-pages@v3` met `keep_files: true` en
`destination_dir: preview` voor preview.

## 3. Concurrency op Pages

```yaml
concurrency:
  group: pages-gh-pages
  cancel-in-progress: false
```

Voorkomt dat een nieuwe push een lopende git-push naar `gh-pages` afbreekt.

## 4. Fail-fast vóór deploy

Elke Pages-workflow roept `scripts/check-publication-output.py` aan (o.a. `index.html`,
gebroken links). Deploy gebeurt pas na groene build + check.

## 5. Bron-sync en validate

Alle Hugo-build-workflows syncen eerst `vendor/bron` (`sync_bron_zondagen.py`) en
valideren `examples/hugo-demo/content-source`. Content-fouten (bijv. `.md`-extensie
vergeten, VSA-semantiek) worden zo opgevangen vóór Pages.

## 6. Lokaal hetzelfde pad als CI

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
scripts\ci.cmd
scripts\build-preview.cmd
```

## 7. Als preview-deploy toch faalt

1. Controleer Pages-instelling (branch `gh-pages`, niet GitHub Actions).
2. Her-run de mislukte workflow (peaceiris is meestal stabieler dan deploy-pages).
3. Kijk of `site-build` / `vsa-ci` op dezelfde commit al groen waren — zo niet, eerst
   die fout oplossen.

## 8. Herbruikbare Pages-deploy (org-breed)

Gedeelde workflow: `.github/workflows/pages-deploy-reusable.yml`

Caller-repo's (VSA-tooling, `koor`, later `parochie-*`) bouwen lokaal, uploaden een
artifact, en roepen daarna de reusable aan voor publicatiecheck + peaceiris-push.

Voorbeeld en parameters: [VSA-tooling hergebruiken](../reuse-vsa-tooling.md#github-pages-deploy).

`bron` (MkDocs) gebruikt dezelfde reusable via `docs-pages.yml` (build + deploy).

## 9. Verdere verbeteringen (optioneel)

- `workflow_run`: preview pas deployen als `site-build` groen is (minder dubbele builds,
  iets langere feedback).
- Dependabot voor GitHub Actions-versies.
- Notificatie alleen op workflow `pages-preview.yml`, niet op elke parallelle job.
