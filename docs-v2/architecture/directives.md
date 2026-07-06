# Directive-architectuur

## Doel

Bracket-directives worden via een generiek framework verwerkt, zodat nieuwe tokens later zonder parservervuiling kunnen worden toegevoegd.

## Categorieën

### Hoogtemarkers

```text
[:]
[/:]
[//:]
```

### Control tokens

```text
[*]
[/]
[*?]
[/?]
```

## Uitbreidingsrichting

Het model houdt rekening met toekomstige tokens zoals:

```text
[token]
[token:param]
[token:param:param]
```

## Ontwerpregel

Nieuwe bracketconstructies krijgen een eigen herkenning, AST-representatie en validatieregel. Ze worden niet als tekstuele voorbewerking opgelost.

## Traceerbaarheid

Gebaseerd op onder meer:

- `docs/architecture/parser-stap-115-directive-framework.md`
- `docs/architecture/parser-stap-116-control-token-registry.md`
- `docs/architecture/parser-stap-112-control-token-dispatch.md`
- `docs/architecture/parser-stap-113-control-token-semantics.md`
