# Grammatica-referentie

Deze pagina bevat compacte EBNF-fragmenten voor [VSA](@).

## VSA-codeblok in Markdown

```ebnf
vsa-codeblok ::=
    "::: vsa-notatie"
    { newline parameter }
    newline
    zangstuk
    newline
    ":::" ;
```

## Metadata-parameter

```ebnf
parameter ::= bekende-parameter | vrije-parameter ;

bekende-parameter ::=
      do-parameter
    | mode-parameter
    | tempo-parameter
    | validate-ending-parameter
    | duration-model-parameter ;

vrije-parameter ::= identifier '="' parameter-waarde '"' ;
```

## Absolute toonhoogte

```ebnf
absolute-toonhoogte ::= toonnaam [ alteratie ] octaaf ;
toonnaam ::= "A" | "B" | "C" | "D" | "E" | "F" | "G" ;
alteratie ::= "#" | "♯" | "b" | "♭" ;
octaaf ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" ;
```

## Bracket tokens

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

## Toonhoogte-markering

`height-marker` in het bracket-token-schema stemt overeen met
[toonhoogte-markering](@) in de normatieve EBNF (`docs/specification/syntax.md`).

Voorbeelden:

| Voorbeeld | Betekenis             |
| --------- | --------------------- |
| `[:]`     | Neutrale hoogte       |
| `[/:]`    | Hoogtebeweging `/`    |
| `[//:]`   | Hoogtebeweging `//`   |
| `[\:]`    | Hoogtebeweging `\`    |

## Frontmatter in `.vsa`

```yaml
---
muziek:
  do: F4
  mode: major
  tempo: 132
identificatie:
  title: Tropaar van de zondag, toon 1
  composer: Traditioneel
  language: nl
---
[:] Ter{/&/wijl_&_} {\\de} steen ...
```

## Status

Deze grammatica is referentieel. De normatieve specificatie staat in `docs/specification/`.
