# Fase 2 migratieplan

## Doel

Fase 2 maakt de definitieve kapstok voor `docs-v2/` en bepaalt in welke volgorde bestaande documenten worden samengevoegd.

`docs/` blijft ongewijzigd.

## Migratievolgorde

| Stap | Doel | Output |
|---:|------|--------|
| 2.1 | Kapstok aanmaken | Hoofdmappen en README's |
| 2.2 | Migratieplan vastleggen | Dit document |
| 2.3 | Specificatie-cluster bepalen | `process/specification-cluster.md` |
| 2.4 | Eerste normatieve specificatie schrijven | `specification/syntax.md` |
| 2.5 | Semantiek en validatie schrijven | `specification/semantics.md` |
| 2.6 | Rendering specificeren | `specification/rendering.md` |
| 2.7 | CLI en configuratie beschrijven | `reference/cli.md`, `reference/configuration.md` |
| 2.8 | Architectuur consolideren | `architecture/*.md` |
| 2.9 | Historie ordenen | `history/parser/` |
| 2.10 | Gebruikersdocumentatie schrijven | `getting-started/`, `guides/` |

## Werkregel

Per stap wordt alleen `docs-v2/` opgeleverd.

Er wordt pas inhoud uit meerdere oude documenten samengevoegd nadat de gebruikte brondocumenten expliciet in een clusterbestand zijn vastgelegd.

## Eerste inhoudelijke cluster

De eerste inhoudelijke migratie wordt het specificatiecluster.

Dat cluster bepaalt welke bestaande documenten normatieve informatie bevatten voor:

- syntax;
- semantiek;
- validatie;
- rendering;
- configuratie;
- control tokens;
- comments;
- directives.

Daarna wordt pas `specification/syntax.md` geschreven.
