# Stap 92 - parsercontract voor meerdere hoogte-markeringen

## Doel

Dit document legt vast wat de parser moet accepteren en afwijzen wanneer meerdere hoogte-markeringen worden ondersteund.

De vorm van een hoogte-markering blijft:

```text
[<EHM>:]
```

Een hoogte-markering bevat dus:

- een openingshaak `[`;
- een geldige EHM;
- een dubbele punt `:`;
- een sluithaak `]`.

## Geldige voorbeelden

### Eén marker aan het begin

```text
[:] Heer, ontferm U.
```

### Tekst vóór de eerste marker

```text
Heer, [:] ontferm U.
```

### Tekst na de laatste marker

```text
[:] Heer, ontferm U.
```

### Meerdere markers in één regel

```text
[//:] {\Heer}, [\:] ontferm {/U}.
```

### Meerdere markers met tekst ervoor, ertussen en erna

```text
Heer, [:] {\ont}ferm [\:] {/U}.
```

### Meerdere markerniveaus

```text
[:] {//eerst} test 1 [//:] {\\en} dan tekst {\twee} [\:] en dan {/tekst} drie [-:]
```

## Ongeldige voorbeelden

Ongeldige voorbeelden zouden in de toekomst nodig kunnen zijn voor uitbreidingen.
Daarom moet het mogelijk zijn om te kiezen of tekst tussen `[` en `:]` een harde fout moet
opleveren, of een waarschuwing (die dan wel gelogd moet worden op een toepasselijk niveau).

### `&` in een hoogte-markering

```text
[/&\:] fout
```

Reden: `&` is geen EHM-teken. Bovendien is `/&\` geen EHM, maar een samengestelde hoogte-modifier.

### Lengtemodifier in een hoogte-markering

```text
[_:] fout
```

Reden: `_` is een ELM, geen EHM.

### Marker zonder dubbele punt

```text
[/] fout
```

Reden: een hoogte-markering vereist `:` vóór `]`.
Feitelijk is dit geen marker, omdat hij niet eindigt op `:]`. 
Er moet gekozen kunnen worden of dit toch een harde fout oplevert,
of een waarschuwing (die op een toepasselijk niveau wordt gelogd).

### Marker met spatie vóór dubbele punt

```text
[/ :] fout
```

Reden: de marker moet exact `[<EHM>:]` volgen; er mogen dus geen spaties in zitten.

## AST-contract

De AST moet niet uitgaan van maximaal één pitch marker per blok.

Een VSA-blok bevat een geordende tokenstroom.

Pitch markers blijven gewone tokens in die stroom, met minimaal:

```text
type = pitch_marker
ehm = <EHM>
position = tokenpositie of bronpositie
```

De eerste pitch marker krijgt geen ander tokentype dan latere pitch markers.

Het onderscheid tussen beginhoogte en latere doelhoogtes is semantisch, niet syntactisch.

## Validator-contract

De validator mag niet meer eisen:

```text
exact één pitch marker per blok
```

De validator mag ook niet eisen:

```text
eerste token is pitch marker
```

Wel blijft ongeldig:

```text
ongeldige EHM in pitch marker
ongeldige bracketconstructie
```

## Renderer-contract

De renderer ontvangt pitch markers in volgorde.

Alle pitch markers worden met dezelfde glyph- en plaatsingsregels gerenderd.

De renderer mag niet afhankelijk zijn van "eerste marker heeft ander tokentype".
