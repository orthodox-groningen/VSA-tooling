# README addendum - rendering font

De SVG-renderer gebruikt standaard **DejaVu Sans** als renderfont.

Reden:

- goed leesbaar sans-font;
- geschikt voor koorbladen op afstand;
- beschikbaar op Linux/GitHub Actions via `fonts-dejavu-core`;
- bruikbaar op Windows via een expliciet fontbestand;
- stabieler en reproduceerbaarder dan Windows-specifieke fonts zoals Segoe UI.

Standaard fontpad:

```text
assets/fonts/DejaVuSans.ttf
```

Als dat bestand ontbreekt, zoekt VSA naar systeemfonts en valt daarna terug op de interne estimator.
