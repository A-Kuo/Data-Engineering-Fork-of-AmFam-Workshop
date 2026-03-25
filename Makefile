.DEFAULT_GOAL := help

.PHONY: help install kernel check clean

help: ## Show available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'

install: ## Install all dependencies via uv
	uv sync

kernel: ## Register the venv as a Jupyter kernel (for VS Code / Cursor)
	uv run python -m ipykernel install --user --name amfam-ai --display-name "AmFam AI (uv)"

check: ## Validate all notebooks (JSON integrity + Python syntax)
	uv run python .github/scripts/validate_notebooks.py

clean: ## Remove generated outputs and caches
	rm -rf outputs/eval_logs outputs/chroma_synthetic_policy __pycache__ .pytest_cache
