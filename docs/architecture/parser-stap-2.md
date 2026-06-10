# Parser stap 2

Deze stap introduceert:

- tokenization;
- diagnostics;
- syntax-validatie;
- regel/kolom-registratie.

## Belangrijk doel

Fouten netjes kunnen rapporteren.

Voorbeeld:

```text
{tekst
```

moet kunnen leiden tot:

```json
{
  "code": "VSA-SYNTAX-UNCLOSED-SCOPE",
  "line": 1,
  "column": 1
}
```

## Waarom belangrijk

Dit wordt later gebruikt voor:

- Hugo build errors;
- GitHub Actions feedback;
- editor-integratie;
- semantische validatie.
