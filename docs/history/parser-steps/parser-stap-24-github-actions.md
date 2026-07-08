# Stap 24 - GitHub Actions opschonen

Deze stap splitst workflows.

## 1. VSA CI

```text
.github/workflows/vsa-ci.yml
```

Draait op Windows:

```text
scripts\ci.cmd
```

Doel:

- Python package installeren;
- tests draaien;
- demo-content valideren;
- demo Markdown/SVG genereren.

## 2. Hugo demo build

```text
.github/workflows/hugo-demo.yml
```

Draait op Ubuntu:

```text
pytest
vsa validate
vsa build-markdown
hugo build
```

Doel:

- controleren dat de gegenereerde Hugo-demo echt bouwt;
- artifact uploaden.

## Legacy workflow

```text
.github/workflows/hugo.yml
```

staat alleen nog op manual dispatch, zodat er geen dubbele of verwarrende automatische builds draaien.
