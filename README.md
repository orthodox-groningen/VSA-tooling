# VSA Tooling

VSA Tool is a standalone parser, validator, renderer, and exporter for the **Vereenvoudigde Slavische Accentnotatie (VSA)** specification.

The project is intended for:

- standalone command-line use on Windows;
- integration into static-site workflows such as Hugo;
- automated builds via GitHub Actions;
- future extensions such as interactive editors or alternative renderers.

The tool processes VSA notation blocks and converts them into validated internal structures, SVG renderings, and symbolic music formats such as MusicXML.

## Goals

- Formal parsing based on the VSA EBNF grammar
- Syntax and semantic validation
- SVG rendering
- MusicXML export
- Stable CLI interface
- Modular architecture
- Testability
- Extensibility

## Planned Features

### Core

- Lexer
- Parser
- AST generation
- Syntax validation
- Semantic validation

### Rendering

- SVG renderer
- HTML embedding support

### Export

- MusicXML export

### Tooling

- Command-line interface
- Hugo preprocessing support
- GitHub Actions integration

## Repository Structure

```text
vsa-tool/
│
├─ README.md
├─ LICENSE
├─ .gitignore
├─ pyproject.toml
│
├─ src/
│   └─ vsa/
│       ├─ parser.py
│       ├─ ast.py
│       ├─ validator.py
│       ├─ semantics.py
│       ├─ render_svg.py
│       ├─ export_musicxml.py
│       └─ cli.py
│
├─ tests/
│
├─ examples/
│
└─ docs/
```

## Development Environment

Recommended environment:

- Windows 11
- Python 3.12+
- CMD.exe or PowerShell
- Git

## Initial Setup

Clone the repository:

```cmd
git clone https://github.com/<your-account>/vsa-tool.git
cd vsa-tool
```

Create a virtual environment:

```cmd
python -m venv .venv
.venv\Scripts\activate
```

Install development dependencies:

```cmd
pip install -e .
```

## Planned CLI

Examples:

```cmd
vsa validate input.md
vsa render-svg input.md output.svg
vsa export-musicxml input.md output.musicxml
```

## Hugo Workflow

Recommended workflow:

```text
Markdown with VSA blocks
        ↓
vsa preprocessing/rendering
        ↓
generated SVG/HTML fragments
        ↓
Hugo build
```

The Hugo site should consume generated output rather than implement parsing logic itself.

## GitHub Actions

Example workflow:

```text
checkout
setup-python
install vsa-tool
run tests
render VSA assets
run hugo build
deploy
```

## Project Status

This repository currently targets:

- VSA specification version 1
- reference implementation phase

## License

See the LICENSE file.
