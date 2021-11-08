import pytest

mocked_record={
    "id": 0,
    "user": {
        "id": 1,
        "first_name": "John",
        "last_name": "Fakington",
        "user_created": "Sep 14, 2021 4:32 AM",
        "thrivey_score": 99
    },
    "behaviour": {
        "id": 1,
        "user_id": 1,
        "session_id": 1,
        "user_action": "A1",
        "date_created": "Oct 17, 2021 5:23 AM",
        "ipv4": "10.0.0.1"
    }
}


def test_root(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
    assert response.json() == {"Thrivey": "OK"}



def test_validate_valid_doc_returns_success(test_app):
    response = test_app.post(
        "/user_behaviour/validate",
        json=mocked_record,
    )
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {'model': 'UserBehaviour', 'isValid': True}



def test_validate_invalid_doc_returns_422(test_app):

    # Update record with invalid type
    mocked_record['id'] = "ThisIsAnInvalidType"

    response = test_app.post(
        "/user_behaviour/validate",
        headers={"X-Token": "coneofsilence"},
        json=mocked_record,
    )

    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == "value is not a valid integer"




