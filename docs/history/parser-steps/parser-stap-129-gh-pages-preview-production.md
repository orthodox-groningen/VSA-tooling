# Stap 129 - GitHub Pages preview en productie via gh-pages

## Doel

Preview automatisch publiceren bij iedere commit:

```text
https://orthodox-groningen.github.io/VSA-tooling/preview/
```

Productie blijft handmatig via workflow dispatch:

```text
https://orthodox-groningen.github.io/VSA-tooling/
```

## Belangrijk ontwerpbesluit

GitHub Pages heeft één publicatiebron.

Daarom publiceren preview en productie allebei naar dezelfde branch:

```text
gh-pages
```

Preview wordt gepubliceerd naar:

```text
gh-pages:/preview/
```

Productie wordt gepubliceerd naar:

```text
gh-pages:/
```

## GitHub Pages instelling (verplicht)

Zet in GitHub handmatig:

```text
Settings → Pages → Build and deployment
Source: Deploy from a branch
Branch: gh-pages
Folder: /
```

Gebruik **niet** “GitHub Actions” als Pages-bron. Met `peaceiris/actions-gh-pages` pushen
de workflows direct naar `gh-pages`; een tweede `pages build and deployment`-run of
`actions/deploy-pages` leidt tot conflicten en intermittente deploy-fouten.

## Waarom niet actions/deploy-pages?

De officiële `actions/deploy-pages` publiceert steeds één volledig artifact en deelt geen
betrouwbare partiële updates tussen `/preview/` en `/`. Bovendien faalt de deploy-stap
regelmatig met generieke API-fouten (“Deployment failed, try again later”).

Met `gh-pages` + `destination_dir: preview` kan preview apart worden bijgewerkt terwijl
productie-root behouden blijft (`keep_files: true`).

## Workflows

- `.github/workflows/pages-preview.yml`
  - draait automatisch op `push`
  - publiceert naar `/preview/`
  - geen pytest (al gedekt door `python-tests.yml` / `hugo-demo.yml`)

- `.github/workflows/pages-demo.yml`
  - draait handmatig
  - publiceert productie-root
  - behoudt bestaande bestanden met `keep_files: true`

Beide workflows delen `concurrency.group: pages-gh-pages` met
`cancel-in-progress: false` om halve git-pushes naar `gh-pages` te vermijden.

Zie ook [ci-reliability.md](ci-reliability.md).
