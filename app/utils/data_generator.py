from datetime import datetime

from faker import Faker
from faker.providers import date_time, internet

# Init faker with providers
fake = Faker()
fake.add_provider(internet)
fake.add_provider(date_time)

user_behaviour_actions = [
    "A1",
    "A3",
    "B6",
    "B12",
    "C3",
    "C8",
    "D3",
    "D8",
    "E3",
    "E8",
    "F3",
    "F8",
    "G3",
    "G8",
    "H3",
    "H8",
    "I3",
    "I8",
    "J3",
    "J8",
    "K3",
    "K8",
]

# datetime format
default_datetime_format = "%b %d, %Y %-I:%M %p"
iso_8601_format = "%Y%m%dT%H%M%S.%fZ"

# Generate IPV4 column for Pandas DF
def add_fake_ipv4_col(pandas_df):
    for index, row in pandas_df.iterrows():
        pandas_df.loc[index, "ipv4"] = fake.ipv4_private()
    return pandas_df


# Generate n more json objects from dict and return larger dict object. CAUTION $$$$$$$EXPENSIVE$$$$$$$$!
def add_n_more_dummy_rows(
    list_of_dicts: list, increase_rows: int, dt_format=default_datetime_format
):
    maxIdIter = max(list_of_dicts, key=lambda x: x["id"])["id"]
    maxUserIdIter = max(list_of_dicts, key=lambda x: x["user"]["id"])["id"]
    print(f"maxIdIter: {maxIdIter}")
    print(f"maxUserIdIter: {maxUserIdIter}")

    for i in range(increase_rows):
        maxIdIter += 1
        maxUserIdIter += 1

        restructured_record = {
            "id": maxIdIter,
            "user": {
                "id": maxUserIdIter,
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "user_created": fake.date_time_ad(
                    start_datetime="-5m", end_datetime="-4m"
                ).strftime(format=dt_format),
                "thrivey_score": fake.pyint(min_value=1, max_value=100),
            },
            "behaviour": {
                "user_id": maxUserIdIter,
                "session_id": fake.pyint(min_value=1, max_value=3),
                "user_action": fake.word(user_behaviour_actions),
                "date_created": fake.date_time_ad(
                    start_datetime="-4m", end_datetime="-3m"
                ).strftime(format=dt_format),
                "ipv4": fake.ipv4_private(),
            },
        }
        list_of_dicts.append(restructured_record)
    return list_of_dicts
