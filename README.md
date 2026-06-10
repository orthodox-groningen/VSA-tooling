# VSA stap 26 - GitHub Pages publicatie

Deze stap voegt een GitHub Pages workflow toe.

Doel:

```text
VSA validate
  ↓
VSA build-markdown
  ↓
Hugo build
  ↓
GitHub Pages deploy
```

Belangrijk:

- deze workflow draait alleen handmatig via `workflow_dispatch`;
- dus hij publiceert niet automatisch bij elke push;
- dat is veiliger zolang de demo/workflow nog in ontwikkeling is.

## GitHub instelling

Zet in GitHub:

```text
Settings → Pages → Build and deployment → Source → GitHub Actions
```
