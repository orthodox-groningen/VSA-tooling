# Stap 31 - voorbeeldvalidatie en CLI-demo pagina's

Deze stap voegt kwaliteitscontrole toe voor voorbeelden.

## Goede voorbeelden

Deze moeten valideren:

```text
examples/hugo-demo/content-source
examples/minimal
examples/site-demo
```

## Verwachte foute voorbeelden

Deze moeten juist falen:

```text
examples/expected-fail/*.vsa
```

## CLI-demopagina's

Per belangrijk commando is er nu een pagina onder:

```text
/voorbeelden/cli/
```

Elke pagina toont:

- doel;
- input;
- commando;
- verwachte output;
- uitleg of foutafhandeling.

Daarmee wordt de demo-site zelf een praktische gebruikershandleiding.
