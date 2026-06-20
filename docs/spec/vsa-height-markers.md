# VSA hoogte-markeringen

Status: ontwerpbesluit voor opname in de VSA-specificatie.

## 1. Begrip

Een hoogte-markering is een positionele markering in een `vsa-notatie`blok.

Voorbeelden:

```vsa
[:]
[/:]
[//:]
[\:]
```

De exacte syntaxis van de markering wordt door de VSA-taalspecificatie bepaald.

## 2. Aantal markeringen

Binnen één `vsa-notatie`blok mogen meerdere hoogte-markeringen voorkomen.

Voorbeeld:

```vsa
::: vsa-notatie
[:] Heer, ontferm U [/:] over ons [\:]
:::
```

Dit is syntactisch geldig.

## 3. Positie ten opzichte van tekst

Er is geen syntactisch voorschrift over de positie van hoogte-markeringen ten opzichte van gezongen tekst.

Daarom zijn onder meer geldig:

```vsa
::: vsa-notatie
[:] Heer, ontferm U
:::
```

```vsa
::: vsa-notatie
Heer, ontferm U [:]
:::
```

```vsa
::: vsa-notatie
Heer, [:] ontferm U
:::
```

```vsa
::: vsa-notatie
Heer, [:] ontferm [/:] U [\:]
:::
```

Tekst mag dus voorkomen:

- vóór de eerste hoogte-markering;
- tussen hoogte-markeringen;
- na de laatste hoogte-markering.

## 4. Semantiek

De eerste hoogte-markering in een `vsa-notatie`blok geeft de beginhoogte aan.

Elke latere hoogte-markering geeft de zanghoogte aan waar de zang op die positie moet zitten.

Hoogte-markeringen zijn daarmee gewone positionele semantische nodes in de documentstroom, met één aanvullende regel:

```text
eerste hoogte-markering = beginhoogte
latere hoogte-markering = lokale hoogte op die positie
```

## 5. Rendering

Voor SVG-rendering worden alle hoogte-markeringen op dezelfde manier behandeld.

De renderer maakt dus geen visueel onderscheid tussen:

- eerste hoogte-markering;
- latere hoogte-markeringen;
- eventueel laatste hoogte-markering.

Rendering is positioneel:

```text
hoogte-markering in bron → hoogte-marker-glyph op die renderpositie
```

## 6. Validatie

De validator mag semantische controles uitvoeren op hoogte-markeringen, maar mag niet eisen dat:

- de eerste hoogte-markering helemaal aan het begin staat;
- de laatste hoogte-markering helemaal aan het eind staat;
- er geen tekst vóór de eerste hoogte-markering staat;
- er geen tekst na de laatste hoogte-markering staat.

Wel kan de validator controleren:

- of hoogte-markeringen syntactisch geldig zijn;
- of de eerste markering als beginhoogte geïnterpreteerd kan worden;
- of latere markeringen betekenisvol zijn binnen de gekozen toon/semantiek;
- of een expliciete eindmarkering overeenkomt met de berekende eindtoon, zodra eindtooncontrole is gespecificeerd.

Een eindmarkering is optioneel. Het ontbreken van een eindmarkering is dus geen semantische fout.

Een eindmarkering `[:]` is niet leeg in semantische zin: zij betekent neutrale hoogte en is equivalent aan `[-:]` c.q. `[~:]`.

## 7. Implementatieconsequenties

### Parser

De parser moet hoogte-markeringen representeren als gewone nodes in de documentstroom.

Niet gewenst:

```text
Document(begin_marker, body, end_marker)
```

Wel gewenst:

```text
Document(nodes=[TextNode, HeightMarkerNode, ScopeNode, ...])
```

of equivalent.

### Validator

De validator moet hoogte-markeringen verzamelen uit de documentstroom.

Semantiek:

```text
height_markers = alle HeightMarkerNode nodes in bronvolgorde
start_height = height_markers[0] indien aanwezig
local_heights = height_markers[1:]
```

### SVG-renderer

De renderer behandelt elke hoogte-markering hetzelfde.

Daarom hoort rendering niet afhankelijk te zijn van:

- `is_start_marker`;
- `is_end_marker`;
- positie aan begin/eind.

### MusicXML

Voor toekomstige MusicXML-export is waarschijnlijk vooral de eerste hoogte-markering relevant als startinformatie.

Latere hoogte-markeringen kunnen later worden gebruikt voor:

- controlepunten;
- pitch hints;
- alignment;
- maat-/regelstructuur;
- melodische validatie.
