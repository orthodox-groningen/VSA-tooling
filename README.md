# VSA Pages enable fix

Deze patch zet in de Pages workflow:

```yaml
enablement: true
```

bij:

```yaml
actions/configure-pages@v5
```

Dit helpt wanneer GitHub Pages nog niet eerder voor de repo is geactiveerd.

Als dit alsnog faalt, moet je handmatig instellen:

```text
Settings → Pages → Build and deployment → Source → GitHub Actions
```
