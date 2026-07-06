# Stap 23 - Hugo workflow

Deze stap voegt een volledige workflow toe.

## Lokaal

```cmd
scripts\serve-hugo.cmd
```

## Build

```cmd
scripts\build-hugo.cmd
```

## GitHub Actions

Workflow:

```text
.github/workflows/hugo.yml
```

Pipeline:

```text
validate
  ↓
pytest
  ↓
vsa build-markdown
  ↓
hugo
  ↓
artifact/site
```

## Structuur

```text
content-source/
    ↓
generated/hugo/content/

generated/hugo/static/vsa/
    ↓
Hugo site
```
