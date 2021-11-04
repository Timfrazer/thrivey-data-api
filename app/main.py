from typing import List
from decouple import config
from fastapi import FastAPI
import uvicorn

from models.UserBehaviour import UserBehaviour, UserBehaviourTable
from db.connection import get_db, init_engine
from db.model import user_behaviour_table_model
from utils.data_shuffle import restructure_tbl_data

# Conf
DEFAULT_SQLITE_DB='sqlite:///data/thrivey.db'
SQLALCHEMY_DATABASE_URL = config("DATABASE_URL", DEFAULT_SQLITE_DB)
API_PORT=config("API_PORT", 8081)
API_WORKER_COUNT=config("API_WORKER_COUNT", 1)

# Init DB Conn
db_metadata = init_engine(SQLALCHEMY_DATABASE_URL)
database = get_db(SQLALCHEMY_DATABASE_URL)
user_behaviour_tbl=user_behaviour_table_model(db_metadata)


# Init FastAPI
app = FastAPI()


# Define routes
@app.get("/")
async def root():
    return {"Thrivey": "Thrivey"}

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/user_behaviour/", response_model=List[UserBehaviourTable])
async def read_user_behaviour():
    query = user_behaviour_tbl.select()
    return await database.fetch_all(query)

@app.get("/user_behaviour_json/", response_model=List[UserBehaviour])
async def read_user_behaviour_json():
    result = await restructure_tbl_data(database, user_behaviour_tbl)
    print(result)
    return result

uvicorn.run(app, host='0.0.0.0', port=API_PORT, workers=API_WORKER_COUNT)


