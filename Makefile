.PHONY: help install run clean sync test

# Default target
help:
	@echo "Available targets:"
	@echo "  make install    - Install dependencies using uv"
	@echo "  make sync       - Sync dependencies with uv"
	@echo "  make run        - Run the sample application"
	@echo "  make clean      - Remove Python cache files"
	@echo "  make test       - Run the application (alias for run)"
	@echo "  make all        - Install dependencies and run the app"

# Install dependencies
install:
	uv sync

# Sync dependencies (alias for install)
sync:
	uv sync

# Run the application
run:
	uv run python main.py

# Run the application (alias)
test: run

# Run everything
all: install run

# Clean Python cache files
clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	@echo "Cleaned up Python cache files"
