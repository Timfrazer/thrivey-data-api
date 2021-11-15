import argparse
import json

from app.utils.data_generator import add_n_more_dummy_rows

# Define the parser
parser = argparse.ArgumentParser(description="Generate JSON UserBehaviour Data")
parser.add_argument("--rows", action="store", dest="rows", type=int, required=True)

args = parser.parse_args()
num_rows = args.rows

# Read sample json
json_file = "data/user_behaviour.json"
with open(json_file) as user_json_file:
    json_data = json.load(user_json_file)

# Return new JSON Collection
new_json = add_n_more_dummy_rows(json_data, num_rows)

# Write out data
json_file_out = "data/user_behaviour_{0}.json".format(num_rows)

with open(json_file_out, "w") as outfile:
    json.dump(new_json, outfile)
