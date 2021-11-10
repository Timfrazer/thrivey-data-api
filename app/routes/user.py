from typing import List

from fastapi_crudrouter import DatabasesCRUDRouter

from app.main import database, user_tbl
from app.models.UserBehaviour import User

user_router = DatabasesCRUDRouter(
    schema=User,
    create_schema=User,
    table=user_tbl,
    database=database,
    get_one_route=False,  # Default id handler doesnt match our pydantic modelling -> Set false
)


@user_router.get("/table", response_model=List[User])
async def read_user():
    query = user_tbl.select()
    return await database.fetch_all(query)


@user_router.post("/validate")
async def validate_behaviour(data: User):
    print(f"Type: {type(data)} \n{data}")
    resp = {"model": User.schema()["title"], "isValid": True}
    return resp
