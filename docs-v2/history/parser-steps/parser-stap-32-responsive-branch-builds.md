# Stap 32 - responsive demo en branch-aware builds

Deze stap voegt toe:

```text
examples/hugo-demo/static/css/site.css
.github/workflows/site-build.yml
```

## Responsive demo

De demo-site bevat nu CSS voor:

- telefoon;
- tablet;
- laptop;
- groot scherm.

Belangrijkste regels:

```css
max-width: 100%;
overflow-x: auto;
@media (max-width: 600px)
```

## Branch-aware build

Nieuwe workflow:

```text
Site build
```

Gedrag:

| Event | Branch | Target |
|-------|--------|--------|
| push | main | production |
| push | andere branch | preview |
| pull_request | elke branch | preview |

De workflow bouwt artifacts, maar publiceert niet automatisch naar GitHub Pages.

Dat blijft bewust apart.
