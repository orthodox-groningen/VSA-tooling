# Stap 59 - inspect Hugo SVG usage

Uit `findstr` bleek dat de SVG voor tropaar toon 8 al meerdere renderregels bevat.

Daarmee lijkt de renderer zelf bron-newlines te respecteren. Het resterende
probleem zit vermoedelijk in:

- welke SVG de HTML-pagina toont;
- browsercache;
- CSS-scaling;
- img/object/embed gebruik;
- oude assets die nog in `public` staan;
- verwarring tussen broncodeweergave en SVG-weergave.

## Script

```cmd
python scripts\inspect-hugo-svg-usage.py toon-8
```
