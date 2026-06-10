# VSA stap 12 - CI/build-script

Deze stap voegt een eerste echte CI-flow toe.

Doel:

```text
tests
  ↓
validate
  ↓
build-markdown
```

Dit werkt lokaal via CMD en in GitHub Actions.

## Lokaal

```cmd
scripts\ci.cmd
```

## GitHub Actions

Bij `push` en `pull_request` draait dezelfde controle automatisch.
