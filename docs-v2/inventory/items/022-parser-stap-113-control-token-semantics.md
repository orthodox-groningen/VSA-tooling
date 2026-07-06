# 022 — Stap 113 - renderer-onafhankelijke control-token semantiek

## Huidige locatie

```text
docs/architecture/parser-stap-113-control-token-semantics.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Deze stap legt de betekenis van control tokens vast zonder parserwijziging. De parser herkent deze tokens dus nog niet als syntax. | Token | Abstracte meaning | |---|---| | `[*]` | `phrase_rest` | | `[/]` | `phrase_boundary` | | `[*?]` | `optional_phrase_rest` | | `[/?]` | `optional_phrase_boundary` |

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
