
# Spec addendum – Control Tokens / Renderer Directives

## Doel

Maak onderscheid tussen:

1. gewone tekst
2. hoogte-markeringen
3. renderer-directives

## Hoogte-markering

```text
[<EHM>:]
```

Voorbeelden:

```text
[:]
[/:]
[//:]
[\:]
```

Deze hebben uitsluitend betrekking op toonhoogte.

## Control tokens

```text
[/]
[*]
[/?]
[*?]
```

Deze zijn geen hoogte-markeringen.

## Semantiek

Control tokens vertegenwoordigen een abstracte intentie.

| Token | Abstracte betekenis |
|---------|---------|
| [*] | phrase_rest |
| [/] | phrase_boundary |
| [*?] | optional_phrase_rest |
| [/?] | optional_phrase_boundary |

## Renderer-afhankelijk gedrag

### SVG

Mogelijke interpretaties:

- zichtbaar teken
- regelafbreking
- zachte regelafbreking
- negeren

volledig configureerbaar.

### MusicXML

Mogelijke interpretaties:

- breath mark
- barline
- system break
- negeren

volledig configureerbaar.

## EBNF

```ebnf
bracket-token ::=
      height-marker
    | control-token ;

height-marker ::= "[" [ EHM ] ":]" ;

control-token ::=
      "[/]"
    | "[*]"
    | "[/?]"
    | "[*?]" ;
```

## Ontwerpregel

Control tokens krijgen geen universele betekenis.

Renderers bepalen zelf hoe de abstracte betekenis wordt uitgewerkt.
