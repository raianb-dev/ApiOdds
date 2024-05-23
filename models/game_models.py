from sqlalchemy import Column, String, DateTime
import datetime
from dbconnection.connection import Base
from datetime import date as DateType

class Jogo(Base):
    __tablename__ = 'game'

    id = Column(String(255), primary_key=True)
    home = Column(String)
    odd_home = Column(String)
    out = Column(String)
    odd_out = Column(String)
    tie = Column(String)
    time = Column(String)
    extract_date = Column(String, default=None)

    def get(self):
        date_only = self.extract_date.split()[0] if self.extract_date else None
        return{
            
            "id": self.id,
            "date-in": f"{date_only} {self.time}",
            "game":{
                "home":self.home,
                "out": self.out,
                "odds":{
                    "odds-home": self.odd_home,
                    "odds-out": self.odd_out,
                    "odds-tie": self.tie
                }
            }
        }
        
