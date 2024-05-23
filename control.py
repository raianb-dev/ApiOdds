from orm.ormGame import insert

from sqlalchemy.orm import Session
from dbconnection.connection import get_db

db = next(get_db()) 


insert(db, "https://www.flashscore.com.br/")

