# Stap 34 - GitHub Pages SVG URL fix

Op GitHub Pages stond de site onder:

```text
/VSA-tooling/
```

maar SVG's werden geladen vanaf:

```text
/vsa/...
```

Dat gaf 404.

De shortcode normaliseert nu:

```go-html-template
{{ $src = replaceRE "^/" "" $src }}
```

en gebruikt daarna:

```go-html-template
{{ $src | relURL }}
```

Daarmee wordt:

```text
/vsa/voorbeeld.svg
```

correct:

```text
/VSA-tooling/vsa/voorbeeld.svg
```

bij publicatie onder GitHub Pages.
