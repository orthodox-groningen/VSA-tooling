# 068 — Parser stap 3 fix

## Huidige locatie

```text
docs/architecture/parser-stap-3-fix.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

De parser kiest nu expliciet: [hoogte-modifier] + zangelement + [lengte-modifier] Daarbij probeert hij geldige prefix- en suffix-modifiers te vinden en blijft het middelste deel het zangelement. Voorbeeld: {/&\&/tekst_&~&~} wordt: height_modifier = ["/", "\", "/"] text            = "tekst" length_modifier = ["_", "~", "~"]

## Relaties met andere documenten

Nog te detailleren tijdens inhoudelijke consolidatie.

## Overlap met andere documenten

Nog te detailleren tijdens inhoudelijke consolidatie.

## Voorgestelde bestemming

```text
docs-v2/history/parser/
```

## Inventarisatiestatus

Eerste classificatie op basis van bestandsnaam, locatie en documentkop.

## Opmerkingen

Geen inhoud migreren in fase 1; alleen classificeren en later controleren.
