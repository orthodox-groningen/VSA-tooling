# TODO addendum stap 91/92

Toevoegen aan `docs/todo.md` onder parser/rendering:

## Meerdere hoogte-markeringen

Status: `Gespecificeerd`

Vastgelegd:

- meerdere hoogte-markeringen per `vsa-notatie` blok zijn toegestaan;
- hoogte-markering heeft strikt vorm `[<EHM>:]`;
- `&` mag niet in een hoogte-markering voorkomen;
- eerste markering is beginhoogte;
- latere markeringen zijn doelhoogtes op die positie;
- tekst vóór de eerste markering is toegestaan;
- tekst na de laatste markering is toegestaan;
- tekst tussen markeringen is toegestaan;
- SVG behandelt alle hoogte-markeringen gelijk.

Nog implementeren:

- parseracceptatie;
- AST-representatie zonder maximaal één pitch marker;
- validatorregels;
- SVG-rendering;
- praktijkvoorbeelden;
- documentatie integreren in hoofd-specificatie.
