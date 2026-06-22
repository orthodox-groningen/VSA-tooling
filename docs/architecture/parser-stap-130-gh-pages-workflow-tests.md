# Stap 130 - workflowtests voor gh-pages preview/productie

## Doel

De workflowtests sluiten aan op het gekozen publicatiemodel:

```text
gh-pages:/
  productie-site

gh-pages:/preview/
  automatische preview-site
```

De oude testverwachtingen voor `actions/configure-pages` en `actions/deploy-pages` zijn vervangen door `peaceiris/actions-gh-pages@v3`.
