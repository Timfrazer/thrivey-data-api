import logging
from fastapi_crudrouter import DatabasesCRUDRouter
from typing import List

from app.models.UserBehaviour import UserBehaviour, UserBehaviourTable
from app.utils.data_shuffle import restructure_tbl_data

from app.main import (
    user_behaviour_tbl,
    user_behaviour_json,
    database,
)

user_behaviour_router = DatabasesCRUDRouter(
    schema=UserBehaviourTable,
    table=user_behaviour_tbl,
    database=database,
)

logger = logging.getLogger()


@user_behaviour_router.get("/{id}", response_model=List[UserBehaviourTable])
async def read_user_behaviour():
    query = user_behaviour_tbl.select()
    return await database.fetch_all(query)

@user_behaviour_router.get("/", response_model=List[UserBehaviourTable])
async def read_user_behaviour():
    query = user_behaviour_tbl.select()
    return await database.fetch_all(query)

@user_behaviour_router.post("/validate")
async def validate_user_behaviour(data: UserBehaviour):
    logger.info(f"Type: {type(data)} \n{data}")
    resp = {"model": UserBehaviour.schema()['title'], "isValid": True}
    return resp