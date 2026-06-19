# Stap 97 - repair bracket token stream

## Probleem

Stap 96 filterde tokens met lege `value` weg.

Dat is fout, want de pitch marker:

```text
[:]
```

heeft een lege EHM-body en is juist geldig.

## Oplossing

`bracket_token_stream()` retourneert nu alle tokens.

Lege teksttokens worden niet geproduceerd door de bestaande cursorlogica; lege pitch-marker bodies blijven behouden.

## Extra regressie

Toegevoegd:

```text
tests/test_step97_repair_bracket_token_stream.py
```
