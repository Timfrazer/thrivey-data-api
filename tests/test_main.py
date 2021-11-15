import pytest

mocked_record = {
    "id": 0,
    "user": {
        "id": 1,
        "first_name": "John",
        "last_name": "Fakington",
        "user_created": "Sep 14, 2021 4:32 AM",
        "thrivey_score": 99,
    },
    "behaviour": {
        "id": 1,
        "user_id": 1,
        "session_id": 1,
        "user_action": "A1",
        "date_created": "Oct 17, 2021 5:23 AM",
        "ipv4": "10.0.0.1",
    },
}

# /
def test_root(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"Thrivey": "OK"}


# /user_behaviour/json
def test_get_json_returns_success(test_app):
    response = test_app.get(
        "/user_behaviour/json",
    )
    assert response.status_code == 200
    assert response.json()[0]["id"] == 0


# /user_behaviour_10k/json
def test_paginated_api_should_return_expected_num_records(test_app):

    # Set pagination params
    page_num = 1
    page_size = 50

    response = test_app.get(
        f"/user_behaviour_10k/json?page={page_num}&size={page_size}",
    )
    resp_json = response.json()
    assert response.status_code == 200
    assert len(resp_json["items"]) == 50
    assert (resp_json["page"]) == 1
    assert (resp_json["size"]) == 50
