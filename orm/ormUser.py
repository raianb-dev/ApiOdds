from sqlalchemy.orm import Session
from models.user_models import User
from encrypt.jwt import create_token_jwt

def post(db: Session, user: str, payment: str):
    if payment == 'Aproval':
        token = create_token_jwt()
        new = User(
             username = user,
             access = token 
        )    
        db.add(new)
        db.commit()
        return 200, token
    else: 
        return 400, "payament not approval"