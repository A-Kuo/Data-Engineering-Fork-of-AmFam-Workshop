# Contributing

Suggestions, corrections, and extensions are welcome.

## Running notebooks

```bash
uv sync          # install all dependencies
make kernel      # register the kernel in VS Code / Cursor (optional)
```

Or open any notebook directly in Google Colab via the badge at the top of each file.

## Adding a notebook

1. Place it in the appropriate folder (`foundations/`, `explorations/`, or `playground/`).
2. Add a Colab badge as the **first markdown cell** (copy the pattern from any existing notebook).
3. Add a row to the **Notebooks at a Glance** table in `README.md`.
4. Update `CLAUDE.md` if the notebook introduces new data dependencies or changes the run order.

## Style conventions

- **Filename:** `lowercase_with_underscores_demo.ipynb`
- **First cell:** Colab badge
- **Second cell:** markdown with notebook title, purpose statement, and what you learn
- **Paths:** relative to repo root (e.g., `../synthetic_data/...` from `explorations/`)
- **Data:** synthetic or public-domain only — no real policy or claims data

## Validation

```bash
make check   # validates all notebook JSON and Python syntax
```

The same checks run automatically on every push via GitHub Actions.

## Reporting issues

Open a GitHub issue describing the problem and which notebook it appears in.
