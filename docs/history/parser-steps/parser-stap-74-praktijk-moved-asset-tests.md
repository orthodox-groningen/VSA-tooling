# Stap 74 - praktijk verplaatst: asset testverwachtingen

De praktijkvoorbeelden zijn verplaatst van:

```text
examples\hugo-demo\content-source\voorbeelden\praktijk
```

naar:

```text
examples\hugo-demo\content-source\praktijk
```

Daarmee verandert ook de correcte SVG asset-stem.

Voorbeeld:

```text
content-source\praktijk\weekdagen\woensdag.md
```

wordt:

```text
/vsa/praktijk-weekdagen-woensdag-block-1.svg
```

Niet:

```text
/vsa/voorbeelden-praktijk-weekdagen-woensdag-block-1.svg
```

De tests controleren nu beide gevallen:

- oude padstructuur;
- nieuwe padstructuur.

De assetnaam moet altijd uit het actuele relatieve pad worden afgeleid.
