import sqlalchemy
from sqlalchemy import create_engine 

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///fastdb.db?check_same_thread=False"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base(metadata=sqlalchemy.MetaData())

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    