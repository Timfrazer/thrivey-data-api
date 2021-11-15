# cat data/user_behaviour.json | jq | xargs -I {} gcloud functions call $FUNC_NAME --data "{}"
gcloud functions call $FUNC_NAME --data "{}"

echo "Authorization: Bearer $(gcloud config config-helper --format 'value(credential.id_token)')" 
curl -H "Authorization: Bearer $(gcloud config config-helper --format 'value(credential.id_token)')" https://us-central1-sandbox-278017.cloudfunctions.net/$FUNC_NAME/