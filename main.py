from scraping.fashscore import scrap_flashscore
from encrypt.jwt import  ACCESS_SECURITY, JWTAUTH

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from serializer.to_json import parser
from fastapi import Query
from datetime import date as DateType
from typing import Optional

from orm import ormGame
from dbconnection.connection import get_db
db = next(get_db())
app = FastAPI(docs_url="/", title="API Footbaal Today Odds 1.01")
# credentials: JWTAUTH = Security(ACCESS_SECURITY)
@app.get("/game/odds", tags=['OddsFootbaal'])
def scrape_flashscore(access:int = Query(...), date: Optional[DateType] = Query(None)):
    if (access != 1234 ):
        return parser("Access token invalid")

    result, code = ormGame.get_game(db, date)
    result = result
    return parser(content=result)

