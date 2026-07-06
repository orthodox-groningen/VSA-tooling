# 049 — Stap 17 fix - tekstwrapping

## Huidige locatie

```text
docs/architecture/parser-stap-17-fix-tekst-wrapping.md
```

## Documenttype

ontwikkelgeschiedenis / architectuurstap

## Doelgroep

ontwikkelaar / maintainer

## Inhoudelijke samenvatting

De eerste multiline-renderer behandelde gewone tekstnodes als ondeelbaar. Voorbeeld: TextNode(" is de Heer, en heilig is Zijn Naam. ") Dat gaf onnodige witruimte wanneer daarna een scope kwam. Deze patch splitst tekstnodes in woordsegmenten: "is " "de " "Heer, " "en " ... Scopes blijven wel ondeelbaar, zodat VSA-markeringen niet losraken van hun zangelement.

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
