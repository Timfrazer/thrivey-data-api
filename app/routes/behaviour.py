from typing import List

from fastapi_crudrouter import DatabasesCRUDRouter

from app.main import behaviour_tbl, database
from app.models.UserBehaviour import Behaviour

behaviour_router = DatabasesCRUDRouter(
    schema=Behaviour,
    create_schema=Behaviour,
    table=behaviour_tbl,
    database=database,
)


@behaviour_router.get("/table", response_model=List[Behaviour])
async def read_behaviour():
    query = behaviour_tbl.select()
    return await database.fetch_all(query)


@behaviour_router.get("/{id}", response_model=List[Behaviour])
async def read_behaviour():
    query = behaviour_tbl.select()
    return await database.fetch_all(query)
