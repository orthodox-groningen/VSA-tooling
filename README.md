# VSA stap 9 - map verwerken

Deze stap breidt `vsa process` uit.

Voorheen:

```cmd
vsa process bestand.md uitvoermap
```

Nu ook:

```cmd
vsa process content generated\vsa
```

Het commando:

- accepteert een bestand of map;
- zoekt recursief naar `.md` en `.markdown`;
- verwerkt alle VSA-blokken;
- schrijft SVG-bestanden naar één uitvoermap;
- gebruikt veilige bestandsnamen met padprefix.

Dit is nuttig voor Hugo:

```text
content/
  ↓
vsa process content generated\vsa
  ↓
hugo build
```
