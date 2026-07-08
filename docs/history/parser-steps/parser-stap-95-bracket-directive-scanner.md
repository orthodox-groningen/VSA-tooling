# Stap 95 - bracket-directive scanner

## Doel

Eerst een kleine geïsoleerde parserbouwsteen toevoegen voordat de bestaande parser wordt aangepast.

Bestand:

```text
src/vsa/bracket_directive.py
```

## Contract

Een bracket-directive heeft vorm:

```text
[<body>:]
```

Het eindtoken is:

```text
:]
```

## Pitch marker

Een pitch marker is een bracket-directive waarvan `<body>` een geldige EHM is.

Voorbeelden:

```text
[:]
[/:]
[/\:]
[//:]
[\:]
[-:]
```

Voorbeelden die wel bracket-directives zijn maar geen pitch markers:

```text
[/&\:]
[_:]
```

## Integratie

Nog niet geïntegreerd in:

- lexer;
- bestaande parser;
- AST;
- validator;
- SVG-renderer.

Dat volgt in een latere stap.
