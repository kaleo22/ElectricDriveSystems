#!/usr/bin/env bash
set -euo pipefail

# Ensure all contributors use the same pre-commit runtime in a local venv.
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if ! command -v python3 >/dev/null 2>&1; then
    echo "Error: python3 is required but was not found in PATH." >&2
    exit 1
fi

if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

VENV_PY="$ROOT_DIR/.venv/bin/python"
VENV_PRE_COMMIT="$ROOT_DIR/.venv/bin/pre-commit"

"$VENV_PY" -m pip install --upgrade pip
"$VENV_PY" -m pip install --upgrade -r requirements-dev.txt

"$VENV_PRE_COMMIT" install
"$VENV_PRE_COMMIT" install-hooks

cat <<'EOF'
Pre-commit is ready.

Useful commands:
  .venv/bin/pre-commit run --all-files
  .venv/bin/pre-commit autoupdate
EOF
