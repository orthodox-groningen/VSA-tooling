# Stap 30 - Hugo home/section layout fix

Hugo had wel `single.html`, maar geen layouts voor:

```text
home
section
```

Daardoor werden wel pagina's zoals:

```text
/voorbeelden/basis/
```

gebouwd, maar niet:

```text
/
```

en niet:

```text
/voorbeelden/
```

Deze patch voegt toe:

```text
layouts/_default/home.html
layouts/_default/list.html
```
