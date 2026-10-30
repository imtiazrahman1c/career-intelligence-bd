#!/usr/bin/env bash
set -euo pipefail
python3 -m unittest discover -s tests -v
node --check web/app.js
for test_file in tests/test_*.mjs; do
  node "$test_file"
done
