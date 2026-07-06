# 174 — Stap 85 - fix Hugo linkchecker tests

## Huidige locatie

```text
docs/architecture/parser-stap-85-fix-hugo-link-checker-tests.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

- `LinkRef` gebruikt `NamedTuple` in plaats van `@dataclass`. - De testloader registreert de module in `sys.modules`. - De oude stap-75 test verwacht geen letterlijke `img=` tekst meer. Onder Python 3.14 kan `@dataclass` met postponed annotations mislopen bij import via `spec.loader.exec_module()` wanneer de module niet in `sys.modules` staat.

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
