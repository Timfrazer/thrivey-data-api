from pydantic import BaseModel, StrictInt, StrictStr, conlist
from typing import  Optional

class User(BaseModel):
    id: StrictInt
    first_name: StrictStr
    last_name: StrictStr
    user_created: str
    thrivey_score: StrictInt
    
class Behaviour(BaseModel):
    user_id: StrictInt
    session_id: StrictInt
    user_action: StrictStr
    date_created: str
    ipv4: str

class UserBehaviour(BaseModel):
    id: StrictInt
    user: User
    behaviour: Behaviour

class UserBehaviourTable(BaseModel):
    index: int
    user_id: int
    first_name: str
    last_name: str
    user_created: str
    thrivey_score: int
    user_action: str
    date_created: str
    ipv4: str
