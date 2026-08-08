# Conformiteit

## Doel

Dit hoofdstuk definieert wanneer een implementatie conform de VSA-specificatie is.

Conformance heeft uitsluitend betrekking op het extern waarneembare gedrag van een implementatie. Interne architectuur, datastructuren en programmeertaal zijn volledig implementatie-onafhankelijk.

---

# Conforming implementation

Een implementatie mag zichzelf uitsluitend aanduiden als *VSA-conform* indien alle relevante conformance-eisen uit deze specificatie worden nageleefd.

Een implementatie hoeft niet noodzakelijk alle onderdelen van VSA te ondersteunen. Conformance wordt daarom per component gedefinieerd.

---

# Conforming parser

Een parser is conform indien deze:

- de normatieve grammatica accepteert;
- alle geldige VSA-documenten correct parseert;
- ongeldige syntax detecteert;
- syntaxfouten rapporteert overeenkomstig de specificatie;
- dezelfde AST produceert als voorgeschreven door de semantiek van de specificatie.

De interne parserarchitectuur is niet voorgeschreven.

---

# Conforming validator

Een validator is conform indien deze:

- alle normatieve validatieregels toepast;
- fouten classificeert volgens de voorgeschreven severity;
- geen documenten accepteert die volgens de specificatie ongeldig zijn;
- geen geldige documenten afwijst.

Extra waarschuwingen zijn toegestaan, mits deze niet strijdig zijn met de specificatie.

---

# Conforming renderer

Een renderer is conform indien:

- de semantische betekenis van het document behouden blijft;
- alle normatieve renderregels worden gevolgd;
- de relatieve positie van tekst, hoogte- en lengtemarkeringen behouden blijft;
- de geproduceerde uitvoer visueel equivalent is aan de normatieve beschrijving.

Kleine verschillen in typografie, lettertype, afronding of SVG-optimalisatie zijn toegestaan zolang de betekenis niet verandert.

---

# Conforming CLI

Een command-line interface is conform indien:

- alle normatieve commando's ondersteunt;
- voorgeschreven foutcodes gebruikt;
- de gespecificeerde invoer en uitvoer respecteert;
- dezelfde resultaten produceert als andere conforme implementaties.

Extra commando's zijn toegestaan zolang zij bestaande functionaliteit niet wijzigen.

---

# Implementatievrijheid

De specificatie schrijft niet voor:

- programmeertaal;
- datastructuren;
- parsertechniek;
- rendererarchitectuur;
- interne API's;
- opslagformaat;
- buildproces.

Implementaties mogen hierin vrij afwijken zolang het extern waarneembare gedrag conform deze specificatie blijft.

---

# Extensies

Implementaties mogen aanvullende functionaliteit aanbieden.

Een extensie mag echter:

- de betekenis van bestaande VSA-documenten niet wijzigen;
- geldige VSA-documenten niet ongeldig maken;
- normatief gedrag niet overschrijven.

Extensies behoren duidelijk als zodanig herkenbaar te zijn.

---

# Referentie-implementatie

De officiële VSA-tooling is de referentie-implementatie van deze specificatie.

De referentie-implementatie dient als praktische bevestiging van de specificatie, maar vormt niet de normatieve bron. Bij eventuele verschillen is de specificatie leidend.