# TODO addendum stap 78

Toevoegen aan `docs/todo.md` onder demo-site:

## Navigatieblokken in `_index.md`

Status: `In uitvoering`

Besluit:

- `_index.md` blijft redactionele content;
- alleen het blok tussen `VSA-INDEX-NAV-START` en `VSA-INDEX-NAV-END` wordt automatisch bijgewerkt;
- scripts mogen niet langer complete `_index.md` pagina's herschrijven.

Nog controleren:

- alle relevante `_index.md` pagina's hebben redactionele intro;
- gegenereerde navigatie bevat Home/Omhoog/siblings/children waar logisch;
- build-script roept alleen `update-index-navigation-blocks.py` aan.
