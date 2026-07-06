# Stap 67 - spacing policy + metrics diagnostics

Echte font metrics vervangen spacingregels niet.

Deze stap introduceert daarom:

- minimale visuele breedte voor bronspaties;
- extra scope safety margin;
- subtielere en kortere filler-lines;
- metricsinformatie op de spacing-diagnostiekpagina.

## Metrics blok

```cmd
python scripts\update-spacing-diagnostics-metadata.py
```

Hiermee wordt de diagnostiekpagina voorzien van:

- font;
- backend;
- real metrics status;
- fontpad;
- voorbeeldbreedtes.
