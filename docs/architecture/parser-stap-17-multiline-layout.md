# Stap 17 - multiline SVG-layout

Deze stap introduceert automatische regelafbreking.

Voorheen:

```text
één lange horizontale SVG
```

Nu:

```text
nodes verdelen over meerdere regels
```

De layout gebeurt voorlopig op node-niveau:

```text
TextNode
ScopeNode
PitchMarkerNode
```

Later mogelijk:

- slimme wrapping;
- syllabeverdeling;
- alignment per muzikale frase;
- staff/group layout.
