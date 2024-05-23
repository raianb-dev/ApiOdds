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

# Configurações de CORS
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "https://football-odds-api.p.rapidapi.com",
    "https://odds-api-football.p.rapidapi.com"
    "http://localhost",
    # Adicione outras origens permitidas aqui
]

app = FastAPI(docs_url="/", title="API Football Today Odds 1.01")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# credentials: JWTAUTH = Security(ACCESS_SECURITY)
@app.get("/game/odds", tags=['OddsFootbaal'])
def scrape_flashscore(access:int = Query(...), date: Optional[DateType] = Query(None)):
    if (access != 1234 ):
        return parser("Access token invalid")

    result, code = ormGame.get_game(db, date)
    result = result
    return parser(content=result)

