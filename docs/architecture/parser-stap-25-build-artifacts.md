# Stap 25 - build artifacts

Deze stap introduceert:

```text
.github/workflows/build-artifacts.yml
```

De workflow bouwt:

```text
generated Markdown
generated SVG
generated Hugo site
```

en uploadt die als GitHub Actions artifacts.

## Waarom

Dit is nuttig om:

- buildresultaten te inspecteren;
- preview-output te downloaden;
- later productie-deploy voor te bereiden.

## Lokaal

```cmd
scripts\build-artifacts.cmd
```

## GitHub

```text
Actions → Build artifacts → Artifacts
```
