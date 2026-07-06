# Stap 121 - Height Marker Validator Contract

## Doel

Vastleggen hoe de validator hoogte-markeringen interpreteert.

## Contract

De validator gebruikt uitsluitend:

```python
height_markers(document)
```

en inspecteert niet rechtstreeks de AST-implementatie.

## Semantiek

- eerste marker: `start_height`
- latere markers: `local_height`

## Volgende stap

Stap 122 koppelt de bestaande validator aan de helperlaag.
