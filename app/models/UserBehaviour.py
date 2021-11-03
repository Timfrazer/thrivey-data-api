from pydantic import BaseModel

class UserBehaviour(BaseModel):
    index: int
    user_id: int
    first_name: str
    last_name: str
    user_created: str
    thrivey_score: int
    user_action: str
    date_created: str
