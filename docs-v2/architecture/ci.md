# CI-architectuur

De CI-architectuur is gericht op vroeg falen, herhaalbaarheid en één duidelijk publicatiemechanisme.

## Lagen

| Laag              | Workflows                                                           | Doel                                                       |
| ----------------- | ------------------------------------------------------------------- | ---------------------------------------------------------- |
| Tests / validatie | `python-tests.yml`, `vsa-ci.yml`, `hugo-demo.yml`, `site-build.yml` | Regressie, bron-sync, validate en Hugo-build zonder deploy |
| Preview deploy    | `pages-preview.yml`                                                 | Gecontroleerde preview naar `gh-pages:/preview/`           |
| Productie deploy  | `pages-demo.yml`                                                    | Gecontroleerde productie naar `gh-pages:/`                 |

## Pages-beleid

Canonieke GitHub Pages-instelling:

```text
Source: Deploy from a branch
Branch: gh-pages
Folder: /
```

Niet combineren met een tweede Pages-mechanisme via `actions/deploy-pages`, omdat dat dubbele deployments en instabiliteit kan veroorzaken.

## Betrouwbaarheidsregels

| Regel                         | Effect                                      |
| ----------------------------- | ------------------------------------------- |
| Fail-fast vóór deploy         | Fouten worden gevonden voordat Pages wijzigt. |
| Eén publicatiemechanisme      | Minder race conditions en minder dubbele runs. |
| Concurrency op Pages          | Deploys breken elkaar niet af.              |
| Lokaal pad gelijk aan CI      | Lokale diagnose sluit aan op GitHub Actions. |
| Reusable workflows            | Andere repos kunnen hetzelfde pad volgen.   |
