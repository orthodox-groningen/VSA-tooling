# CI-architectuur

De CI-architectuur is gericht op vroeg falen, herhaalbaarheid en één duidelijk publicatiemechanisme.

## Lagen

| Laag                | Workflows                                              | Doel                                                       |
| ------------------- | ------------------------------------------------------ | ---------------------------------------------------------- |
| Tests / validatie   | `vsa-ci.yml`, `docs-build.yml`                         | Pytest, consumer-minimal, MkDocs `--strict` zonder deploy  |
| Docs deploy         | `docs-pages.yml`                                       | MkDocs → `gh-pages:/` (`main`) of `/preview/`              |
| Release (handmatig) | `release-artifacts.yml`                                | Package- en smoke-artifacts bij release                    |
| Org-herbruikbaar    | `pages-deploy-reusable.yml`, `vsa-render-reusable.yml` | Deploy/render voor andere repo's                           |

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
| Fail-fast in CI               | Geen deploy bij rode tests of validate         |
| Herbruikbare deploy-workflow  | Één publicatiepad voor org-repo's              |
| Publication check             | Dode links/assets vóór push naar `gh-pages`    |
