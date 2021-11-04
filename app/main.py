from typing import Optional, List

from fastapi import FastAPI
from models.UserBehaviour import UserBehaviour, UserBehaviourTable

from db.connection import get_db
from db.model import user_behaviour_tbl
from sqlalchemy.sql import text

from utils.data_shuffle import restructure_tbl_data

database = get_db()
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "YURT"}

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

import uvicorn
uvicorn.run(app, host='0.0.0.0', port=8081, workers=1)


