# Stap 81 - Hugo navigatie stabiliseren

## Wijzigingen

- `update-nav-placeholders.py` robuuster gemaakt;
- oude navigatie-artefacten worden opgeruimd;
- `vsa_nav_exclude: true` wordt ondersteund;
- dubbele pagina/sectie-links worden vermeden;
- `examples/examples` wordt verwijderd als obsolete prototype;
- stap-78 tests zijn teruggebracht tot compatibiliteitschecks.

## Belangrijk

Navigatie wordt alleen gegenereerd waar expliciete `VSA-NAV:*` markers staan.
