# Stap 45 - prefix modifier and line offset fix

Deze patch herstelt twee regressies.

## Prefix-modifiers

Dit blijft syntactisch geldig:

```text
{/&\tekst_}
```

Het kan daarna semantisch falen met:

```text
VSA-SEMANTIC-MODIFIER-COUNT-MISMATCH
```

## Echte syntaxfouten

```text
{\\}
{&\ken__}
{fout/}
```

krijgen specifieke syntaxmeldingen.

## Markdown line offset

Foutmeldingen binnen `::: vsa-notatie` blokken wijzen weer naar de juiste
regel in het Markdownbestand.
