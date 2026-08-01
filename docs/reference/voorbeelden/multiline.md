# Multiline

Langere VSA-regel die de renderer over meerdere regels kan zetten.

## Invoer

```text
[:] {/Hei_}{/lig_} is de Heer en Hij is heilig en wonderbaar in al Zijn werken. [//:]
```

## Commando

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
vsa svg examples\minimal\100_multiline_demo.vsa generated\docs-demo-multiline.svg --max-line-width 400
```

## Uitleg

Met `--max-line-width` breekt de renderer af als een regel te breed wordt voor
de gekozen breedte (pixels).
