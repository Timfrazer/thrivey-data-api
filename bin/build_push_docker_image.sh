#!/bin/sh

set -e
source .env

IMAGE_NAME="us.gcr.io/$PROJECT_ID/$FUNC_NAME:latest"

echo "Building docker image"
docker build --progress plain -t $IMAGE_NAME .
docker push $IMAGE_NAME
