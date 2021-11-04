from pydantic import BaseModel
from typing import  Optional

class User(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    user_created: str
    thrivey_score: int
    
class Behaviour(BaseModel):
    user_id: int
    session_id: int
    user_action: str
    date_created: str
    ipv4: str

class UserBehaviour(BaseModel):
    id: int
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
