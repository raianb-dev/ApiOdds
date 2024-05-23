from sqlalchemy.orm import Session
from models.game_models import Jogo
from scraping.fashscore import scrap_flashscore
import datetime
from sqlalchemy import func
from datetime import date as DateType

def get_game(db: Session, target_date: DateType):
    try:
        if target_date != None:
            query = db.query(Jogo).filter(func.date(Jogo.extract_date) == target_date)
            data = [Jogo.get() for Jogo in query]
            return data, 200
        else:
            return "Result Invalid", 400
    except:
        msg = 'Games not foud'
        return msg, 400

def insert(db: Session, url ):
        exemplo_dados = scrap_flashscore(url)
        for item in exemplo_dados:
            novo_jogo = Jogo(
                id=item["id"],
                home=item["home"]["name"],
                odd_home=item["home"]["odd-home"],
                out=item["out"]["name"],
                odd_out=item["out"]["odd-out"],
                tie=item["tie"]["odd"],
                time=item["time"],
                extract_date=str(datetime.datetime.now())
            )
            # Adicionando o novo jogo à sessão
            db.add(novo_jogo)
        # Commit para persistir os dados no banco de dados
        db.commit()


