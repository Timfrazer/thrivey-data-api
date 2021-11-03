from decouple import config
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import databases


DEFAULT_SQLITE_DB='sqlite:///data/thrivey.db'
SQLALCHEMY_DATABASE_URL = config("DATABASE_URL", DEFAULT_SQLITE_DB)
print(SQLALCHEMY_DATABASE_URL)

import os
print(os.getcwd())
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_sesh():
    sesh = SessionLocal()
    try:
        yield sesh
    finally:
        sesh.close()

def get_db():
    database = databases.Database(DEFAULT_SQLITE_DB)
    metadata = MetaData()

    metadata.create_all(engine)

    return database
