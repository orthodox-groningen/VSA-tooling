# Stap 34 - links en responsive layout fix

## Gebroken links

De demo gebruikte absolute links zoals:

```text
/voorbeelden/
```

Dat werkt lokaal op root, maar niet op GitHub Pages onder:

```text
/VSA-tooling/
```

Daarom gebruikt de template nu:

```go-html-template
{{ "voorbeelden/" | relURL }}
```

Markdownpagina's gebruiken relatieve links.

## Afbeeldingen

Voor VSA-afbeeldingen gebruikt de demo nu shortcode-output.

De shortcode past `relURL` toe:

```go-html-template
src="{{ $src | relURL }}"
```

## Responsive layout

De CSS gebruikt nu:

```css
width: 100%;
max-width: none;
env(safe-area-inset-left)
```

op kleine schermen, zodat de homepage niet halfbreed wordt op foldables of smalle telefoons.
