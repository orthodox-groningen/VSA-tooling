# Stap 19 - validate op mappen

Deze stap breidt `vsa validate` uit.

## Bestand

```cmd
vsa validate examples\minimal\040_valid_markdown_validate.md
```

## Map

```cmd
vsa validate examples\hugo-demo\content-source
```

De tool zoekt recursief naar:

```text
*.md
*.markdown
*.vsa
```

en rapporteert alle fouten in één run.

Dit is de basis voor:

- lokale pre-build controle;
- Hugo preprocessing;
- GitHub Actions.
