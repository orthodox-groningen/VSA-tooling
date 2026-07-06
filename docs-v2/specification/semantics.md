# Semantiek

Status: **geconsolideerde werkversie**.

## Scope

Dit document beschrijft de betekenis van syntactisch geldige VSA-notatie.

## Muzikale positie

De kleinste muzikale eenheid is de muzikale positie.

Een positie representeert één gezongen toon met relatieve hoogte en duur.

## Hoogte

Hoogte-modifiers beschrijven relatieve melodische beweging binnen de gekozen do-context en modus.

Een hoogte-markering is een positionele node in de documentstroom.

Regel:

```text
eerste hoogte-markering = beginhoogte
latere hoogte-markering = lokale hoogte op die positie
```

Een eindmarkering is optioneel.

Het ontbreken van een eindmarkering is geen semantische fout.

Een eindmarkering `[:]` betekent neutrale hoogte en is equivalent aan `[-:]` of `[~:]`.

## Duur

Lengte-modifiers beschrijven duur, verlenging of positionele duurinformatie.

De concrete exportmapping hoort bij het gekozen `duration-model`.

## Positionele koppeling

Hoogte- en lengte-informatie binnen een scope zijn positioneel gekoppeld.

Wanneer beide aanwezig zijn, moeten de aantallen muzikale posities overeenkomen.

Een mismatch is een semantische fout of diagnostiek volgens het foutmodel.

## Validatie

De validator mag controleren:

- geldigheid van hoogte-markeringen;
- geldigheid van modifiers;
- positionele koppeling tussen hoogte en lengte;
- eindtooncontrole wanneer `validate-ending` actief is;
- betekenis van markeringen binnen gekozen toon- en moduscontext.

De validator mag niet eisen dat:

- de eerste hoogte-markering helemaal aan het begin staat;
- de laatste hoogte-markering helemaal aan het einde staat;
- er geen tekst vóór de eerste hoogte-markering staat;
- er geen tekst na de laatste hoogte-markering staat.

## Foutmodel

Een implementatie onderscheidt bij voorkeur:

- syntactische fouten;
- semantische fouten;
- recoverable diagnostiek;
- waarschuwingen.

Recoverable diagnostiek mag verdere parsing, validatie of rendering niet onnodig blokkeren.
