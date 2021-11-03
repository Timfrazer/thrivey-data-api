import json
import pandas as pd
import sqlite3

user_file='data/user.json'
behaviour_file='data/behaviour.json'
sqlite='data/thrivey.db'

with open(user_file) as user_json_file:
    user_data = json.load(user_json_file)

with open(behaviour_file) as behaviour_json_file:
    behaviour_data = json.load(behaviour_json_file)


user_df = pd.DataFrame(user_data)
print(user_df)

behaviour_df = pd.DataFrame(behaviour_data)
print(behaviour_df)

user_behaviour_df = pd.merge(user_df, behaviour_df, left_on='id', right_on='user_id').drop(columns=['id_x', 'id_y'])
print(user_behaviour_df)
print(user_behaviour_df.columns)

conn = sqlite3.connect( sqlite )

column_order = ["user_id", "first_name", "last_name", "session_id", "user_created", "thrivey_score", "user_action", "date_created"]
ordered_user_behaviour_df = user_behaviour_df.reindex(columns=column_order)

ordered_user_behaviour_df.to_sql('user_behaviours', conn, if_exists='replace', index=True)
print(pd.read_sql('select * from user_behaviours', conn))


