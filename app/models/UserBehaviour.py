from pydantic import BaseModel


class User(BaseModel):
    first_name: str
    last_name: str
    user_created: str
    thrivey_score: int
    
class Behaviour(BaseModel):
    user_action: str
    date_created: str
    ipv4: str

class UserBehaviour(BaseModel):
    id: int
    user_id: str
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
