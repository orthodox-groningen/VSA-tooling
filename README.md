# Stap 61 - Markdown hardbreak newlines

Toon 8 gebruikt in de VSA-bron regels met twee spaties vóór newline:

```markdown
... {\ge_}.  
Drie ...
```

Binnen een `vsa-notatie` blok moeten die twee spaties niet als gewone inline
spacing blijven meetellen. Ze betekenen hier praktisch: einde bronregel.

Deze stap:

- normaliseert `  \r\n`, `  \n`, `  \r` naar gewone newline;
- stript trailing whitespace vóór harde bronregelgrenzen;
- voegt regressietests toe op toon-8-achtige bron.
