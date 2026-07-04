# Stap 129 - GitHub Pages preview en productie via gh-pages

## Doel

Preview automatisch publiceren bij iedere commit:

```text
https://orthodox-groningen.github.io/preview/
```

Productie blijft handmatig via workflow dispatch:

```text
https://orthodox-groningen.github.io/
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

## GitHub Pages instelling

Zet in GitHub handmatig:

```text
Settings → Pages → Build and deployment
Source: GitHub Actions
```

Preview en productie publiceren via `actions/deploy-pages` met gedeelde site-state
(`actions/cache` + eenmalige bootstrap vanuit `gh-pages`).

## Waarom deploy-pages met cache?

`actions/deploy-pages` publiceert steeds één volledig Pages-artifact. Preview en
productie delen daarom één samengestelde site-root (`pages-site/`): preview onder
`/preview/`, productie onder `/`. De cache bewaart die samengestelde staat tussen
runs; alleen preview-updates overschrijven `pages-site/preview/`, productie-updates
alleen de root (de map `preview/` blijft staan).

De oude `peaceiris`-push naar `gh-pages` veroorzaakte een tweede, conflicterende
`pages build and deployment`-run van GitHub zelf.

## Workflows

- `.github/workflows/pages-preview.yml`
  - draait automatisch op `push`
  - publiceert naar `/preview/`

- `.github/workflows/pages-demo.yml`
  - draait handmatig
  - publiceert productie-root
  - behoudt preview via gedeelde site-cache
