# Directives en commentaar

Status: **geconsolideerde werkversie**.

## Scope

Dit document beschrijft bronconstructies die niet rechtstreeks gezongen tekst zijn.

## HTML-commentaar

Binnen een `::: vsa-notatie`blok mag HTML-commentaar voorkomen.

Regels:

- de oorspronkelijke brontekst blijft ongewijzigd;
- commentaar blijft behouden in de bron;
- commentaar is uitsluitend bedoeld voor de broncode;
- commentaar heeft geen invloed op parsing;
- commentaar heeft geen invloed op validatie;
- commentaar heeft geen invloed op rendering;
- commentaar heeft geen invloed op afgeleide artefacten;
- commentaar wordt niet als tekstnode behandeld;
- commentaar wordt niet als whitespace of newline behandeld;
- commentaar komt niet terecht in SVG, HTML, JSON, MusicXML of andere output.

## Include

Het include-mechanisme is bedoeld om VSA-bronmateriaal te hergebruiken.

Normatieve details worden in een latere fase geconsolideerd uit `docs/spec/include-vsa.md`.

## Bracket- en control-directives

Bracket- en control-directives worden als aparte bronelementen behandeld.

Parser en validator moeten deze constructies kunnen onderscheiden van gewone tekst, scopes en hoogte-markeringen.

## Open consolidatiepunt

De exacte dispatchregels voor wraptokens en control tokens worden nog geconsolideerd uit de parser-stapdocumenten.

Tot die consolidatie is dit document richtinggevend, maar nog niet volledig normatief.
