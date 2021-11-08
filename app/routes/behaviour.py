from fastapi_crudrouter import DatabasesCRUDRouter
from typing import List


from app.models.UserBehaviour import Behaviour

from app.main import (
    behaviour_tbl,
    database,
)

behaviour_router = DatabasesCRUDRouter(
    schema=Behaviour,
    create_schema=Behaviour,
    table=behaviour_tbl,
    database=database
)


@behaviour_router.get("/behaviour/table", response_model=List[Behaviour])
async def read_behaviour():
    query = behaviour_tbl.select()
    return await database.fetch_all(query)
@behaviour_router.post("/behaviour/validate")
async def validate_behaviour(data: Behaviour):
    print(f"Type: {type(data)} \n{data}")
    resp = {"model": Behaviour.schema()['title'], "isValid": True}
    return resp
