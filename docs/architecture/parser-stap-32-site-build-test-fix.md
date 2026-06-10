# Stap 32 - site build workflow testfix

De workflow was correct, maar de test was te letterlijk.

De werkende workflowregel is:

```bash
"${GITHUB_REF}" == "refs/heads/main"
```

De test zocht per ongeluk naar een variant zonder `}`.

De test controleert nu robuuster:

- `GITHUB_REF`;
- `refs/heads/main`;
- `target=production`;
- `target=preview`.
