from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import Annotated
URL_DATABASE = 'mysql+pymysql://root:@localhost:3308/classicmodels'

engine = create_engine(URL_DATABASE)

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
