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
Source: Deploy from a branch
Branch: gh-pages
Folder: /
```

## Waarom niet actions/deploy-pages?

De bestaande `actions/deploy-pages` publiceert steeds één volledig Pages artifact.

Dat maakt het lastig om automatisch `/preview/` te verversen zonder de handmatige productie-root te overschrijven.

Met `gh-pages` + `destination_dir: preview` kan preview apart worden bijgewerkt.

## Workflows

- `.github/workflows/pages-preview.yml`
  - draait automatisch op `push`
  - publiceert naar `/preview/`

- `.github/workflows/pages-demo.yml`
  - draait handmatig
  - publiceert productie-root
  - behoudt bestaande bestanden met `keep_files: true`
