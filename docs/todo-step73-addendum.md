# TODO addendum stap 73

Toevoegen aan `docs/todo.md` onder parser/validator/rendering:

## Hoogte-markeringen als positionele nodes

Status: `Open`

Specificatiebesluit:

- meerdere hoogte-markeringen binnen één `vsa-notatie`blok zijn toegestaan;
- de eerste markering is de beginhoogte;
- latere markeringen zijn lokale hoogtecontrolepunten;
- tekst mag vóór, tussen en na hoogte-markeringen staan;
- SVG-rendering behandelt alle hoogte-markeringen gelijk.

Implementatie later controleren:

- parser modelleert hoogte-markeringen als nodes in documentstroom;
- validator verzamelt markeringen in bronvolgorde;
- renderer heeft geen start/eind-marker-special cases;
- MusicXML bepaalt later welke markeringen relevant zijn.
