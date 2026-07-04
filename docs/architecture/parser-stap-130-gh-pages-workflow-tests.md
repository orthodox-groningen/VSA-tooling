# Stap 130 - workflowtests voor gh-pages preview/productie

## Doel

De workflowtests sluiten aan op het gekozen publicatiemodel:

```text
gh-pages:/
  productie-site

gh-pages:/preview/
  automatische preview-site
```

De workflowtests controleren `actions/upload-pages-artifact` en
`actions/deploy-pages` plus gedeelde site-cache tussen preview en productie.
