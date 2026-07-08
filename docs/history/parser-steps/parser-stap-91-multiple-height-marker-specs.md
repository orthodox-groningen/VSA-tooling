# Stap 91 - meerdere hoogte-markeringen

## Doel

Binnen één `::: vsa-notatie ... :::` blok mogen meerdere hoogte-markeringen voorkomen.

Een hoogte-markering heeft strikt deze vorm:

```text
[<EHM>:]
```

Daarbij is `<EHM>` een bestaande geldige EHM volgens de EHM-specificatie.

Voorbeelden van geldige hoogte-markeringen:

```text
[:]
[/\:]
[//:]
[\:]
[-:]
```

Voorbeelden van ongeldige hoogte-markeringen:

```text
[/&:]
[&:]
[/_ :]
```

`&` is geen onderdeel van een hoogte-markering.

## Positie

Er is geen voorschrift over de positie van hoogte-markeringen ten opzichte van gezongen tekst.

Toegestaan:

```text
[:] begintekst
tekst vóór [:]
tekst vóór [:] tekst na marker
tekst vóór [:] tekst tussen [\:] tekst erna
```

Dus:

- er mag tekst vóór de eerste hoogte-markering staan;
- er mag tekst na de laatste hoogte-markering staan;
- tussen hoogte-markeringen mag tekst staan;
- meerdere hoogte-markeringen mogen in hetzelfde blok staan.

## Semantiek

Elke hoogte-markering geeft een (toon)hoogte aan ten opzichte van de basistoon ('do').

Voor de eerste hoogte-markering wordt de hoogte (of basistoon) extern gegeven. 
In de praktijk van het zingen wordt dit aangegeven door de koorlei(st)er.
Binnen de context van conversies, bijvoorbeeld naar MusicXML, wordt dat gespecificeerd 
door de feitelijke conversie - dat is buiten de scope van VSA.

Elke volgende hoogte-markering geeft aan dat de zang op die positie op die hoogte moet zitten. 
Een latere hoogte-markering vervangt dus niet de eerdere markering als documentstructuur, maar introduceert een nieuwe pitch-positie in dezelfde melodische lijn.

Het is een gangbare praktijk om voor een zangstuk een hoogte-markering te schrijven,
en om dit ook aan het eind van een zangstuk te doen (ter controle voor zangers).
Indien twee zangstukken elkaar opvolgen, kan dat vanuit VSA perspectief dan ook
gezien worden als een enkel zangstuk met tussenliggende hoogte-markeringen.

## Rendering

De SVG-renderer behandelt alle hoogte-markeringen gelijk.

Dat betekent:

- dezelfde glyphfamilie;
- dezelfde plaatsingslogica;
- dezelfde koppeling aan de tekst-/positieflow;
- geen aparte visuele status voor "eerste" versus "latere" hoogte-markering.

Alleen de muzikale interpretatie verschilt:

- eerste markering: beginhoogte;
- volgende markeringen: doelhoogte op die positie.

## Parser-impact

De parser moet meerdere pitch-marker tokens binnen één VSA-blok accepteren.

Daarbij mag tekst vóór de eerste marker niet als fout worden behandeld.

Ook tekst na de laatste marker blijft gewone gezongen tekst.

## Validator-impact

De validator mag niet eisen dat een VSA-blok precies één hoogte-markering heeft.

De validator mag ook niet eisen dat de eerste token in een blok een hoogte-markering is.

Validatie moet zich richten op:

- syntactisch geldige marker;
- geldige EHM;
- geldige positie in de tokenstroom;
- consistente renderingposities.

## Niet in deze stap

Deze stap implementeert nog niet:

- parserwijzigingen;
- AST-wijzigingen;
- validatorwijzigingen;
- SVG-renderingwijzigingen.

Dat volgt in latere stappen.
