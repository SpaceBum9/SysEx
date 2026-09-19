#!/bin/sh
set -e
root=$(git rev-parse --show-toplevel)
mkdir -p "$root/.git/hooks"
cp "$root/hooks/pre-commit" "$root/.git/hooks/pre-commit"
chmod +x "$root/.git/hooks/pre-commit"
echo "installed $root/.git/hooks/pre-commit"
