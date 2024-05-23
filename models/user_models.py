from dbconnection.connection import Base
from sqlalchemy import String, Column


class User(Base):
    __tablename__ = "user"
    id = Column(String(255), primary_key=True)
    username = Column(String)
    access = Column(String(510))
    
    def get_access(self):
        return{
            "access":self.access
        }
    