from fastapi import HTTPException


# Return 1 of 5 dummy HTTP Responses
def success():
    print("Successful Response!")


def bad_request():
    raise HTTPException(status_code=400, detail="Validation Failed!")


def not_found():
    raise HTTPException(status_code=404, detail="Item not found!")


def unauthourized():
    raise HTTPException(status_code=401, detail="Unauthorized!")


def server_error():
    raise HTTPException(status_code=500, detail="Server Error!")


def generate_dummy_resp(choice):
    options = {
        1: success,
        2: bad_request,
        3: not_found,
        4: unauthourized,
        5: server_error,
    }
    try:
        options[choice]()
    # Handle int value outside the above selection
    except KeyError:
        not_found
