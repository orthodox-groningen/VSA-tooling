# Stap 130 - workflowtests voor gh-pages preview/productie

## Doel

De workflowtests sluiten aan op het gekozen publicatiemodel:

```text
gh-pages:/
  productie-site

gh-pages:/preview/
  automatische preview-site
```

De workflowtests controleren `peaceiris/actions-gh-pages@v3`, geen
`actions/deploy-pages`, en gedeelde `pages-gh-pages`-concurrency zonder cancel.
