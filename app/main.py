from typing import Optional, List
import databases

from fastapi import FastAPI
from db.connection import get_sesh
from models.UserBehaviour import UserBehaviour

from db.connection import get_db
from db.model import user_behaviour_tbl


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


@app.get("/user_behaviour/", response_model=List[UserBehaviour])
async def read_notes():
    query = user_behaviour_tbl.select()
    return await database.fetch_all(query)

import uvicorn
uvicorn.run(app, host='0.0.0.0', port=8081, workers=1)


