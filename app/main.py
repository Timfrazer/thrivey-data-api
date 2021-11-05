from typing import List
from decouple import config
from fastapi import FastAPI, HTTPException
import uvicorn

from app.models.UserBehaviour import User, Behaviour, UserBehaviour, UserBehaviourTable
from app.db.connection import get_db, init_engine
from app.db.model import user_behaviour_table_model, user_table_model, behaviour_table_model
from app.utils.data_shuffle import restructure_tbl_data

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

# Init FastAPI
app = FastAPI()

# Define routes
@app.get("/")
async def root():
    return {"Thrivey": "OK"}

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/user/table", response_model=List[User])
async def read_user():
    query = user_tbl.select()
    return await database.fetch_all(query)
@app.post("/user/validate")
async def validate_behaviour(data: User):
    print(f"Type: {type(data)} \n{data}")
    resp = {"model": User.schema()['title'], "isValid": True}
    return resp


@app.get("/behaviour/table", response_model=List[Behaviour])
async def read_behaviour():
    query = behaviour_tbl.select()
    return await database.fetch_all(query)
@app.post("/behaviour/validate")
async def validate_behaviour(data: Behaviour):
    print(f"Type: {type(data)} \n{data}")
    resp = {"model": Behaviour.schema()['title'], "isValid": True}
    return resp


@app.get("/user_behaviour/table", response_model=List[UserBehaviourTable])
async def read_user_behaviour():
    query = user_behaviour_tbl.select()
    return await database.fetch_all(query)

@app.get("/user_behaviour/json", response_model=List[UserBehaviour])
async def read_user_behaviour_json():
    result = await restructure_tbl_data(database, user_behaviour_tbl)
    print(result)
    return result

@app.post("/user_behaviour/validate")
async def validate_user_behaviour(data: UserBehaviour):
    print(f"Type: {type(data)} \n{data}")
    resp = {"model": UserBehaviour.schema()['title'], "isValid": True}
    return resp


def run_server():
    uvicorn.run(app, host='0.0.0.0', port=API_PORT, workers=API_WORKER_COUNT)


