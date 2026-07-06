# Stap 96 - bracket token stream

## Doel

De bracket-directive scanner uit stap 95 wordt uitgebreid met een tokenstroom-bouwsteen.

Bestand:

```text
src/vsa/bracket_token_stream.py
```

## Tokenvormen

De tokenstroom kent voorlopig drie soorten tokens:

```text
text
directive
pitch_marker
```

## Betekenis

`text` is gewone tekst buiten bracket-directives.

`directive` is een geldige bracket-directive waarvan de inhoud geen EHM is.

`pitch_marker` is een bracket-directive waarvan de inhoud een geldige EHM is.

## Waarom apart?

Deze bouwsteen maakt het mogelijk om later de bestaande parser gecontroleerd aan te passen.

Daarmee vermijden we dat bracket-token dispatch en bestaande scope parsing tegelijk worden gewijzigd.

## Nog niet gedaan

Nog niet geïntegreerd in:

- bestaande parser;
- AST;
- validator;
- SVG-renderer.
