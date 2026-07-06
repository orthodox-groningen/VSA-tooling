# 020 — Stap 111 - ControlTokenNode in AST

## Huidige locatie

```text
docs/architecture/parser-stap-111-control-token-ast-node.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

Control tokens krijgen een eigen AST-node voordat parserdispatch wordt gebouwd. ControlTokenNode( token="[/]", meaning="phrase_boundary", start=..., end=..., ) | Token | Meaning | |---|---| | `[*]` | `phrase_rest` | | `[/]` | `phrase_boundary` | | `[*?]` | `optional_phrase_rest` | | `[/?]` | `optional_phrase_boundary` |

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
