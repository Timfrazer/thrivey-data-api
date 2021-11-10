import json
import logging
import random
from typing import List

from fastapi import APIRouter, HTTPException, Path
from fastapi_pagination import Page, add_pagination, paginate

from app.main import api
from app.models.UserBehaviour import UserBehaviour
from app.utils import http_error_generator

# Init router
user_behaviour_json_router = APIRouter()
logger = logging.getLogger()

# Load data files
json_file = "data/user_behaviour.json"
json_file10k = "data/user_behaviour_10000.json"

with open(json_file) as user_json_file:
    json_data = json.load(user_json_file)

with open(json_file10k) as user_json_file10k:
    json_data10k = json.load(user_json_file10k)


# Load 150 records straight up
@api.get("/user_behaviour/json", response_model=list[UserBehaviour])
async def read_user_behaviour_json():
    result = json_data
    logging.info("result: %s", result)
    return result


# HTTP endpoint that will fail 4/5 times
# Either pass the param[1-5] else randomly generate a request outcome each GET
@api.get("/user_behaviour/dodgy_endpoint")
async def read_user_behaviour_dodgy_endpoint(
    http_req_outcome: int = random.randint(1, 5)
):

    http_error_generator.generate_dummy_resp(http_req_outcome)

    # If option 1 occurs -> Successful response returned. Else HTTPException
    return json_data


# Load 10,000 recs with pagination
@api.get("/user_behaviour_10k/json", response_model=Page[UserBehaviour])
async def read_user_behaviour_json10k():
    result = paginate(json_data10k)
    return result


add_pagination(api)
