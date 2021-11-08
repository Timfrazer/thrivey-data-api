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
    database=database,
    # get_all_route= False, # Default id handler doesnt match our pydantic modelling -> Set false
    # get_one_route= False, # Default id handler doesnt match our pydantic modelling -> Set false
)


@behaviour_router.get("/table", response_model=List[Behaviour])
async def read_behaviour():
    query = behaviour_tbl.select()
    return await database.fetch_all(query)
@behaviour_router.get("/{id}", response_model=List[Behaviour])
async def read_behaviour():
    query = behaviour_tbl.select()
    return await database.fetch_all(query)
@behaviour_router.post("/validate")
async def validate_behaviour(data: Behaviour):
    print(f"Type: {type(data)} \n{data}")
    resp = {"model": Behaviour.schema()['title'], "isValid": True}
    return resp
