#!/bin/sh

if [ -z "$API_PORT"  ] && [ -z "$API_WORKER_COUNT" ];then
    API_PORT=8000
    API_WORKER_COUNT=2
fi

poetry run uvicorn --host=0.0.0.0 --port ${API_PORT} \
    --workers ${API_WORKER_COUNT} app.main:app