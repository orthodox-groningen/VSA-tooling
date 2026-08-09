# TODO addendum stap 104

Toevoegen aan `docs/todo.md` onder [parser](@):

## Parseracceptatie meerdere hoogte-markeringen

Status: `Geïmplementeerd`

De [parser](@) accepteert meerdere `[<EHM>:]` [hoogte-markeringen](@) in documentvolgorde.

Compatibiliteit:

- `PitchMarkerNode` blijft bestaan;
- `HeightMarkerNode` is alias voor `PitchMarkerNode`.

Nog doen:

- [parser](@) koppelen aan `bracket_token_stream`;
- [validator](@)regels voor meerdere [hoogte-markeringen](@);
- SVG-rendering controleren;
- documentatie integreren in hoofd-specificatie.
