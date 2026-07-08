# Stap 134 - plain-text comments verwijderen uit SVG

## Probleem

SVG-output bevatte metadata-comments van de vorm:

```xml
<!-- plain-text: ... -->
```

Dat is niet gewenst: commentaar uit of over de bron hoort niet als SVG-output te worden gegenereerd.

## Wijziging

De `plain-text` comment-output is volledig uit `SVGRenderer.render_document()` verwijderd.

De zichtbare `<text>` rendering blijft ongewijzigd.

Bestaande tests die afhankelijk waren van de metadata-comments zijn aangepast naar de nieuwe policy.
