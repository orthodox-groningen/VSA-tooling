# Syntax

Status: **geconsolideerde werkversie**.

## Scope

Dit document beschrijft wat letterlijk in VSA-brontekst mag staan.

Semantische betekenis, validatie en rendering staan in aparte documenten.

## VSA-blok

Een VSA-zangstuk staat in een fenced blok:

```text
::: vsa-notatie
[:] {/Hei_}{/lig_} is de Heer. [:]
:::
```

Een blok kan metadata bevatten. Bekende metadata zijn onder andere:

| Parameter | Betekenis |
|---|---|
| `do` | absolute starttoon voor interpretatie en export |
| `mode` | modusdefinitie voor toonladderinterpretatie |
| `tempo` | tempo voor MusicXML-export |
| `validate-ending` | eindtooncontrole aan/uit |
| `duration-model` | mapping van lengte naar exportduur |

## Vrije tekst

Tekst buiten scopes blijft gewone gezongen of weergegeven tekst.

Tekst mag vóór, tussen en na hoogte-markeringen voorkomen.

## Scope

Een scope is een zangelement tussen accolades:

```text
{/Hei_}
```

Een scope bevat tekst en optioneel hoogte- en lengte-informatie.

## Hoogte-modifiers

Hoogte-modifiers staan bij de gezongen tekst en geven relatieve melodische beweging aan.

Voorbeelden:

```text
{/Hei}
{//lig}
{\Heer}
{+/U}
{-\ons}
```

Samengestelde hoogte-modifiers gebruiken `&`:

```text
{/&//Heer}
```

## Lengte-modifiers

Lengte-modifiers geven duur of verlenging aan.

Voorbeelden:

```text
{Heer_}
{Heer__}
{Heer.}
{Heer..}
{Heer~}
```

Samengestelde lengte-modifiers gebruiken eveneens `&`.

## Hoogte-markeringen

Hoogte-markeringen staan tussen rechte haken en eindigen met `:`.

Voorbeelden:

```text
[:]
[/:]
[//:]
[\:]
```

Binnen één `vsa-notatie`blok mogen meerdere hoogte-markeringen voorkomen.

Voorbeelden:

```text
[:] Heer, ontferm U
Heer, ontferm U [:]
Heer, [:] ontferm [/:] U [\:]
```

## Commentaar

Binnen een VSA-blok mag HTML-commentaar voorkomen:

```text
<!-- dit is commentaar -->
```

Commentaar blijft broninformatie en is geen VSA-tekst.

## Syntax versus semantiek

Syntax bepaalt of de brontekst grammaticaal herkenbaar is.

Semantiek bepaalt of die tekst muzikaal en positioneel betekenisvol is.
