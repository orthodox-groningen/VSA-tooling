# Pages enable fix

De Pages workflow faalde bij:

```text
Setup Pages
```

met:

```text
Get Pages site failed
```

De workflow zet nu:

```yaml
with:
  enablement: true
```

bij:

```yaml
actions/configure-pages@v5
```

Als GitHub dit niet toestaat, moet Pages handmatig worden ingesteld:

```text
Settings → Pages → Build and deployment → Source → GitHub Actions
```
