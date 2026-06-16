# TODO lijst

1. Hoogte-controle bij laatste hoogte-marker

Het volgende is fout, maar wordt niet gedetecteerd

::: vsa-notatie
[//:] aap{/noot}{/mies}, [:]
:::

2. Bij de analyse over het gebruik van `+/` en `-\` gebruik maken van de 'zaligsprekingen', Liturgikon pp. 54-55;

3. Het moet mogelijk zijn om in kommentaarblokken (of regelcommentaar) ongeldige syntax of semantiek te beschrijven. Er moeten dus manieren komen om aan te geven wat blok-commentaar en wat regel-commentaar is.

4. Als de gebruiker de fontgrootte schaalt, moeten de onder- en boven-glyphgs meeschalen.

5. Er moet syntax en (renderings)semantiek komen die toelaat dat het beginakkoord (voor SATB) ook in SVGs terecht gaat komen.

6. Binnen `::: vsa-notatie ... :::` constructies mogen meerdere hoogte-markeringen voorkomen. De eerste geeft de beginhoogte aan. Elke volgende geeft de hoogte aan waar op die positie de zang moet 'zitten'. Er is geen voorschrift over de posities van zulke markeringen ten opzichte van de (gezongen) tekst: er mag dus best tekst staan voor de eerste hoogtemarkering, en ook na de laatste. Daartussen mogen ook hoogtemarkeringen worden gezet. De SVG rendering behandelt alle hoogtemarkeringen op dezelfde wijze.