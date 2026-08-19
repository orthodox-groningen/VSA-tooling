# Stap 137 - publicatiechecks en herbruikbare VSA-tool

## Doel

Twee zaken worden vastgelegd:

1. preview/productie-output wordt vóór deployment gecontroleerd;
2. andere repositories kunnen de VSA-rendering makkelijk gebruiken.

## Publicatiecontrole

Nieuw script:

```text
scripts/check-publication-output.py
```

Controleert:

- `index.html` bestaat;
- interne `href`/`src` verwijzingen bestaan;
- absolute paden gebruiken het juiste GitHub Pages projectpad;
- oude SVG `plain-text` metadata-comments komen niet terug;
- browser/XML-foutteksten worden niet gepubliceerd.

Preview gebruikt:

```text
/VSA-tooling/preview/
```

Productie gebruikt:

```text
/VSA-tooling/
```

## Hergebruik door andere repos

Nieuwe herbruikbare workflow:

```text
.github/workflows/vsa-render-reusable.yml
```

Andere repositories kunnen deze via `workflow_call` gebruiken.

Daarnaast blijft direct gebruik via `pip install` mogelijk:

```text
vsa-tool[rendering] @ git+https://github.com/orthodox-ronl/VSA-tooling.git@main
```
