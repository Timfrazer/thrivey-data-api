import logging
from typing import List
import json

from fastapi import APIRouter, HTTPException, Path
from fastapi_pagination import Page, add_pagination, paginate

from app.models.UserBehaviour import UserBehaviour
from app.main import api

# Init router
user_behaviour_json_router = APIRouter()
logger = logging.getLogger()

# Load data files
json_file='data/user_behaviour.json'
json_file10k='data/user_behaviour_10000.json'

with open(json_file) as user_json_file:
    json_data = json.load(user_json_file)

with open(json_file10k) as user_json_file10k:
    json_data10k = json.load(user_json_file10k)

# Load 150 records straight up
@api.get("/user_behaviour/json", response_model=UserBehaviour)
async def read_user_behaviour_json():
    result = (json_data)
    return result

# Load 10,000 recs with pagination
@api.get("/user_behaviour_10k/json", response_model=Page[UserBehaviour])
async def read_user_behaviour_json10k():
    result = paginate(json_data10k)
    return result

add_pagination(api)
