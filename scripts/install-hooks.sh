#!/bin/sh
set -e
root=$(git rev-parse --show-toplevel)
cd "$root"
if command -v npm >/dev/null 2>&1; then
  npm install
  git config core.hooksPath .husky
  echo "husky hooksPath=.husky"
else
  mkdir -p "$root/.git/hooks"
  cp "$root/hooks/pre-commit" "$root/.git/hooks/pre-commit"
  chmod +x "$root/.git/hooks/pre-commit"
  echo "shell hook only"
fi
