# Stap 26 - GitHub Pages publicatie

Deze stap voegt toe:

```text
.github/workflows/pages-demo.yml
```

De workflow doet:

```text
pytest
  ↓
vsa validate
  ↓
vsa build-markdown
  ↓
hugo build
  ↓
deploy-pages
```

## Handmatig starten

In GitHub:

```text
Actions → Deploy Hugo demo to GitHub Pages → Run workflow
```

## Vereiste instelling

In de repo:

```text
Settings → Pages → Build and deployment → Source → GitHub Actions
```

## Waarom handmatig?

Zolang de demo nog experimenteel is, is handmatig deployen veiliger dan automatisch publiceren bij elke push.
