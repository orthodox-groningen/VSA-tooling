# Onderzoek naar tropaar- en kondakmelodieën in VSA

Ik wil een onderzoek uitvoeren naar de manier waarop **tropaar- en kondakmelodieën** in VSA kunnen worden gemodelleerd, als voorbereiding op een toekomstige uitbreiding van VSA naar meerstemmigheid.

## Achtergrond

VSA (Vereenvoudigde Slavische Accentnotatie) modelleert momenteel één melodielijn.

Voor Russische/Orthodoxe liturgische muziek is het echter nuttig om meerstemmigheid te kunnen modelleren. Uiteindelijk willen we een VSA-model ontwikkelen waarmee onder meer vierstemmige muziek kan worden beschreven en vervolgens naar **MusicXML** kan worden geëxporteerd.

Voordat we syntax of een AST voor meerstemmigheid ontwerpen, wil ik eerst begrijpen hoe de bestaande melodische patronen en tekstkoppeling in de praktijk werken.

### Specifiek onderzoeksobject

Ik wil beginnen met **troparen en kondaken**, omdat deze gebruikmaken van de tropaarmelodie.

Ik beschik over Markdown-bestanden waarin bestaande VSA-blokken staan. Daarin moeten relevante voorbeelden van troparen en kondaken worden gevonden.

Daarnaast beschik ik over een PDF met notenbalken waarin voor elk van de acht tonen de volgende melodieën zijn opgenomen:

* versmelodie;
* stichiermelodie;
* tropaarmelodie.

In die notenbalken staan geen lyrics. De bedoeling is dat de lettergrepen/woorden van een gegeven tropaartekst met behulp van de tekens en markeringen van de tropaarmelodie, waaronder `e. st.`, `l. st.`, `laatste` en `vl. st.` (met pijlen), hun plaats in de melodie vinden.

Sommige noten staan tussen haakjes. Dat betekent dat deze noten onderdeel zijn van de melodische template, maar afhankelijk van de tekst niet noodzakelijk worden gezongen.

## Doel van het onderzoek

Onderzoek eerst **wat deze bestaande notatie en markeringen semantisch betekenen**.

We willen uiteindelijk kunnen begrijpen:

1. hoe een tropaarmelodie als melodisch template kan worden beschreven;
2. hoe een tekst aan zo'n template wordt gekoppeld;
3. wat `e. st.`, `l. st.`, `laatste`, `vl. st.` en eventuele andere markeringen precies betekenen;
4. welke delen van de melodie vast zijn en welke afhankelijk zijn van de tekst;
5. hoe verschillende teksten met hetzelfde melodische type op dezelfde manier kunnen worden verwerkt;
6. welke informatie uiteindelijk in VSA moet worden gerepresenteerd;
7. hoe dit model later naar MusicXML kan worden vertaald.

**Ontwerp van nieuwe VSA-syntax is nadrukkelijk nog niet het doel van de eerste onderzoeksfase.**

Eerst moet het muzikale en semantische model worden begrepen.

---

# Werkwijze

Werk als een onderzoeker: verzamel eerst bewijs en trek pas daarna conclusies.

## Stap 1 — inventariseer het beschikbare materiaal

Wanneer ik Markdown-bestanden, PDF's of andere bestanden aanlever:

* lees en analyseer ze;
* identificeer relevante passages;
* zoek specifiek naar troparen en kondaken;
* groepeer voorbeelden waar mogelijk per toon;
* bewaar de oorspronkelijke VSA-notatie en tekst als bronmateriaal.

Verander de aangeleverde bestanden niet.

## Stap 2 — vraag mij gericht om ontbrekend materiaal

Je hoeft niet te wachten totdat ik zelf bedenk wat je nodig hebt.

Als er onvoldoende voorbeelden zijn, vraag mij dan expliciet om bijvoorbeeld:

* een specifiek Markdown-bestand;
* een voorbeeld voor een bepaalde toon;
* een tweede voorbeeld van dezelfde toon;
* een scan/PDF van een bepaalde pagina;
* de bijbehorende tekst;
* een voorbeeld waarin een bepaalde markering voorkomt.

**Vraag steeds alleen om materiaal dat daadwerkelijk nodig is voor de volgende onderzoeksvraag.**

Leg kort uit waarom je dat voorbeeld nodig hebt.

## Stap 3 — vergelijk voorbeelden

