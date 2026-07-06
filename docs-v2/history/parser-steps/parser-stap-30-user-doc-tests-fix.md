# Stap 30 - user docs testfix

De vorige testset was te broos.

Voorbeeld:

```python
assert "generated\\\\static\\\\vsa" in text
```

De documentatie gebruikt terecht normale Windowspaden:

```text
generated\static\vsa
```

Daarom zijn de tests aangepast.

De nieuwe tests controleren op inhoudelijke bruikbaarheid:

- kerncommando's aanwezig;
- validatiechecks uitgelegd;
- succes- en foutoutput beschreven;
- vervolgactie na fouten beschreven;
- AST-output uitgelegd;
- `--json` output uitgelegd;
- `<assets-dir>` en `assets-url-prefix` uitgelegd;
- defaults en diagnosevolgorde aanwezig.

De documentatiebestanden zelf worden in deze patch niet gewijzigd.
