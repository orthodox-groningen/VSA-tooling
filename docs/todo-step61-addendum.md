# TODO addendum stap 61

Toevoegen aan `docs/todo.md`:

## Markdown hardbreaks in VSA-blokken

Status: `Afgerond`

Regel-eindes in `vsa-notatie` mogen Markdown-hardbreakspaties bevatten.
Die spaties zijn geen muzikale inhoud en worden vóór rendering gestript:

```markdown
regel 1··
regel 2
```

wordt voor VSA-rendering:

```text
regel 1
regel 2
```
