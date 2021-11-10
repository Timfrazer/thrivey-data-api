#!/bin/sh

FUNC_NAME=hello_http

poetry export --without-hashes -f requirements.txt --output requirements.txt

gcloud auth activate-service-account $GOOGLE_CLOUD_USER_ACCOUNT --key-file=$GOOGLE_APPLICATION_CREDENTIALS

gcloud functions deploy --project $PROJECT_ID $FUNC_NAME --runtime python39 --trigger-http --allow-unauthenticated

gcloud functions describe $FUNC_NAME
