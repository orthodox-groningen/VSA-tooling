# Stap 128 - automatische GitHub Pages preview

## Doel

Bij elke commit wordt automatisch een preview-site gebouwd en gepubliceerd onder:

```text
https://orthodox-ronl.github.io/preview/
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
gh-pages:/preview/
```

De rest van de `gh-pages` branch blijft staan.

## GitHub Pages instelling

Deze aanpak verwacht dat GitHub Pages publiceert vanuit:

```text
Branch: gh-pages
Folder: /
Source: Deploy from a branch
```

Niet “GitHub Actions” — zie [ci-reliability.md](ci-reliability.md).

## Productie

Productie blijft handmatig.

Als productie later ook via dezelfde `gh-pages` branch moet blijven bestaan, moet de productie-workflow de root van `gh-pages` bijwerken en de map `preview/` bewaren.
