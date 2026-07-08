# Design Principles

## Doel

Dit document beschrijft de fundamentele ontwerpprincipes van VSA (Vereenvoudigde Slavische Accentnotatie).

Deze principes vormen de basis voor ontwerpbeslissingen binnen de specificatie en de referentie-implementatie. Bij twijfel hebben deze principes richtinggevende waarde.

---

# De specificatie staat centraal

De VSA-specificatie is de primaire bron van waarheid.

Implementaties volgen uit de specificatie. De specificatie wordt niet aangepast aan de beperkingen of voorkeuren van een implementatie.

---

# Semantiek vóór implementatie

VSA beschrijft de betekenis van een document, niet de wijze waarop deze betekenis intern wordt verwerkt.

Programmeertaal, datastructuren, algoritmen en softwarearchitectuur behoren tot de implementatie en maken geen onderdeel uit van de taal.

---

# Semantiek vóór rendering

De betekenis van een VSA-document staat los van de uiteindelijke presentatie.

Rendering is een afgeleide van de semantiek en mag de betekenis van een document niet beïnvloeden.

---

# Scheiding van verantwoordelijkheden

Iedere architectuurlaag heeft één duidelijk afgebakende verantwoordelijkheid.

In het bijzonder worden de volgende verantwoordelijkheden gescheiden gehouden:

* lexicale analyse;
* syntactische analyse;
* semantische analyse;
* validatie;
* layout;
* rendering.

Deze scheiding bevordert onderhoudbaarheid, uitbreidbaarheid en alternatieve implementaties.

---

# Implementatie-onafhankelijkheid

De specificatie schrijft geen programmeertaal, parsertechniek, datastructuren of rendererarchitectuur voor.

Conforme implementaties mogen intern volledig van elkaar verschillen, zolang het extern waarneembare gedrag overeenkomt met de specificatie.

---

# Deterministisch gedrag

Een geldig VSA-document behoort altijd dezelfde semantische betekenis te hebben.

Implementatieverschillen mogen niet leiden tot verschillende interpretaties van hetzelfde document.

---

# Achterwaartse compatibiliteit

Binnen een MAJOR-versie blijft bestaande functionaliteit behouden.

Nieuwe mogelijkheden worden bij voorkeur toegevoegd zonder bestaande documenten ongeldig te maken of hun betekenis te wijzigen.

---

# Eenvoud boven complexiteit

Nieuwe taalconstructies worden uitsluitend toegevoegd wanneer zij aantoonbare functionele meerwaarde bieden.

Complexiteit zonder duidelijke meerwaarde wordt vermeden.

---

# Uitbreidbaarheid

De taal wordt zodanig ontworpen dat toekomstige uitbreidingen mogelijk blijven zonder bestaande documenten of implementaties onnodig te verstoren.

---

# Leesbaarheid

Een VSA-document is bedoeld om zowel door mensen als door software verwerkt te kunnen worden.

Daarom streeft VSA naar een evenwicht tussen menselijke leesbaarheid en formele eenduidigheid.

---

# Objectiviteit

Normatieve regels beschrijven uitsluitend het gewenste gedrag.

Ontwerpkeuzes worden gebaseerd op technische argumenten en niet op voorkeuren voor een specifieke implementatie of programmeerstijl.
