# VSA-commentaar

Binnen een `::: vsa-notatie` blok mag HTML-commentaar voorkomen:

```text
<!-- dit is commentaar -->
```

## Regels

- De oorspronkelijke brontekst blijft ongewijzigd.
- Commentaar blijft behouden in de bron.
- Commentaar is uitsluitend bedoeld voor de broncode.
- Commentaar heeft geen invloed op parsing.
- Commentaar heeft geen invloed op validatie.
- Commentaar heeft geen invloed op rendering.
- Commentaar heeft geen invloed op afgeleide artefacten.
- Commentaar mag niet als tekstnode worden behandeld.
- Commentaar mag niet als whitespace worden behandeld.
- Commentaar mag niet als newline worden behandeld.
- Commentaar mag geen invloed hebben op positionering, spacing of layout.
- Commentaar mag niet in SVG, HTML, JSON, MusicXML of andere afgeleide artefacten terechtkomen.
