#!/bin/bash

TARGET="${1:-.}"

echo "Formatting Python code in $TARGET..."
black "$TARGET"
isort "$TARGET"

echo "✓ Formatting complete!"
