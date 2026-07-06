# Stap 136 - comment-only regels zonder extra whitespace

## Probleem

HTML-commentaar binnen `::: vsa-notatie` werd genegeerd, maar een commentaarregel kon nog als lege regel doorwerken in afgeleide artefacten.

Voorbeeld:

```text
<!-- Liturgikon, 270 -->
```

moet geen extra verticale ruimte in SVG veroorzaken.

## Regel

- Commentaar dat een hele regel inneemt verdwijnt inclusief de regelafbreking.
- Inline commentaar verdwijnt op die positie.
- De oorspronkelijke bron wordt niet aangepast.
- Commentaar mag geen tekst, whitespace, newline, spacing of layout opleveren.
