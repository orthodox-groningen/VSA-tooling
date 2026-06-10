## Appendix 1 - Uitleg van notatie volgens Nederlands Liturgikon

De volgende tekst komt uit het Liturgikon, pp 27-30 (een uitgave van
de Nederlands Orthodoxe Kerk, dr. Kuyperstraat 2, den Haag, maart 1968):

### De Muziek

Hoewel overal in de Orthodoxe Kerken dezelfde liturgische teksten worden gebruikt,  
is er geen algemene muziektraditie. In Griekenland en de Balkanlanden worden nog  
de oude eenstemmige melodieën gebruikt, die echter merkbaar een Turkse invloed  
hebben ondergaan.

De Russische Kerk heeft sinds een eeuw de meerstemmige muziek ingevoerd,  
volgens de Europese harmonieleer. Het gebruik van een of meer tegenstemmen  
is al veel ouder. Ook de Griekse kerkmuziek kent de *ison*, de op één toonhoogte  
aangehouden begeleidende grondtoon.

De Nederlandse Kerk, evenals de meeste Missiekerken, heeft zich aangesloten  
bij het Russische gebruik, omdat dit reeds met beperkte en weinig‑geschoolde  
krachten tot een aannemelijk resultaat voert.

Maar ook in deze melodieën is veel verscheidenheid, zodat een bepaalde keuze  
gedaan moest worden. Om voor de hand liggende redenen zijn hiervoor meestal  
de eenvoudigste voorbeelden genomen.

Alle russische componisten hebben ook kerkmuziek geschreven.  
Veel daarvan draagt een concertkarakter of is slechts voor grotere koren geschikt.  
Maar onder hun werk bevinden zich ook onsterfelijk‑schone eenvoudige melodieën.  
Wie slechts ééns het vastenlied *‘Aan de stromen van Babylon…’* of op Goede Vrijdag  
*‘De rechtvaardige Josef…’* heeft horen zingen, weet dat hij deze zangen nooit meer  
vergeten zal. En eigenlijk kan hetzelfde al gezegd worden van het gewone  
*Kyrie eleison*, of het *‘Wij prijzen U…’* van elke heilige Liturgie.

De vierstemmige liturgiemuziek is apart uitgegeven.  
In deze uitgave is alleen de melodie aangegeven, in een vereenvoudigd neumenschrift.

###De Muzieknotatie

Deze kan het best duidelijk gemaakt worden aan de hand van enkele voorbeelden.

![Drie voorbeelden van de notatie](liturgikon-voorbeelden.jpg)

De tekens bóven de tekst geven een verandering van toonhoogte aan.  
Het aantal boven elkaar geplaatste stijgende of dalende strepen betekent een  
stijging of daling van de melodie van evenveel tonen.

Wanneer een notengroep op dezelfde toon begint als de laatstgezongen toon,  
wordt deze aangegeven met een horizontaal streepje  
(zie het begin van het derde voorbeeld).

Om de plaats van de melodie in de toonladder vast te leggen, wordt voor het stuk  
de eerste toon aangegeven. Staat er alleen een liggend streepje, dan begint de zang  
op de grondtoon (do). Hiervoor wordt, zo mogelijk, de toon van priester of diaken  
aangehouden.

Deze ‘do’ moet dus niet verward worden met de ‘c’, die een vaste toonhoogte heeft.  
Staat een stuk met één kruis geschreven, dan is ‘g’ de grondtoon of de ‘do’, enz.  
Zo is in het tweede voorbeeld de begintoon een ‘mi’, maar die zal in werkelijkheid  
gezongen worden op ‘a’, of in die buurt. Dit moet de koorleider bepalen.

De gekozen notatie geeft dus uitsluitend de relatieve toonhoogte aan ten opzichte  
van de laatst gezongen toon, d.w.z. dat als men ergens een verkeerd interval  
genomen heeft, dan de hele rest verkeerd uitkomt; maar bij enigermate bekende  
melodieën bestaat hiervoor in de praktijk geen gevaar. Het is natuurlijk een nadeel,  
maar daar staat tegenover dat deze tekens veel vlotter geleerd worden dan noten  
lezen, en dat het gebruik mogelijk is waar muzieknotatie te kostbaar zou zijn.  
De slottoon wordt telkens aangegeven, om de overgang naar een volgend stuk te weten.

*(Afbeelding 2)*

Een kruis (+) betekent een extra stijging van een halve toon;  
een mol (b) een extra daling van een halve toon.  
Zo worden ze ook als herstellingsteken gebruikt (zie 3e voorbeeld).

