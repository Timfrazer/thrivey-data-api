#!/bin/sh

STARTUP_DB_PY_SCRIPT="app/startup.py"

echo "Executing db prep script: ${STARTUP_DB_PY_SCRIPT}"
poetry run python ${STARTUP_DB_PY_SCRIPT}
