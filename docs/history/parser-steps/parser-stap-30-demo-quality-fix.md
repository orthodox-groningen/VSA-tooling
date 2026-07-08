# Stap 30 - demo quality fix

Deze patch herstelt twee problemen in de demo-site.

## Dubbele titels

Hugo-template `single.html` voegde een titel toe:

```html
<h1>{{ .Title }}</h1>
```

maar de Markdownpagina's bevatten zelf ook:

```markdown
# Titel
```

Daarom ontstonden dubbele titels.

De template laat nu alleen de inhoud zien.

## Ongeldig multiline voorbeeld

De demo gebruikte:

```text
[:] ... [:]
```

Dat is voor dit voorbeeld semantisch niet gewenst.

De afsluiting is gecorrigeerd naar:

```text
[\\:]
```

Daarnaast is een test toegevoegd die de demo-content valideert.
