import json
import pandas as pd
import sqlite3
from utils.data_generator import add_fake_ipv4_col

# Data files
user_file='data/user.json'
behaviour_file='data/behaviour.json'
sqlite='data/thrivey.db'

# Open json data files
with open(user_file) as user_json_file:
    user_data = json.load(user_json_file)
with open(behaviour_file) as behaviour_json_file:
    behaviour_data = json.load(behaviour_json_file)

# Init sqlite connection
conn = sqlite3.connect( sqlite )

# Read json as PD DF's
user_df = pd.DataFrame(user_data)
print(user_df)

behaviour_df = add_fake_ipv4_col( pd.DataFrame(behaviour_data) )
print(behaviour_df)

# Merge DF's => UserBehaviour
user_behaviour_df = pd.merge(user_df, behaviour_df, left_on='id', right_on='user_id').drop(columns=['id_x', 'id_y'])
print(user_behaviour_df)
print(user_behaviour_df.columns)

# Shuffle cols
column_order = ["user_id", "first_name", "last_name", "session_id", "user_created", "thrivey_score", "user_action", "date_created", "ipv4"]
ordered_user_behaviour_df = user_behaviour_df.reindex(columns=column_order)

# Write out DF's as sqlite tbls
user_df.to_sql('user', conn, if_exists='replace', index=True)
behaviour_df.to_sql('behaviour', conn, if_exists='replace', index=True)
ordered_user_behaviour_df.to_sql('user_behaviours', conn, if_exists='replace', index=True)
print(pd.read_sql('select * from user_behaviours', conn))


