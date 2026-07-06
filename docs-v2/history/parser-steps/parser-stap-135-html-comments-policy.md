# Stap 135 - HTML-commentaar in VSA-notatie

## Doel

HTML-commentaar binnen VSA-notatie wordt broncommentaar.

## Policy

Commentaar van de vorm `<!-- ... -->` binnen VSA-notatie blijft in de oorspronkelijke bron staan, maar wordt genegeerd bij:

- parsing;
- syntaxvalidatie;
- semantische validatie;
- SVG-rendering;
- afgeleide artefacten.

## Implementatie

Nieuwe helper:

```text
src/vsa/vsa_comments.py
```

Deze helper wordt gebruikt vóór parsing en validatie.

SVG-rendering ontvangt daardoor geen commentaartekst en schrijft ook geen `plain-text` metadata-comments meer.
