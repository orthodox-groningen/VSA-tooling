# 078 — Stap 32 - site build workflow testfix

## Huidige locatie

```text
docs/architecture/parser-stap-32-site-build-test-fix.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

De workflow was correct, maar de test was te letterlijk. De werkende workflowregel is: "${GITHUB_REF}" == "refs/heads/main" De test zocht per ongeluk naar een variant zonder `}`. De test controleert nu robuuster: - `GITHUB_REF`; - `refs/heads/main`; - `target=production`; - `target=preview`.

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
