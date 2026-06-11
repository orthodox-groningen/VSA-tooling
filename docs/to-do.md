# TODO lijst

1. Demo-site afronden
- alle pagina’s nalopen op tekst, links, voorbeelden, mobiel/tablet.
- beste keuze als je eerst iets toonbaars/stabiels wilt.
2. Parser/validator uitbreiden
- strengere checks op pitch-markers, eindtoon, metadata.
- beste keuze als betrouwbaarheid voorop staat.
3. SVG-rendering verbeteren
- spacing, typografie, regels, glyph-posities.
- beste keuze als de zichtbare output nog niet netjes genoeg is.
4. MusicXML-export starten
- AST → MusicXML.
- grotere stap; pas doen als parser/semantiek stevig genoeg zijn.
5. CLI netter maken
- betere foutmeldingen, --help, command output, exitcodes.
- praktisch nuttig voor dagelijks gebruik.

## SVG-rendering verbeteren.

1. Op dit moment worden de regels over de gehele breedte uitgesmeerd (tweezijdig uitgelijnd). Regels moeten links worden uitgelijnd.
2. in de toonhoogte markeringen aan begin en eind is het liggende streepje te breed, en ze staan beiden  ook te dicht op de tekst.
3. de streepjes boven de tekst zijn te groot en staan te ver van de tekst af. De streepjes boven de tekst hebben meer het karakter van een (gestapelde set) accenten aigu of grave, en zouden in geschreven tekst nog net tussen twee tekstregels passen. De strepen onder de tekst zijn ook iets te breed (ze beslaan blijkbaar de hele breedte van de positie, 80% lijkt me voldoende) en mogen ook iets dichter op de tekst, vergelijkbaar met een underline die dan niet door de letters gaan (dus niet door de 'staart' van de g of j).
4. 
5. er mag wel een of ander config file specificatie komen waarin gebruikers hun voorkeuren kunnen opgeven. Dan kunnen ze rendering-variabelen of keuze opties specificeren, zoals de kleur van streepjes (bovenkant zwart, onderkant rood als default), het te gebruiken font, de font grootte, e.d. 

## Losse flodders


1. Nieuwe README maken voor de repo waar mensen die de repo clonen wat aan hebben.
2. Repo opruimen. Wat kan er allemaal weg (omdat we het niet meer gebruiken)
3. 