from typing import List

import uvicorn
from decouple import config
from fastapi import FastAPI, HTTPException

from app.db.connection import get_db, init_engine
from app.db.model import (behaviour_table_model, user_behaviour_json_model,
                          user_behaviour_table_model, user_table_model)
from app.models.UserBehaviour import (Behaviour, User, UserBehaviour,
                                      UserBehaviourTable)

# from app.db import bq_connector


# Conf
DEFAULT_SQLITE_DB = "sqlite://"
SQLALCHEMY_DATABASE_URL = config("DATABASE_URL", DEFAULT_SQLITE_DB)
API_PORT = config("API_PORT", 8000)
API_WORKER_COUNT = config("API_WORKER_COUNT", 1)

# Init DB Conn
db_metadata = init_engine(SQLALCHEMY_DATABASE_URL)
database = get_db(SQLALCHEMY_DATABASE_URL)
user_tbl = user_table_model(db_metadata)
behaviour_tbl = behaviour_table_model(db_metadata)
user_behaviour_tbl = user_behaviour_table_model(db_metadata)
user_behaviour_json = user_behaviour_json_model(db_metadata)

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
    uvicorn.run(api, host="0.0.0.0", port=API_PORT, workers=API_WORKER_COUNT)


# Import & init routers
from app.routes.user_behaviour_json import user_behaviour_json_router

api.include_router(user_behaviour_json_router)
