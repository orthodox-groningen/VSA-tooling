# VSA stap 30 - demo quality fix

Deze patch herstelt twee demo-site problemen.

## 1. Dubbele titels

De templates voegden automatisch `<h1>{{ .Title }}</h1>` toe, terwijl de Markdownpagina's zelf ook al een `# Titel` bevatten.

Fix:

- `single.html` toont alleen `.Content`;
- `list.html` toont alleen `.Content`;
- `home.html` toont alleen `.Content` plus paginaoverzicht.

## 2. Ongeldig multiline voorbeeld

Het multiline voorbeeld had:

```text
[:] ... [:]
```

maar de afsluiting moet zijn:

```text
[\\:]
```

Fix:

```text
[:] {/Hei_}{/lig_} is de Heer en Hij is heilig en wonderbaar in al Zijn werken. [\\:]
```

Ook toegevoegd:

- tests die controleren dat demo-content valideert;
- test die controleert dat het multiline voorbeeld de correcte afsluitende pitch-marker bevat.
