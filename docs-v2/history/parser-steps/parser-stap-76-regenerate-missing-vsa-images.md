# Stap 76 - ontbrekende VSA SVG's regenereren

## Aanleiding

Na het verplaatsen van `praktijk` naar een hoger niveau verwijst HTML naar nieuwe SVG-namen:

```text
/vsa/praktijk-weekdagen-woensdag-block-1.svg
```

terwijl de SVG-map nog oude namen kan bevatten:

```text
/vsa/voorbeelden-praktijk-weekdagen-woensdag-block-1.svg
```

Of er is nog helemaal geen SVG gegenereerd voor een nieuwe pagina.

## Script

```cmd
python scripts\regenerate-missing-vsa-images.py
```

Het script:

1. scant gegenereerde HTML in `public`;
2. zoekt ontbrekende VSA image refs;
3. zoekt de corresponderende markdown in `content-source`;
4. rendert het gevraagde VSA-blok opnieuw;
5. schrijft de ontbrekende SVG naar `public\vsa`.

## Tijdelijk karakter

Dit is een veilige herstelstap na herstructurering.
Later moet de primaire buildpipeline zelf direct de correcte namen genereren.
