# Tokenreferentie

## Hoogte-markeringen

Een hoogte-markering heeft de vorm:

```text
[<EHM>:]
```

| Token   | Soort             | Opmerking                         |
| ------- | ----------------- | --------------------------------- |
| `[:]`   | Hoogte-markering  | Neutraal                          |
| `[/:]`  | Hoogte-markering  | Enkelvoudige hoogtebeweging       |
| `[//:]` | Hoogte-markering  | Samengestelde hoogtebeweging      |
| `[\:]`  | Hoogte-markering  | Dalende hoogtebeweging            |

## Control tokens

Control tokens zijn geen hoogte-markeringen.

| Token  | Abstracte betekenis          |
| ------ | ---------------------------- |
| `[*]`  | `phrase_rest`                |
| `[/]`  | `phrase_boundary`            |
| `[*?]` | `optional_phrase_rest`       |
| `[/?]` | `optional_phrase_boundary`   |

## Renderer-afhankelijk gedrag

| Renderer  | Mogelijke interpretatie                                  |
| --------- | -------------------------------------------------------- |
| SVG       | Zichtbaar teken, regelafbreking, zachte breuk of negeren |
| MusicXML  | Breath mark, barline, system break of negeren            |

## Ontwerpregel

Control tokens hebben geen universele visuele betekenis.

De parser legt de abstracte intentie vast; renderers bepalen de concrete uitvoer.
