# VSA stap 10 - process valideert vóór SVG-generatie

Deze stap maakt `vsa process` veiliger.

Voorheen:

```text
process
  ↓
SVG genereren
```

Nu:

```text
process
  ↓
validate
  ↓
alleen bij OK: SVG genereren
```

Bij fouten:

- worden foutmeldingen getoond;
- wordt er geen SVG gegenereerd;
- eindigt het commando met exitcode `1`.

Dit is belangrijk voor:

- lokale controle;
- Hugo-builds;
- GitHub Actions.
