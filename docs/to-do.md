# TODO lijst

1. Parser/validator uitbreiden: strengere checks op pitch-markers, eindtoon, metadata.
3. SVG-rendering verbeteren: spacing, typografie, regels, glyph-posities, etc. (zie hieronder).
4. CLI netter maken: betere foutmeldingen (alle foutmeldingen moeten niet alleen aangeven wat er fout is, en waar (bestand, regelnummer, positie), maar ook wat er concreet gebeuren moet om de fout op te lossen), --help, command output, exitcodes. Wellicht dat de --help icm foutcodes meer informatie kan geven met voorbeelden. Het moet praktisch nuttig zijn voor dagelijks gebruik.
5. Demo-site afronden
- alle pagina’s nalopen op tekst, links, voorbeelden, mobiel/tablet.
- beste keuze als je eerst iets toonbaars/stabiels wilt.
1. MusicXML-export starten
- AST → MusicXML.
- grotere stap; pas doen als parser/semantiek stevig genoeg zijn.

## SVG-rendering verbeteren.

1. Op dit moment worden de regels over de gehele breedte uitgesmeerd (tweezijdig uitgelijnd). Regels moeten links worden uitgelijnd.
2. in de toonhoogte markeringen aan begin en eind is het liggende streepje te breed, en ze staan beiden  ook te dicht op de tekst.
3. de streepjes boven de tekst zijn te groot en staan te ver van de tekst af. De streepjes boven de tekst hebben meer het karakter van een (gestapelde set) accenten aigu of grave, en zouden in geschreven tekst nog net tussen twee tekstregels passen. De strepen onder de tekst zijn ook iets te breed (ze beslaan blijkbaar de hele breedte van de positie, 80% lijkt me voldoende) en mogen ook iets dichter op de tekst, vergelijkbaar met een underline die dan niet door de letters gaan (dus niet door de 'staart' van de g of j).
4. er mag wel een of ander config file specificatie komen waarin gebruikers hun voorkeuren kunnen opgeven. Dan kunnen ze rendering-variabelen of keuze opties specificeren, zoals de kleur van streepjes (bovenkant zwart, onderkant rood als default), het te gebruiken font, de font grootte, e.d. 


## Afwerking

1. Nieuwe README maken voor de repo waar mensen die de repo clonen wat aan hebben.
2. Repo opruimen. Wat kan er allemaal weg (omdat we het niet meer gebruiken)
3. Controleren dat alle vsa-commando's 
   - in de hugo demo een eigen pagina hebben, met een specificatie van de commando-syntax, de inputs, outputs, parameters (wat die verwacht worden te zijn en waar ze verwacht worden), dat er voorbeelden zijn van inputs, outputs, en voorbeelden van wat parameters doen als dat niet al te triviaal is
   - in de handleiding ook zijn beschreven
4. Nagaan wat er veranderd is aan de oorspronkelijk VSA referentie v1 (v1.0) en aan de gebruikershandleiding documenten, en wat er nog aan gedaan moet worden, gegeven alle veranderingen in de code van de repo. In het bijzonder kan ik me voorstellen dat de gebruikershandleiding gebruik maakt van het feit dat er een hugo demo site bestaat waar lezers zelf dingen kunnen zien (zeker als ze daarin ook parameters kunnen uitproberen)

## Nieuwe dingen

1. In de hugo demo de mogelijkheid geven om parameters in te vullen om te zien welke effecten dat heeft, bijvoorbeeld de breedte van een SVG, andere rendering-variabelen of keuze opties.