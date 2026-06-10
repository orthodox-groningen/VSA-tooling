# Scripts voor VSA Tooling

Deze map bevat eenvoudige scripts voor lokaal ontwikkelen en voor gebruik in GitHub Actions.

De scripts zijn bewust eenvoudig gehouden en gericht op Windows 11, CMD.exe en Python.

## Overzicht

| Script | Doel |
|---|---|
| `bootstrap.cmd` | virtuele omgeving maken en dependencies installeren |
| `test.cmd` | alle tests uitvoeren |
| `test-verbose.cmd` | tests uitvoeren met extra uitvoer |
| `clean.cmd` | tijdelijke build- en testbestanden verwijderen |
| `run-example.cmd` | voorbeeldbestand verwerken |
| `ci.cmd` | lokaal dezelfde stappen uitvoeren als CI |

## Aanbevolen workflow

Na clone:

```cmd
scripts\bootstrap.cmd
```

Tijdens ontwikkeling:

```cmd
scripts\test.cmd
```

Voor commit/push:

```cmd
scripts\ci.cmd
```

## GitHub Actions

GitHub Actions kan later exact dezelfde scripts gebruiken.
