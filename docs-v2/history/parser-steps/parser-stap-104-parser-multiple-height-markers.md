# Stap 104 - parseracceptatie voor meerdere hoogte-markeringen

## Doel

De parser accepteert meerdere hoogte-markeringen binnen één VSA-bron.

Voorbeeld:

```text
[:] begin [/:] midden [//:] einde
```

## Besluit

De bestaande `PitchMarkerNode` blijft behouden om renderer, validator en bestaande tests compatibel te houden.

Daarnaast is een alias toegevoegd:

```python
HeightMarkerNode = PitchMarkerNode
```

Zo kan documentatie en toekomstige code over hoogte-markeringen spreken zonder bestaande AST-consumenten te breken.

## Syntax

Een hoogte-markering gebruikt het bracket-directive eindtoken:

```text
:]
```

De parser zoekt dus niet meer naar een losse `]`, maar naar het samengestelde eindtoken `:]`.

De inhoud van een hoogte-markering moet één geldige EHM zijn.

Daarom is dit ongeldig:

```text
[/&\:]
```

Ook al zijn `/` en `\` afzonderlijk geldige EHM's.

## Nog niet gedaan

Nog niet aangepast:

- semantic validator;
- SVG-renderer;
- MusicXML;
- volledige parser-integratie met `bracket_token_stream`.
