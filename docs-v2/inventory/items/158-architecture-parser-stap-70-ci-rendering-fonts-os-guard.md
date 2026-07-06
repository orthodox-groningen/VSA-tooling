# Inventarisatie 158 — Stap 70 - CI rendering fonts OS guard

## Huidige locatie

`docs/architecture/parser-stap-70-ci-rendering-fonts-os-guard.md`

## Documenttype

Historie / ontwikkelstap

## Doelgroep

Nog te bevestigen.

## Inhoudelijke samenvatting

GitHub Actions faalde omdat Linux-only fontinstallatie ook op Windows runners draaide. sudo apt-get update && sudo apt-get install -y fonts-dejavu-core Windows heeft geen `sudo`.

## Belangrijke koppen

- `# Stap 70 - CI rendering fonts OS guard`
- `## Fix`
- `## Script`
- `## Tests`

## Relaties met andere documenten

Nog te bepalen tijdens de overlap-analyse.

## Overlap met andere documenten

Nog te bepalen tijdens de overlap-analyse.

## Voorgestelde bestemming

`docs-v2/history/parser/parser-stap-70-ci-rendering-fonts-os-guard.md`

## Status inventarisatie

Eerste inventarisatie op basis van bestandsnaam, koppen en inhoudsscan.

## Opmerkingen

Controleer in fase 1 of dit document normatieve inhoud bevat die niet verloren mag gaan bij latere samenvoeging.
