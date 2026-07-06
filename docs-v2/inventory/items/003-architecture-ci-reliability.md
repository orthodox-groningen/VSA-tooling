# Inventarisatie 003 — CI-betrouwbaarheid (VSA-tooling)

## Huidige locatie

`docs/architecture/ci-reliability.md`

## Documenttype

Architectuur / ontwerpnotitie

## Doelgroep

Nog te bevestigen.

## Inhoudelijke samenvatting

Strategie om GitHub Actions-fouten te verminderen. Doel: **falen vóór deploy**, **één publicatiemechanisme**, **geen dubbel werk op dezelfde push**. Preview-deploy draait **geen pytest** meer: dezelfde push triggert al `python-tests` en

## Belangrijke koppen

- `# CI-betrouwbaarheid (VSA-tooling)`
- `## 1. Scheiding build vs. publicatie`
- `## 2. Eén GitHub Pages-mechanisme`
- `## 3. Concurrency op Pages`
- `## 4. Fail-fast vóór deploy`
- `## 5. Bron-sync en validate`
- `## 6. Lokaal hetzelfde pad als CI`
- `## 7. Als preview-deploy toch faalt`
- `## 8. Herbruikbare Pages-deploy (org-breed)`
- `## 9. Verdere verbeteringen (optioneel)`

## Relaties met andere documenten

Nog te bepalen tijdens de overlap-analyse.

## Overlap met andere documenten

Nog te bepalen tijdens de overlap-analyse.

## Voorgestelde bestemming

`docs-v2/architecture/ci-reliability.md`

## Status inventarisatie

Eerste inventarisatie op basis van bestandsnaam, koppen en inhoudsscan.

## Opmerkingen

Controleer in fase 1 of dit document normatieve inhoud bevat die niet verloren mag gaan bij latere samenvoeging.
