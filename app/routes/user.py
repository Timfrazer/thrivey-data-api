from fastapi_crudrouter import DatabasesCRUDRouter
from typing import List


from app.models.UserBehaviour import User

from app.main import (
    user_tbl,
    database,
)

user_router = DatabasesCRUDRouter(
    schema=User,
    create_schema=User,
    table=user_tbl,
    database=database
)


@user_router.get("/user/table", response_model=List[User])
async def read_user():
    query = user_tbl.select()
    return await database.fetch_all(query)
@user_router.post("/user/validate")
async def validate_behaviour(data: User):
    print(f"Type: {type(data)} \n{data}")
    resp = {"model": User.schema()['title'], "isValid": True}
    return resp
