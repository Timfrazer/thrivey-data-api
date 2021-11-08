from fastapi_crudrouter import DatabasesCRUDRouter
from typing import List


from app.models.UserBehaviour import UserBehaviour, UserBehaviourTable
from app.utils.data_shuffle import restructure_tbl_data

from app.main import (
    UserBehaviour,
    user_behaviour_tbl,
    database,
)

user_behaviour_router = DatabasesCRUDRouter(
    schema=UserBehaviour,
    create_schema=UserBehaviour,
    table=user_behaviour_tbl,
    database=database
)


@user_behaviour_router.get("/user_behaviour/table", response_model=List[UserBehaviourTable])
async def read_user_behaviour():
    query = user_behaviour_tbl.select()
    return await database.fetch_all(query)

@user_behaviour_router.get("/user_behaviour/json", response_model=List[UserBehaviour])
async def read_user_behaviour_json():
    result = await restructure_tbl_data(database, user_behaviour_tbl)
    print(result)
    return result

@user_behaviour_router.post("/user_behaviour/validate")
async def validate_user_behaviour(data: UserBehaviour):
    print(f"Type: {type(data)} \n{data}")
    resp = {"model": UserBehaviour.schema()['title'], "isValid": True}
    return resp