Vergelijk meerdere voorbeelden van dezelfde toon en vervolgens voorbeelden van verschillende tonen.

Let onder meer op:

* melodische patronen;
* tekstlengte;
* syllabering;
* plaatsing van tekst ten opzichte van noten;
* herhaling;
* optionele noten;
* haakjes;
* `e. st.`;
* `l. st.`;
* `laatste`;
* `vl. st.`;
* pijlen;
* andere nog onbekende markeringen;
* verschillen tussen teksten die dezelfde melodie gebruiken.

Maak onderscheid tussen:

**waargenomen feit**

> Dit komt in drie voorbeelden voor.

**hypothese**

> Dit lijkt erop te wijzen dat `e. st.` ...

**conclusie**

> Na vergelijking met voldoende onafhankelijke voorbeelden kunnen we aannemen dat ...

Presenteer een hypothese nooit als vastgesteld feit.

## Stap 4 — probeer hypotheses te falsificeren

Wanneer je denkt te weten wat een teken betekent, zoek dan actief naar voorbeelden waarin die interpretatie niet zou werken.

Bijvoorbeeld:

> Als `e. st.` altijd het einde van een bepaalde tekstuele eenheid betekent, zoeken we een voorbeeld waarin `e. st.` voorkomt bij een andere tekststructuur.

Een interpretatie die niet door meerdere voorbeelden wordt ondersteund, moet als voorlopig worden aangemerkt.

---

# Belangrijke uitgangspunten

### Niet vooruitlopen op syntax

Ontwerp nog geen syntax zoals:

```text
stem1: ...
stem2: ...
```

of een ander concreet VSA-formaat voor meerstemmigheid, tenzij we daar later bewust aan beginnen.

Eerst het semantische model.

### Geen aannames uit algemene kennis

Gebruik de aangeleverde bronnen als primaire basis.

Als algemene kennis over Russische of Orthodoxe kerkmuziek wordt gebruikt, vermeld dan duidelijk dat dit externe kennis is en niet rechtstreeks uit het aangeleverde materiaal afkomstig is.

Als iets niet uit het bronmateriaal kan worden vastgesteld, zeg dat expliciet.

### Bestaande VSA respecteren

De bestaande VSA-specificatie en terminologie zijn uitgangspunt.

Veronderstel niet dat bestaande VSA-concepten moeten worden vervangen omdat een andere modellering gemakkelijker lijkt.

### Behoud van praktische bruikbaarheid

Bij een toekomstig ontwerp moeten minstens deze eigenschappen behouden blijven:

* gemakkelijk intypen;
* gemakkelijk lezen;
* gemakkelijk onderhouden en corrigeren;
* geschikt voor menselijke auteurs;
* eenduidig interpreteerbaar;
* geschikt voor verwerking door software;
* uiteindelijk omzetbaar naar MusicXML.

Maar **optimaliseer daar pas voor nadat duidelijk is welke muzikale informatie daadwerkelijk moet worden vastgelegd.**

---

# Onderzoeksresultaat

Werk uiteindelijk toe naar een documentatie van het muzikale model, niet direct naar syntax.

Daarin moet duidelijk worden:

1. welke elementen een tropaar/kondak-melodie bevat;
2. welke elementen tekstafhankelijk zijn;
3. welke elementen vast zijn;
4. hoe tekst en melodie aan elkaar worden gekoppeld;
5. welke betekenis iedere relevante markering heeft;
6. welke uitzonderingen bestaan;
7. welke onzekerheden nog bestaan;
8. welke gegevens een toekomstige VSA-representatie minimaal moet kunnen bevatten.

Pas wanneer dit model voldoende duidelijk is, gaan we onderzoeken hoe het elegant in VSA-syntax en AST kan worden gerepresenteerd.

## Belangrijk

Neem gedurende het onderzoek **niet automatisch aan dat je al genoeg informatie hebt**.

Als een conclusie onvoldoende onderbouwd is, vraag mij om meer voorbeelden.

Ik wil dit onderzoek iteratief uitvoeren: jij analyseert het beschikbare materiaal, formuleert de volgende concrete onderzoeksvraag en vraagt mij vervolgens om precies de bestanden of voorbeelden die nodig zijn om die vraag te beantwoorden.

Begin dus met het inventariseren van het beschikbare materiaal en stel daarna de **eerste gerichte vraag** die nodig is om het onderzoek voort te zetten.
