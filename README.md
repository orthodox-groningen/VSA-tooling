# VSA CI pytest fix

Deze patch maakt `scripts\\ci.cmd` robuuster.

Probleem op GitHub Actions:

```text
No module named pytest
```

Fix:

- `ci.cmd` installeert eerst het project en pytest;
- daarna pas tests draaien;
- lokaal blijft het ook werken.
