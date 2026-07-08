# Parser stap 3 fix

De parser kiest nu expliciet:

```text
[hoogte-modifier] + zangelement + [lengte-modifier]
```

Daarbij probeert hij geldige prefix- en suffix-modifiers te vinden en blijft het middelste deel het zangelement.

Voorbeeld:

```text
{/&\&/tekst_&~&~}
```

wordt:

```text
height_modifier = ["/", "\", "/"]
text            = "tekst"
length_modifier = ["_", "~", "~"]
```
