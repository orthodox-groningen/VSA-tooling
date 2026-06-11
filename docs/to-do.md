# TODO lijst

1. Parser/validator uitbreiden: strengere checks op pitch-markers, eindtoon, metadata.
3. SVG-rendering verbeteren: spacing, typografie, regels, glyph-posities, etc. (zie hieronder).
4. CLI netter maken (zie hieronder)
5. Demo-site afronden (zie verderop)
6. MusicXML-export starten (dat is een grote stap; zie ook hieronder): AST → MusicXML.

## CLI netter maken

1. betere foutmeldingen (alle foutmeldingen moeten niet alleen aangeven wat er fout is, en waar (bestand, regelnummer, positie), maar ook wat er concreet gebeuren moet om de fout op te lossen). foutmeldingen moeten bruikbaar zijn voor non-techies (zoals ik).
2. de terminologie in de foutmeldingen en andere hulpteksten moet correct zijn: zo is een `&` geen 'modifierteken', en als een positie in een regel een zangelement aangeeft, of een EHM, of een testgedeelte van een zangelement, of ..., dan mag dat wel duidelijk gezegd worden.
3. --help met wat uitgebreidere hulpteksten, zoals gebruikelijk bij dit soort tools
4. vsa <command> --help (of zo): uitgebreide hulptekst voor <command>, met uitgebreide beschrijving van inputs, locaties, exitcodes, etc. zoals ook in de hugo demo en in de referentie documentatie
5. mogelijk kan `vsa <errorcode> --help` meer informatie over de fout geven (met voorbeelden?). 
6. --help, foutmeldingen e.d. moeten allemaal praktisch nuttig zijn voor dagelijks gebruik.
7. Er mogen geen python foutmeldingen verschijnen - dat moeten allemaal nette foutcodes zijn
8. commando's die een fout genereren moeten als het even kan doorgaan met wat ze doen (bijvoorbeeld bij de parser of de semantische checker), zodat je meteen een lijst met fouten krijgt in plaats van dat je na elke fix een nieuwe run moet doen om de volgende fout te vinden.

## SVG-rendering verbeteren.

Je had het over: spacing, typografie, regels, glyph-posities, etc. Lijkt me prima. Hier alvast wat observaties van mij, maar ga eerst na wat je denkt dat er zoal nodig is, zodat we geen dingen missen.
1. Op dit moment worden de regels over de gehele breedte uitgesmeerd (tweezijdig uitgelijnd). Regels moeten links worden uitgelijnd.
3. in de toonhoogte markeringen aan begin en eind is het liggende streepje te breed, en ze staan beiden  ook te dicht op de tekst.
4. de streepjes boven de tekst zijn te groot en staan te ver van de tekst af. De streepjes boven de tekst hebben meer het karakter van een (gestapelde set) accenten aigu of grave, en zouden in geschreven tekst nog net tussen twee tekstregels passen. De strepen onder de tekst zijn ook iets te breed (ze beslaan blijkbaar de hele breedte van de positie, 80% lijkt me voldoende) en mogen ook iets dichter op de tekst, vergelijkbaar met een underline die dan niet door de letters gaan (dus niet door de 'staart' van de g of j).
5. er mag wel een of ander config file specificatie komen waarin gebruikers hun voorkeuren kunnen opgeven. Dan kunnen ze rendering-variabelen of keuze opties specificeren, zoals de kleur van streepjes (bovenkant zwart, onderkant rood als default), het te gebruiken font, de font grootte, e.d.

## demo-site afronden

1. Nieuwe README maken voor de repo waar mensen die de repo clonen wat aan hebben.
2. Repo opruimen. Wat kan er allemaal weg (omdat we het niet meer gebruiken)
3. alle pagina’s nalopen op tekst, links, voorbeelden, mobiel/tablet.
4. Controleren dat alle vsa-commando's 
   - in de hugo demo een eigen pagina hebben, met een specificatie van de commando-syntax, de inputs, outputs, parameters (wat die verwacht worden te zijn en waar ze verwacht worden), dat er voorbeelden zijn van inputs, outputs, en voorbeelden van wat parameters doen als dat niet al te triviaal is
   - in de handleiding ook zijn beschreven
5. nagaan of het mogelijk is in de hugo demo om gebruikers de mogelijkheid geven om parameters in te vullen om te zien welke effecten dat heeft, bijvoorbeeld de breedte van een SVG, andere rendering-variabelen of keuze opties.
6. Nagaan wat er veranderd is aan de oorspronkelijk VSA referentie v1 (v1.0) en aan de gebruikershandleiding documenten, en wat er nog aan gedaan moet worden, gegeven alle veranderingen in de code van de repo. In het bijzonder kan ik me voorstellen dat de gebruikershandleiding gebruik maakt van het feit dat er een hugo demo site bestaat waar lezers zelf dingen kunnen zien (zeker als ze daarin ook parameters kunnen uitproberen)
