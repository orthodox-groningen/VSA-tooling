# SVG stap 7 fix

De eerste SVG-renderer gebruikte alleen `MusicalPosition[]`.

Daardoor verdwenen gewone tekstnodes buiten scopes, bijvoorbeeld:

```text
is de Heer.
```

De renderer gebruikt nu de volledige AST:

```text
Document
  ├── PitchMarkerNode
  ├── TextNode
  ├── ScopeNode
  ├── TextNode
  └── PitchMarkerNode
```

Dit sluit beter aan bij het VSA-overlaymodel:

```text
bovenlaag
tekstlaag
onderlaag
```

De grafische glyphs zijn nog tijdelijk tekstueel weergegeven. Later worden dit echte SVG-lijnen en -punten.
