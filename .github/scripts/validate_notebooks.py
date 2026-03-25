"""Validate all Jupyter notebooks: JSON integrity + Python syntax in code cells."""
import ast
import json
import sys
from pathlib import Path


def main() -> int:
    errors: list[str] = []
    notebooks = sorted(Path(".").rglob("*.ipynb"))

    for nb_path in notebooks:
        try:
            with open(nb_path) as f:
                nb = json.load(f)
            assert "cells" in nb, "missing 'cells' key"
            assert "metadata" in nb, "missing 'metadata' key"
        except Exception as e:
            errors.append(f"{nb_path}: {e}")
            continue

        for i, cell in enumerate(nb["cells"]):
            if cell.get("cell_type") != "code":
                continue
            src = "".join(cell.get("source", []))
            # Strip IPython magics and shell commands before parsing
            clean = "\n".join(
                ln for ln in src.splitlines()
                if not ln.strip().startswith(("%", "!"))
            )
            try:
                ast.parse(clean)
            except SyntaxError as e:
                errors.append(f"{nb_path} (cell {i}): {e}")

    if errors:
        print("Validation errors found:")
        for e in errors:
            print(f"  {e}")
        return 1

    print(f"All {len(notebooks)} notebook(s) passed validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
