from typing import List
from fastapi import APIRouter

from app.models.UserBehaviour import UserBehaviour, UserBehaviourTable
from app.utils.data_shuffle import restructure_tbl_data

from app.main import SQLALCHEMY_DATABASE_URL
from app.db.model import user_behaviour_table_model
from app.db.connection import get_db, init_engine

router = APIRouter()

# database = get_db(SQLALCHEMY_DATABASE_URL)
# db_metadata = init_engine(SQLALCHEMY_DATABASE_URL)
# user_behaviour_tbl=user_behaviour_table_model(db_metadata)


# @router.get("/ping")
# async def pong():
#     # some async operation could happen here
#     # example: `notes = await get_all_notes()`
#     return {"ping": "pong!"}


# @router.get("/user_behaviour/table", response_model=List[UserBehaviourTable])
# async def read_user_behaviour():
#     query = user_behaviour_tbl.select()
#     return await database.fetch_all(query)

# @router.get("/user_behaviour/json", response_model=List[UserBehaviour])
# async def read_user_behaviour_json():
#     result = await restructure_tbl_data(database, user_behaviour_tbl)
#     print(result)
#     return result

# @router.post("/user_behaviour/validate")
# async def validate_user_behaviour(data: UserBehaviour):
#     print(f"Type: {type(data)} \n{data}")
#     return {"isValid": True}