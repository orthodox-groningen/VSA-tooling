# VSA stap 32 - site build workflow testfix

Deze patch wijzigt alleen de test.

Probleem:

De workflow bevat correct:

```bash
"${GITHUB_REF}" == "refs/heads/main"
```

maar de test zocht naar:

```text
GITHUB_REF" == "refs/heads/main"
```

Dat mist de sluitende `}`.

Fix:

- test zoekt nu inhoudelijk naar `GITHUB_REF`;
- test zoekt naar `refs/heads/main`;
- test zoekt naar `target=production` en `target=preview`.
