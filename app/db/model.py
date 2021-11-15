import uuid

from sqlalchemy import Column, Integer, String, Table, Text


def user_table_model(metadata) -> Table:
    user_tbl = Table(
        "user",
        metadata,
        Column("index", Integer, primary_key=True),
        Column("id", Integer),
        Column("first_name", String),
        Column("last_name", String),
        Column("user_created", String),
        Column("thrivey_score", Integer),
    )
    return user_tbl


def behaviour_table_model(metadata) -> Table:
    behaviour_tbl = Table(
        "behaviour",
        metadata,
        Column("index", Integer, primary_key=True),
        Column("id", Integer),
        Column("user_id", Integer),
        Column("session_id", Integer),
        Column("user_action", String),
        Column("date_created", String),
        Column("ipv4", String),
    )
    return behaviour_tbl


def user_behaviour_table_model(metadata) -> Table:
    user_behaviour_tbl = Table(
        "user_behaviour",
        metadata,
        Column("index", Integer, primary_key=True),
        Column("user_id", Integer),
        Column("first_name", String),
        Column("last_name", String),
        Column("user_created", String),
        Column("thrivey_score", Integer),
        Column("session_id", Integer),
        Column("user_action", String),
        Column("date_created", String),
        Column("ipv4", String),
    )
    return user_behaviour_tbl


def user_behaviour_json_model(metadata) -> Table:
    user_behaviour_json = Table(
        "user_behaviour_json",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("user", Text),
        Column("behaviour", Text),
    )
    return user_behaviour_json
