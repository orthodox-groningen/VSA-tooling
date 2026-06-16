# Stap 72 - fix nested VSA image refs

## Probleem

Bij pagina's in subdirectories werd soms naar een verkeerde SVG verwezen.

Voorbeeld:

```text
content-source\voorbeelden\praktijk\weekdagen\woensdag.md
```

moet verwijzen naar:

```text
/vsa/voorbeelden-praktijk-weekdagen-woensdag-block-1.svg
```

## Fix

Toegevoegd:

```cmd
python scripts\repair-vsa-image-refs.py
```

Dit script herleidt de SVG naam uit het volledige relatieve pagina-pad.
