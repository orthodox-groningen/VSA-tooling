# Stap 128 - automatische GitHub Pages preview

## Doel

Bij elke commit wordt automatisch een preview-site gebouwd en gepubliceerd onder:

```text
https://orthodox-groningen.github.io/preview/
```

Productie blijft handmatig.

## Aanpak

De workflow `.github/workflows/pages-preview.yml`:

1. draait tests;
2. valideert VSA-content;
3. genereert Hugo-content en SVG;
4. bouwt Hugo met `baseURL` op `/preview/`;
5. publiceert alleen de map `preview/` naar de `gh-pages` branch.

## Belangrijk

De preview-workflow wijzigt alleen:

```text
pages-site/preview/
```

De rest van de gepubliceerde site (productie-root) blijft in de gedeelde cache staan.

## GitHub Pages instelling

Deze aanpak verwacht:

```text
Settings → Pages → Build and deployment
Source: GitHub Actions
```

Publicatie verloopt via `actions/deploy-pages` (niet meer via directe commits op
`gh-pages`).

## Productie

Productie blijft handmatig.

Als productie later ook via dezelfde `gh-pages` branch moet blijven bestaan, moet de productie-workflow de root van `gh-pages` bijwerken en de map `preview/` bewaren.
