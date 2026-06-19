# Stap 92 - parsercontract voor meerdere hoogte-markeringen

## Doel

Dit document legt vast wat de parser moet accepteren en afwijzen wanneer meerdere hoogte-markeringen worden ondersteund.

## Bracket-directive model

Een constructie tussen `[` en `:]` wordt gezien als een bracket-directive.

Het einde van zo'n directive is het samengestelde eindtoken:

```text
:]
```

Dus de parser behandelt dit niet als twee losse tekens:

```text
:
]
```

Dit maakt later andere directive-vormen tussen `[` en `:]` mogelijk.

## Hoogte-markering

Een hoogte-markering is een specifieke bracket-directive met deze vorm:

```text
[<EHM>:]
```

Daarbij is `<EHM>` een geldige EHM volgens de EHM-specificatie.

Voorbeelden:

```text
[:]
[/:]
[//:]
[\:]
[-:]
```

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

## Ongeldige of nog niet ondersteunde voorbeelden

### `&` in een hoogte-markering

```text
[/&\:] fout
```

Reden: `&` is geen EHM-teken. Bovendien is `/&\` geen EHM, maar een samengestelde hoogte-modifier.

### Lengtemodifier in een hoogte-markering

```text
[_:] fout
```

Reden: `_` is geen EHM (dat het wel een ELM is doet niet terzake).

### non-EHM modifiers in een hoogte-markering

```text
[//\:] fout
```

Reden: `//\` is geen EHM (het doet er niet toe dat alle karakters in een EHM kunnen voorkomen).

### Geen bracket-directive omdat het eindtoken ontbreekt

```text
[/] fout of waarschuwing
```

Reden: deze constructie eindigt niet op `:]` en is daarom geen hoogte-markering.

Er moet gekozen kunnen worden of dit een harde fout oplevert of een waarschuwing die op een toepasselijk niveau wordt gelogd.

### Marker met spatie vóór het eindtoken

```text
[/ :] fout
```

Reden: `/ ` is geen EHM; er mogen geen spaties in zitten.

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

Het onderscheid tussen eerste hoogte-markering en latere hoogte-markeringen is semantisch, niet syntactisch.

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
ongeldige bracket-directive
```

## Renderer-contract

De renderer ontvangt pitch markers in volgorde.

Alle pitch markers worden met dezelfde glyph- en plaatsingsregels gerenderd.

De renderer mag niet afhankelijk zijn van "eerste marker heeft ander tokentype".
