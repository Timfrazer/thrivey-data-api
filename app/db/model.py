import uuid

from sqlalchemy import Column, String, Integer
from sqlalchemy import Table
from sqlalchemy.ext.declarative import declarative_base


def user_behaviour_table_model(metadata):
    user_behaviour_tbl = Table(
        "user_behaviours",
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

# from db.connection import engine
# Base = declarative_base()
# metadata = MetaData()

# class UserBehaviourModel(Base):
#     __tablename__ = "user_behaviours"

#     index = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer)
#     first_name = Column(String)
#     last_name = Column(String)
#     user_created = Column(String)
#     thrivey_score = Column(Integer)
#     user_action = Column(String)
#     date_created = Column(String)
#     ipv4 = Column(String)




# # Base.metadata.create_all(engine)
