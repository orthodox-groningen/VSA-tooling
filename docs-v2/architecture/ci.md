# CI-architectuur

De CI-architectuur is gericht op vroeg falen, herhaalbaarheid en één duidelijk publicatiemechanisme.

## Lagen

| Laag                | Workflows                                              | Doel                                                         |
| ------------------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| Tests / validatie   | `vsa-ci.yml`, `site-build.yml`                         | Regressie, bron-sync, validate en Hugo-build zonder deploy   |
| Preview deploy      | `pages-preview.yml`                                    | Preview naar `gh-pages:/preview/` (elke push, alle branches) |
| Productie deploy    | `pages-demo.yml`                                       | Gecontroleerde productie naar `gh-pages:/`                   |
| Release (handmatig) | `release-artifacts.yml`                                | Package- en demo-artifacts bij release                       |
| Org-herbruikbaar    | `pages-deploy-reusable.yml`, `vsa-render-reusable.yml` | Deploy/render voor andere repo's                             |

## Pages-beleid

Canonieke GitHub Pages-instelling:

```text
Source: Deploy from a branch
Branch: gh-pages
Folder: /
```

Niet combineren met een tweede Pages-mechanisme via `actions/deploy-pages`, omdat dat dubbele deployments en instabiliteit kan veroorzaken.

## Betrouwbaarheidsregels

| Regel                         | Effect                                         |
| ----------------------------- | ---------------------------------------------- |
| Fail-fast vóór deploy         | Fouten worden gevonden voordat Pages wijzigt.  |
| Eén publicatiemechanisme      | Minder race conditions en minder dubbele runs. |
| Concurrency op Pages          | Deploys breken elkaar niet af.                 |
| Lokaal pad gelijk aan CI      | Lokale diagnose sluit aan op GitHub Actions.   |
| Reusable workflows            | Andere repos kunnen hetzelfde pad volgen.      |

Zie ook [CI-betrouwbaarheid](../../docs/architecture/ci-reliability.md) voor Pages-troubleshooting en verwijderde dubbele workflows.