Wanneer een zelfde melodietje steeds herhaald wordt, zoals bv. in de Zaligsprekingen,  
dan worden deze tekens niet steeds weer geschreven, omdat het oor zich

Een kruis (+) betekent een extra stijging van een halve toon;  
een mol (♭) een extra daling van een halve toon.  
Zo worden ze ook als herstellingstekens gebruikt (zie 3e voorbeeld).

Wanneer een zelfde melodietje steeds herhaald wordt, zoals bv. in de Zaligsprekingen,  
dan worden deze tekens niet steeds weer geschreven, omdat het oor zich gemakkelijk  
aanpast aan de andere toonschaal.

De tekens onder de tekst geven de duur van de tonen aan.  
Zonder teken duurt elke noot één tel, of een kwartnoot.  
Een horizontale onderstreping verdubbelt de duur tot een halve noot, twee tellen.  
Dubbele onderstreping is vier of drie tellen (zie slot van 2e en 3e voorbeeld).

Een punt of verticaal streepje onder de tekst maakt deze tot een achtste noot  
of halve tel (zie 3e voorbeeld).

Het einde van een muzikaal zinsdeel wordt aangegeven door een sterretje (*)  
tussen de tekst, en dit zal dus vaak een rustteken zijn.

Er is geen strakke maat: het ritme moet de zinsbouw en de betekenis  
zo duidelijk mogelijk doen uitkomen.

De muziektekens zijn een uiterste vereenvoudiging van het oude Neumenschrift,  
uit de tijd dat er nog geen notenbalk was uitgevonden.  
Zij hebben het voordeel van een heel grote ruimtebesparing,  
en zijn vooral bruikbaar voor eenvoudige melodieën,  
zoals die juist in de kerkmuziek het meeste voorkomen.  
Ze kunnen ook gemakkelijk aan bestaande boeken worden toegevoegd.

### Relatie tussen de Liturgikon-notatie en VSA

De VSA-notatie is sterk geïnspireerd door de vereenvoudigde neumennotatie zoals beschreven in het Nederlands Liturgikon (1968), maar is daar niet volledig identiek aan. VSA formaliseert en generaliseert verschillende aspecten van deze praktijknotatie om parsing, validatie, rendering en export naar formaten zoals MusicXML mogelijk te maken.

De belangrijkste verschillen zijn:

| Onderwerp | Liturgikon-notatie | VSA |
|-----------|-------------------|-----|
| Doel      | Praktische zanghulp voor menselijke zangers | Formele, machine-verwerkbare notatie |
| Syntax    | Geen formele grammatica | Volledig formele syntax (EBNF) |
| Structuur | Markeringen direct boven/onder tekst | Gestructureerde scopes `{...}` |
| Toonhoogte | Relatieve intervalnotatie | Relatieve toonladder-notatie binnen een do-context |
| `+/` en `-\` | Extra halve toon bovenop een bestaande beweging | Zelfstandige halve ladderstap |
| Lege posities | Impliciet | Expliciet via `~` |
| Melisma   | Impliciet / ad hoc | Formeel model via samengestelde modifiers |
| Validatie | Alleen muzikaal gehoor | Syntactische en semantische validatie |
| Export    | Niet voorzien | SVG en MusicXML |

Het grootste inhoudelijke verschil betreft de interpretatie van `+/` en `-\`. In het Liturgikon staat dat een kruis (+) een *extra* stijging van een halve toon betekent (en een mol (b) een *extra* daling van een halve toon). Dit wordt gestaafd door het bijbehorende voorbeeld. Echter, een dergelijke notatie maakt het dan onmogelijk om een halve ladderstap omhoog of omlaag te gaan. De zangpraktijk van de auteur is dat `+/` en `-\` (ook?) worden gebruikt om een stijging/daling van een halve toon mee aan te geven. Dat is ook zoals zij in VSA worden geïnterpreteerd: als zelfstandige relatieve toonhoogtebewegingen van een halve ladderstap.

Bij omzetting van historische notaties naar VSA kunnen daardoor de volgende situaties optreden:

- een historische `+/` moet soms worden herschreven als een combinatie van een hele en halve beweging;
- de exacte melodische uitkomst kan afhankelijk zijn van de gekozen modus en do-context;
- historische notaties laten sommige toonladderinformatie impliciet, terwijl VSA die expliciet moet modelleren;
- melismatische passages moeten in VSA soms explicieter worden gespecificeerd dan in historische bronnen.

VSA moet daarom worden gezien als een geformaliseerde afleiding van deze historische praktijknotatie, niet als een exacte reproductie ervan.