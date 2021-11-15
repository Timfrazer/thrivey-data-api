#!/bin/sh

set -e
source .env

echo "Deploying cloud build:\ngcloud builds submit --config=cloudbuild.yaml --substitutions=_FUNC_NAME=$FUNC_NAME"
gcloud builds submit --config=cloudbuild.yaml --substitutions=_FUNC_NAME=$FUNC_NAME