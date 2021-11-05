
from sqlalchemy import select
import json
from databases import Database
from sqlalchemy import Table

async def restructure_tbl_data(database: Database, table: Table):

    query = table.select()
    res = await database.fetch_all(query)

    col_list=table.columns.keys()

    id_index = col_list.index('index')
    user_id_index = col_list.index('user_id')
    first_name_index = col_list.index('first_name')
    last_name_index = col_list.index('last_name')
    user_created_index = col_list.index('user_created')
    thrivey_score_index = col_list.index('thrivey_score')

    session_id_index = col_list.index('session_id')
    user_action_index = col_list.index('user_action')
    date_created_index = col_list.index('date_created')
    ipv4_index = col_list.index('ipv4')

    denormalized_obj_lst=[]
    for rec in res:
        restructured_record = {
            "id": rec[id_index],
            "user": {
                "id": rec[user_id_index],
                "first_name": rec[first_name_index],
                "last_name": rec[last_name_index],
                "user_created": rec[user_created_index],
                "thrivey_score": rec[thrivey_score_index],
            },
            "behaviour": {
                "user_id": rec[user_id_index],
                "session_id": rec[session_id_index],
                "user_action": rec[user_action_index],
                "date_created": rec[date_created_index],
                "ipv4": rec[ipv4_index],
            }
        }
        denormalized_obj_lst.append(restructured_record)
        
    print(denormalized_obj_lst)

    return denormalized_obj_lst
