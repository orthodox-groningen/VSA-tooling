# Stap 131 - GitHub Pages project-site baseURL

## Probleem

De repository is een GitHub Pages project-site.

Daardoor staat de site niet op:

```text
https://orthodox-ronl.github.io/
```

maar op:

```text
https://orthodox-ronl.github.io/VSA-tooling/
```

De preview staat daarom op:

```text
https://orthodox-ronl.github.io/VSA-tooling/preview/
```

## Wijziging

De workflows gebruiken nu project-site baseURL's:

```text
Productie: https://orthodox-ronl.github.io/VSA-tooling/
Preview:   https://orthodox-ronl.github.io/VSA-tooling/preview/
```

## Gevolg

Hugo genereert navigatie, CSS-links en andere absolute URL's met `/VSA-tooling/` ertussen.

Hiermee verdwijnen links van de foutieve vorm:

```text
/preview/...
```

Die worden:

```text
/VSA-tooling/preview/...
```
