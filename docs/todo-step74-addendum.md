# TODO addendum stap 74

Toevoegen aan `docs/todo.md` onder demo-site:

## Praktijkvoorbeelden padwijziging controleren

Status: `In uitvoering`

De map `praktijk` is verplaatst naar een hoger niveau.

Controleer:

- indexnavigatie verwijst naar `/praktijk/`;
- oude links naar `/voorbeelden/praktijk/` zijn weg of bewust redirectbaar;
- SVG assetnamen gebruiken het actuele relatieve pad;
- generated HTML verwijst naar bestaande SVG assets;
- tests de nieuwe padstructuur als default gebruiken.
