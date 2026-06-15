# TODO addendum stap 58

Voeg toe aan `docs/todo.md` als dit nog ontbreekt:

## Pipeline newline preservation

Status: `In uitvoering`

Fysieke VSA-bronregels moeten in de hele pipeline behouden blijven:

- Markdown block extraction;
- Hugo shortcode generatie;
- SVG rendering;
- CLI process/build routes.

Verboden voor VSA-source:

```python
" ".join(lines)
source.replace("\n", " ")
```

Toegestaan:

```python
"\n".join(lines)
source.replace("\r\n", "\n").replace("\r", "\n")
```
