# Mijn eigen TODO lijst onderwerpen

1. Hoogte-controle bij laatste hoogte-marker

Het volgende is fout, maar wordt niet gedetecteerd

::: vsa-notatie
[//:] aap{/noot}{/mies} [:]
:::

2. Bij de analyse over het gebruik van `+/` en `-\` gebruik maken van de 'zaligsprekingen', Liturgikon pp. 54-55;

3. Het moet mogelijk zijn om in kommentaarblokken (of regelcommentaar) ongeldige syntax of semantiek te beschrijven. Er moeten dus manieren komen om aan te geven wat blok-commentaar en wat regel-commentaar is.

4. Als de gebruiker de fontgrootte schaalt, moeten de onder- en boven-glyphgs meeschalen.

5. Er moet syntax en (renderings)semantiek komen die toelaat dat het beginakkoord (voor SATB) ook in SVGs terecht gaat komen.

6. Binnen `::: vsa-notatie ... :::` constructies mogen meerdere hoogte-markeringen voorkomen. De eerste geeft de beginhoogte aan. Elke volgende geeft de hoogte aan waar op die positie de zang moet 'zitten'. Er is geen voorschrift over de posities van zulke markeringen ten opzichte van de (gezongen) tekst: er mag dus best tekst staan voor de eerste hoogtemarkering, en ook na de laatste. Daartussen mogen ook hoogtemarkeringen worden gezet. De SVG rendering behandelt alle hoogtemarkeringen op dezelfde wijze.
   
7. Het komt voor dat `::: vsa-notatie` vergeten wordt, of de afsluitende `:::`. De bouw

8. Color highlighting theme voor `::: vsa-notatie` voor vscode, inclusief aangeven van fouten. Vooral ook voorkomen dat teksten cursief worden weergegeven omdat we markdown-achtige symbolen gebruiken als `_` en `*`.

9.  Een manier verzinnen om, nadat AI een heleboel troparen en kondaken heeft geanalyseerd en dus zou moeten weten hoe de verschillende tonen daarbij werken, te komen tot een veel snellere manier om notaties in te voeren. Bijvoorbeeld door op zekere plekken een `|` neer te zetten die de scheidingen aangeeft tussen vsa-fragmenten, zodat de AI die dan kan omzetten in wat nodig is voor een gegeven tropaar, kondak, stichier of wat dan ook.