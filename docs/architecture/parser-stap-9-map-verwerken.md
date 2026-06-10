# Stap 9 - map verwerken

Deze stap breidt `vsa process` uit zodat het ook een map accepteert.

Voorbeeld:

```cmd
vsa process examples\site-demo generated\vsa
```

Het commando zoekt recursief naar:

```text
*.md
*.markdown
```

en genereert per VSA-blok een SVG-bestand.

## Naamgeving

Bij een bestand:

```text
examples/site-demo/zondag/toon-1.md
```

wordt de uitvoer:

```text
zondag-toon-1-block-1.svg
```

Dit voorkomt naamconflicten bij grotere sites.
