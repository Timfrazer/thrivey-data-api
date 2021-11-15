#!/bin/sh

set -e
source .env

# Vars
MEM_MB=1024

poetry export --without-hashes -f requirements.txt --output requirements.txt
if [ -z ${USE_SERVICE_ACCOUNT+x} ]; 
    then echo "USE_SERVICE_ACCOUNT var is not set. Using currently logged in user"; 
else 
    gcloud auth activate-service-account $GOOGLE_CLOUD_USER_ACCOUNT --key-file=$GOOGLE_APPLICATION_CREDENTIALS
fi


exec_func="gcloud functions deploy --project ${PROJECT_ID} ${FUNC_NAME} --memory ${MEM_MB}MB --runtime python39 --trigger-http --allow-unauthenticated"
echo "$exec_func"
exec $($exec_func)
# gcloud functions deploy --project $PROJECT_ID $FUNC_NAME --runtime python39 --entry-point bin/run-api.sh --trigger-http --allow-unauthenticated

gcloud functions describe $FUNC_NAME
