import pytest

#################################
### 1. Merge Behaviours by User
#################################
# Test description:
##  Each UserBehaviour{} object contains both a single User() and Behaviour()
##  See starting_json below:
starting_json = [
    {
        "id": 0,
        "user": {
            "id": 1,
            "first_name": "Fawne",
            "last_name": "MacDowal",
            "user_created": "Sep 14, 2021 4:32 AM",
            "thrivey_score": 81,
        },
        "behaviour": {
            "user_id": 1,
            "session_id": 3,
            "user_action": "C423",
            "date_created": "Oct 17, 2021 5:23 AM",
            "ipv4": "172.30.189.226",
        },
    },
    {
        "id": 1,
        "user": {
            "id": 1,
            "first_name": "Fawne",
            "last_name": "MacDowal",
            "user_created": "Sep 14, 2021 4:32 AM",
            "thrivey_score": 81,
        },
        "behaviour": {
            "user_id": 1,
            "session_id": 1,
            "user_action": "E77",
            "date_created": "Oct 16, 2021 7:05 PM",
            "ipv4": "10.49.192.181",
        },
    },
]
# Test aim:
## The aim is to firstly,
## - consume the 150 UserBehaviour objects via Requests,
## - merge the behaviours object and create a new JSON entry
## - where each JSON object contains:
### (i) A single user object
### (ii) n Behaviour objects - all behaviour objects associated with that userId

# Sample of expected JSON to assert at end of test:
final_json = [
    {
        "id": 0,
        "user": {
            "id": 1,
            "first_name": "Fawne",
            "last_name": "MacDowal",
            "user_created": "Sep 14, 2021 4:32 AM",
            "thrivey_score": 81,
        },
        "behaviour": [
            {
                "user_id": 1,
                "session_id": 3,
                "user_action": "C423",
                "date_created": "Oct 17, 2021 5:23 AM",
                "ipv4": "172.30.189.226",
            },
            {
                "user_id": 1,
                "session_id": 1,
                "user_action": "E77",
                "date_created": "Oct 16, 2021 7:05 PM",
                "ipv4": "10.49.192.181",
            },
        ],
    }
]
