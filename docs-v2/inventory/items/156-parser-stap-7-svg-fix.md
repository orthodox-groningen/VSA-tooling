# 156 — SVG stap 7 fix

## Huidige locatie

```text
docs/architecture/parser-stap-7-svg-fix.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

De eerste SVG-renderer gebruikte alleen `MusicalPosition[]`. Daardoor verdwenen gewone tekstnodes buiten scopes, bijvoorbeeld: is de Heer. De renderer gebruikt nu de volledige AST: Document ├── PitchMarkerNode ├── TextNode ├── ScopeNode ├── TextNode └── PitchMarkerNode Dit sluit beter aan bij het VSA-overlaymodel:

## Relaties met andere documenten

Nog te detailleren tijdens inhoudelijke consolidatie.

## Overlap met andere documenten

Nog te detailleren tijdens inhoudelijke consolidatie.

## Voorgestelde bestemming

```text
docs-v2/history/parser/
```

## Inventarisatiestatus

Eerste classificatie op basis van bestandsnaam, locatie en documentkop.

## Opmerkingen

Geen inhoud migreren in fase 1; alleen classificeren en later controleren.
