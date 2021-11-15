import pytest


#################################
### 3. Request Pagination
#################################
# Test description:
## The endpoint: /user_behaviour_10k/json returns too many JSON objects
## Need to paginate to split up requests into pages and return 
## in batches of 50?

# Test aim:
## The aim is to pull the first 500 records out of the 10k collection 
## on the /user_behaviour_10k/json endpoint
## The candidate will need to loop through 10 pages of 50 records each time

## PSUEDO CODE
def not_a_real_test_yet(test_app):
    page_size=50
    result_list=[]
    
    # We dont want:
    test_app.get(
            f"/user_behaviour_10k/json",
        )
    
    # We do want:
    for i in range(1, 10):
        response = test_app.get(
            f"/user_behaviour_10k/json?page={i}&size={page_size}",
        )
        result_list.append(response.json())

    # Assert final list of objs
    assert len(result_list['items']) == 500

