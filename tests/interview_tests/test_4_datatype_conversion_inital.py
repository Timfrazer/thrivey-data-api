from pydantic.main import BaseModel
import pytest

#################################
### 4. Datatype Conversions
#################################
# Test description:
## Within our UserBehaviours dataset we have 2 timestamp fields:
### - user.user_created -> 'Sep 25, 2021 9:33 PM'
### - behaviour.date_created -> 'Oct 19, 2021 12:57 PM'
## We want to write this dataset to out sqlite table, 
## however this STRING format is not compatable with our already existing table.
## The ORM will already be setup and configured so no need for implementing connection.

#TODO: 
# Decide do we want to convert to 1 of the following sqlite column types:
## (i) TEXT as ISO8601 strings ("YYYY-MM-DD HH:MM:SS.SSS").
## (ii) INTEGER as Unix Time, the number of seconds since 1970-01-01 00:00:00 UTC.

# Test aim:
## The aim is to take the objects within a request and:
### - traverse through the nested user() + behaviour() objects
### - Update the TS with the recommended datatype that conforms to both pydantic model + sqllite tbl
### - Write out the records to the sqlite table
### - Assert expected results are written to tbl

sample_json_list_of_records=[{
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
}]

#TBD
connection=()
sql_alchemy_table=()


#Pydantic Model
from pydantic import BaseModel, StrictInt, StrictStr

class UserBehaviour(BaseModel):
    id = StrictInt
    firstname = StrictStr
    user_created = 'str date'
    date_created = 'str date'

# This function will need to convert str ts -> recommended ts datatype value
def convert_ts(value_in: str):
    value_out=''
    return value_out

# TODO: Maybe create a db conn fixture here
def this_is_defininetly_not_a_test():
    result_list=[]

    for rec in sample_json_list_of_records:

        # Do the conversion:
        converted_user_created = convert_ts(sample_json_list_of_records['user']['user_created'])
        converted_date_created = convert_ts(sample_json_list_of_records['behaviour']['date_created'])

        result_list.append({
            'id' : sample_json_list_of_records['id'],
            'firstname' : sample_json_list_of_records['user']['first_name'],
            'user_created' : converted_user_created,
            'date_created' : converted_date_created,
        }[UserBehaviour])

    connection.execute(sql_alchemy_table.insert(),
        result_list
    )
