# Publicatiearchitectuur

## Doel

Publicatie maakt onderscheid tussen preview, productie en herbruikbaar gebruik vanuit andere repositories.

## Publicatiecontrole

Voor deployment wordt gecontroleerd dat gegenereerde output bruikbaar is. Controlepunten zijn onder andere:

- `index.html` bestaat;
- interne `href`- en `src`-verwijzingen bestaan;
- projectpaden kloppen voor GitHub Pages;
- oude SVG-metadata-comments komen niet terug;
- browser- of XML-foutteksten worden niet gepubliceerd.

## Preview en productie

```text
Preview:   /VSA-tooling/preview/
Productie: /VSA-tooling/
```

## Hergebruik

Andere repositories kunnen de VSA-rendering gebruiken via een herbruikbare GitHub Actions-workflow of via installatie van de tool.

## Traceerbaarheid

Gebaseerd op onder meer:

- `docs/architecture/parser-stap-24-github-actions.md`
- `docs/architecture/parser-stap-26-github-pages.md`
- `docs/architecture/parser-stap-128-github-pages-preview.md`
- `docs/architecture/parser-stap-129-gh-pages-preview-production.md`
- `docs/architecture/parser-stap-137-publication-checks-and-reusable-tool.md`
