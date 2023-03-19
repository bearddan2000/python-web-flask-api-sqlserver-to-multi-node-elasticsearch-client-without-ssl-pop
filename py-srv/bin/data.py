import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

from db_schema import COLUMN_NAME
import db_settings
from model import DbModel

INDEX_NAME = "pop-demo"

def build_engine():
    return db.create_engine('{engine}://{username}:{password}@{host}/{db_name}'.format(
        **db_settings.SQLSERVER
    ), echo=db_settings.SQLALCHEMY['debug'] )

session_local = sessionmaker(
    bind= build_engine(),
    autoflush=db_settings.SQLALCHEMY['autoflush'],
    autocommit=db_settings.SQLALCHEMY['autocommit']
)

def get_session():
    session = session_local()
    try:
        yield session
    finally:
        session.close()

def main():
    session = next(get_session())

    result = session.query(DbModel).all()
    return [
        {
            COLUMN_NAME['col_0']['name']: col.__getattribute__(COLUMN_NAME['col_0']['name']),
            COLUMN_NAME['col_1']['name']: col.__getattribute__(COLUMN_NAME['col_1']['name']),
            COLUMN_NAME['col_2']['name']: col.__getattribute__(COLUMN_NAME['col_2']['name'])
        } for col in result]

DOC = main()