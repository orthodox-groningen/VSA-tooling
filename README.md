# VSA stap 18 - SVG regelbreedte instelbaar maken

Deze stap maakt de maximale SVG-regelbreedte instelbaar via de CLI.

Nieuw:

```cmd
vsa svg input.vsa output.svg --max-line-width 600
vsa process input.md output-dir --max-line-width 600
vsa build-markdown input-dir output-dir assets-dir --max-line-width 600
```

Waarom:

- smalle websitekolom: kleinere regelbreedte;
- brede desktopweergave: grotere regelbreedte;
- print/PDF: eventueel nog groter;
- layoutgedrag wordt reproduceerbaar testbaar.

Default blijft:

```text
800
```
