# Quick start

Doel: snel controleren of de VSA-tool lokaal werkt.

## 1. Ga naar de repo-root

```cmd
cd /d C:\Git\orthodox-groningen\VSA-tooling
```

## 2. Installeer de lokale omgeving

```cmd
scripts\bootstrap.cmd
```

## 3. Controleer de installatie

```cmd
vsa --version
```

Verwachte vorm:

```text
vsa 0.1.0
```

## 4. Valideer een voorbeeld

```cmd
vsa validate examples\minimal\050_svg_demo.vsa
```

Bij succes:

```text
OK
```

## 5. Genereer een SVG

```cmd
vsa svg examples\minimal\050_svg_demo.vsa generated\vsa\050_svg_demo.svg
```

## 6. Controleer de hele keten

```cmd
scripts\ci.cmd
```

## Bronnen

Gebaseerd op:

- `docs/guides/user-guide.md`
- `docs/reference/cli.md`
