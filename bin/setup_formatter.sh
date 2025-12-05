#!/bin/bash

echo "Setting up Python code formatter..."

pip install black isort ruff

echo ""
echo "✓ Formatter setup complete!"
echo ""
echo "Usage:"
echo "  bash format.sh          # Format all Python files"
echo "  bash format.sh file.py  # Format specific file"
