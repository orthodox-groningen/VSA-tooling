---
title: "CLI demo's"
---

# CLI demo's

- [Home](../../)
- [Vorige: Markdown](../markdown/)
- [Volgende: Rendering](../rendering/)

Deze sectie laat per `vsa`-commando zien hoe je het gebruikt.

## Commando's

| Pagina | Doel |
|--------|------|
| [`vsa validate`](validate/) | controleren of VSA klopt |
| [`vsa svg`](svg/) | SVG maken uit VSA |
| [`vsa blocks`](blocks/) | VSA-blokken in Markdown inspecteren |
| [`vsa parse`](parse/) | AST/debugstructuur bekijken |
| [`vsa process`](process/) | SVG's maken uit Markdown |
| [`vsa build-markdown`](build-markdown/) | Hugo Markdown + SVG bouwen |
| [`vsa --version`](version/) | versie tonen |
| [`--config`](config/) | configuratie en severity-overrides gebruiken |

## Snelle sanity check

```cmd
vsa validate examples\hugo-demo\content-source
```

Verwachte output:

```text
OK
```

## Config gebruiken

```cmd
vsa validate bestand.vsa --config vsa.toml
```
