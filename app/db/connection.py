from decouple import config
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import databases


def init_engine(db_url):
    engine = create_engine(
        db_url, 
        connect_args={"check_same_thread": False}
    )
    metadata = MetaData()
    metadata.create_all(engine)

    return metadata


def get_db(db_url):
    database = databases.Database(db_url)

    return database




# def get_sesh():
#     SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#     Base = declarative_base()
#     sesh = SessionLocal()
#     try:
#         yield sesh
#     finally:
#         sesh.close()
