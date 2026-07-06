# Stap 119 - Height Marker Parser Contract

## Doel

Definitief vastleggen wat de parser moet opleveren zodra
hoogte-markeringen volledig geactiveerd worden.

## Contract

Parser-uitvoer blijft documentvolgorde behouden.

Voorbeeld:

```text
[:] tekst {/abc_} [/:]
```

wordt conceptueel:

```text
HeightMarkerNode
TextNode
ScopeNode
HeightMarkerNode
```

## Compatibiliteit

Bestaande PitchMarkerNode-contracten mogen niet breken.

HeightMarkerNode mag voorlopig een compatibiliteitslaag blijven.
