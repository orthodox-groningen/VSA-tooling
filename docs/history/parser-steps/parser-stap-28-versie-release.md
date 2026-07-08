# Stap 28 - versie en releasevoorbereiding

Deze stap introduceert basaal versiebeheer.

## CLI

```cmd
vsa --version
```

## Changelog

```text
CHANGELOG.md
```

## Release artifacts

Handmatige workflow:

```text
Actions → Release artifacts → Run workflow
```

Deze bouwt:

```text
dist/*
generated/release/*
```

## Let op

Dit publiceert nog niets naar PyPI of productie.

Het maakt alleen downloadbare artifacts voor controle.
