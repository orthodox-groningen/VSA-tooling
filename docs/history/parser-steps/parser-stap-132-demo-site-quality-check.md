# Stap 132 - demo-site kwaliteitscontrole

## Doel

De demo-site krijgt een herhaalbare kwaliteitscontrole voor de gegenereerde Hugo-output.

## Script

```text
scripts/check-demo-site-quality.py
```

Controleert:

- ontbrekende `index.html`;
- kapotte interne links;
- SVG/image verwijzingen naar ontbrekende bestanden;
- foutieve project-site links zoals `/preview/` in plaats van `/VSA-tooling/preview/`.

## Gebruik

```cmd
python scripts\check-demo-site-quality.py --site-dir examples\hugo-demo\public --mode preview
```

Voor CI kan deze check later na de Hugo-build worden toegevoegd.
