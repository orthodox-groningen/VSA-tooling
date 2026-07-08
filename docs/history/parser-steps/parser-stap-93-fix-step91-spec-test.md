# Stap 93 - fix stap 91 specificatietest

## Probleem

De test `test_step91_spec_has_no_invalid_ampersand_example_as_valid_example` selecteerde tekst vanaf:

```text
Voorbeelden van geldige hoogte-markeringen:
```

tot:

```text
## Positie
```

Daardoor viel ook de sectie met ongeldige voorbeelden binnen de testselectie.

## Oplossing

De testselectie eindigt nu bij:

```text
Voorbeelden van ongeldige hoogte-markeringen:
```

Daarnaast is expliciet getest dat `[/&:]` juist wel in de ongeldige sectie staat.
