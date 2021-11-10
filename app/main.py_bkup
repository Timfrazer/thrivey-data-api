from typing import List
from decouple import config
from fastapi import FastAPI, HTTPException
import uvicorn

from app.models.UserBehaviour import User, Behaviour, UserBehaviour, UserBehaviourTable
from app.db.connection import get_db, init_engine
from app.db.model import user_behaviour_table_model, user_behaviour_json_model, user_table_model, behaviour_table_model
# from app.db import bq_connector


# Conf
DEFAULT_SQLITE_DB='sqlite:///data/thrivey.db'
SQLALCHEMY_DATABASE_URL = config("DATABASE_URL", DEFAULT_SQLITE_DB)
API_PORT=config("API_PORT", 8000)
API_WORKER_COUNT=config("API_WORKER_COUNT", 1)

# Init DB Conn
db_metadata = init_engine(SQLALCHEMY_DATABASE_URL)
database = get_db(SQLALCHEMY_DATABASE_URL)
user_tbl=user_table_model(db_metadata)
behaviour_tbl=behaviour_table_model(db_metadata)
user_behaviour_tbl=user_behaviour_table_model(db_metadata)
user_behaviour_json=user_behaviour_json_model(db_metadata)

# Init FastAPI
api = FastAPI()

# Define default routes
@api.get("/")
async def root():
    return {"Thrivey": "OK"}

# @api.get("/bq")
# async def bigquery_select_count():
#     result = bq_connector.fire_bq()
#     return result

# Init DB conn on startup
@api.on_event("startup")
async def startup():
    await database.connect()

# Shutdown DB conn on startup
@api.on_event("shutdown")
async def shutdown():
    await database.disconnect()

def run_server():
    uvicorn.run(api, host='0.0.0.0', port=API_PORT, workers=API_WORKER_COUNT)

# Import & init routers
from app.routes.user_behaviour_json import user_behaviour_json_router
api.include_router(user_behaviour_json_router)

# from app.routes.user_behaviour import user_behaviour_router, user_behaviour_json_router
# from app.routes.user import user_router
# from app.routes.behaviour import behaviour_router
# api.include_router(user_behaviour_router)
# api.include_router(user_router)
# api.include_router(behaviour_router)


# from flask import escape

def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return 'Hello {}!'.format((name))

