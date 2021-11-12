# cat data/user_behaviour.json | jq | xargs -I {} gcloud functions call $FUNC_NAME --data "{}"
gcloud functions call $FUNC_NAME --data "{}"
