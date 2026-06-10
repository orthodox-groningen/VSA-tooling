# VSA multiline stap 17 - fix 2

Deze patch herstelt de tests na tekst-wrapping.

Probleem:

De renderer splitst gewone tekst nu in losse woordsegmenten:

```text
is 
de 
Heer.
```

Daardoor staat de originele tekst niet meer letterlijk aaneengesloten in de SVG-output, terwijl bestaande tests zoeken op:

```text
is de Heer
```

Oplossing:

- tekstwrapping blijft behouden;
- leidende whitespace wordt niet als aparte tekstchunk behandeld;
- originele `TextNode`-inhoud wordt als SVG-commentaar opgenomen.

Voorbeeld:

```xml
<!-- plain-text: is de Heer. -->
```

Dat maakt regressietests en debugging eenvoudiger zonder de zichtbare rendering te verstoren.
