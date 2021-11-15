import pytest


###################################
### 2. Handle failed HTTP Requests           
###################################
# Test description:
## We want to test the candidates knowledge of HTTP requests, status codes,
## Exceptions and exception handling

# Test aim:
## The aim is to fire 5 different requests at /user_behaviour/dodgy_endpoint
## When we pass the 'http_req_outcome' param, we will get 1 of 5 responses
### (i) /user_behaviour/dodgy_endpoint?http_req_outcome=1'
###     => HTTPResponse(200, expected_data)
### (ii) /user_behaviour/dodgy_endpoint?http_req_outcome=2'
###     => HTTPException(400, 'Validation Error')
### (iii) /user_behaviour/dodgy_endpoint?http_req_outcome=3'
###     => HTTPException(404, 'Not found error')
### (iv) /user_behaviour/dodgy_endpoint?http_req_outcome=4'
###     => HTTPException(401, 'Unauthourized Exception')
### (v) /user_behaviour/dodgy_endpoint?http_req_outcome=5'
###     => HTTPException(500, 'Server Error your code is f*****')


## TODO:
### Decide if we want to extend this into different scenarios, 
### where each request outcome will hold a challenge in itself 
### That will need to be resolved.
### Example:
### When HTTPException(401, 'Unauthourized Exception') => Why is this failing? 
# Do we need to a auth token in our header?

# See for more information:
from app.utils import http_error_generator
