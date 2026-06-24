# Stap 133 - veilige SVG-comments

## Probleem

SVG-output bevatte metadata-comments zoals:

```xml
<!-- plain-text: ... -->
```

Wanneer de brontekst zelf een Markdown/HTML-comment bevatte, kon de geëscapete tekst nog steeds `--` bevatten.

XML/SVG-comments mogen geen dubbele hyphen bevatten.

Voorbeeld van foutmelding in de browser:

```text
Double hyphen within comment
```

## Oplossing

`SVGRenderer` gebruikt voortaan:

```python
_safe_xml_comment_text(value)
```

Deze helper:

- escaped XML-gevoelige tekens;
- vervangt `--` door `- -`;
- voorkomt dat commentaartekst eindigt op `-`.

## Gedrag

Alleen SVG-metadata-comments worden aangepast.

De zichtbare rendering verandert niet.
