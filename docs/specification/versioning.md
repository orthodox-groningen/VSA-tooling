# Versionering

## Doel

Dit document beschrijft het versiebeleid van de VSA-specificatie.

Het versiebeleid zorgt ervoor dat gebruikers en implementaties kunnen bepalen welke wijzigingen compatibel zijn en welke aanpassingen een nieuwe hoofdversie vereisen.

---

## Versienummering

De VSA-specificatie gebruikt semantische versienummering in de vorm:

```
MAJOR.MINOR
```

Bijvoorbeeld:

```
1.0
1.1
1.2
2.0
```

Patchversies maken geen onderdeel uit van de normatieve specificatie.

---

## MAJOR-versies

Een nieuwe MAJOR-versie wordt uitgebracht wanneer een wijziging niet achterwaarts compatibel is.

Voorbeelden zijn:

- wijziging van de grammatica waardoor bestaande documenten ongeldig worden;
- wijziging van de semantiek van bestaande constructies;
- verwijdering van bestaande taalconstructies;
- wijzigingen die bestaande conforme implementaties vereisen aan te passen.

---

### MINOR-versies

Een nieuwe MINOR-versie wordt uitgebracht voor achterwaarts compatibele uitbreidingen.

Voorbeelden zijn:

- nieuwe optionele taalconstructies;
- nieuwe directives;
- aanvullende validatieregels die bestaande geldige documenten niet ongeldig maken;
- verduidelijkingen van de specificatie zonder wijziging van de semantiek.

Een implementatie die versie *1.x* ondersteunt behoort documenten uit eerdere *1.x*-versies correct te kunnen verwerken, tenzij de specificatie uitdrukkelijk anders vermeldt.

---

## Correcties

Redactionele verbeteringen mogen worden aangebracht zonder wijziging van het versienummer, mits de normatieve betekenis van de specificatie ongewijzigd blijft.

Voorbeelden zijn:

- spelling;
- grammatica;
- verduidelijking van formuleringen;
- verbetering van voorbeelden.

---

## Verouderde onderdelen

Onderdelen kunnen als *deprecated* worden aangemerkt.

Een deprecated onderdeel:

- blijft geldig;
- behoudt zijn oorspronkelijke betekenis;
- behoort door conforme implementaties ondersteund te blijven binnen dezelfde MAJOR-versie.

Verwijdering van een deprecated onderdeel mag uitsluitend plaatsvinden in een volgende MAJOR-versie.

---

## Compatibiliteitsbeginsel

Bij twijfel wordt een wijziging als niet achterwaarts compatibel beschouwd.

Een wijziging wordt pas als achterwaarts compatibel beschouwd wanneer dit aantoonbaar kan worden onderbouwd.

---

## Compatibiliteit

Binnen dezelfde MAJOR-versie behoort een geldig VSA-document geldig te blijven.

Uitbreidingen mogen bestaande documenten niet ongeldig maken of hun betekenis wijzigen.

---

## Referentie-implementatie

De referentie-implementatie behoort dezelfde versie van de VSA-specificatie te ondersteunen als zij claimt te implementeren.

Afwijkingen tussen implementatie en specificatie behoren expliciet te worden gedocumenteerd.