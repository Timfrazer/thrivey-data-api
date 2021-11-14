#!/bin/sh

set -e
source .env


docker build --progress plain -t us.gcr.io/$PROJECT_ID/$FUNC_NAME .
