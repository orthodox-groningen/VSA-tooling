# Stap 12 - CI/build-script

Deze stap maakt één lokaal CI-commando:

```cmd
scripts\ci.cmd
```

Het commando doet:

```text
1. tijdelijke CI-output verwijderen
2. pytest draaien
3. demo-content valideren
4. demo-content naar Markdown + SVG bouwen
```

## Waarom

Hiermee test je niet alleen losse functies, maar ook de eerste complete keten:

```text
Markdown met VSA
  ↓
validate
  ↓
build-markdown
  ↓
gegenereerde Markdown + SVG
```

## GitHub Actions

De workflow `.github/workflows/vsa-ci.yml` gebruikt hetzelfde script.

Daardoor blijven lokaal testen en GitHub Actions zoveel mogelijk gelijk.
