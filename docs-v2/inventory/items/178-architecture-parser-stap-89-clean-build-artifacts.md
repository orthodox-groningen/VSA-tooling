# Inventarisatie 178 — Stap 89 - clean build artifacts

## Huidige locatie

`docs/architecture/parser-stap-89-clean-build-artifacts.md`

## Documenttype

Historie / ontwikkelstap

## Doelgroep

Nog te bevestigen.

## Inhoudelijke samenvatting

Oude routes bleven verschijnen doordat generated output niet volledig werd opgeschoond vóór een nieuwe Hugo-build. Daarnaast was `build-hugo.cmd` kwetsbaar voor patchscripts die regels midden in een `hugo ^` blok invoegden. `build-hugo.cmd` is opnieuw compact gemaakt en gebruikt nu:

## Belangrijke koppen

- `# Stap 89 - clean build artifacts`
- `## Probleem`
- `## Oplossing`

## Relaties met andere documenten

Nog te bepalen tijdens de overlap-analyse.

## Overlap met andere documenten

Nog te bepalen tijdens de overlap-analyse.

## Voorgestelde bestemming

`docs-v2/history/parser/parser-stap-89-clean-build-artifacts.md`

## Status inventarisatie

Eerste inventarisatie op basis van bestandsnaam, koppen en inhoudsscan.

## Opmerkingen

Controleer in fase 1 of dit document normatieve inhoud bevat die niet verloren mag gaan bij latere samenvoeging.
