from sqlalchemy.orm import Session, sessionmaker
from .models import User, Base
from .database import SessionLocal, engine

Base.metadata.create_all(bind=engine)
db = SessionLocal()

def create_user(chat_id:int):
    db_user = User(id=chat_id, indicators=None, interval="1h", style="candle", timezone="America/New_York", chain="ethereum")
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except:
        return False
    return db_user

# Define the indicator updating function
def update_indicators(id:int, indicators:str):
    user = db.query(User).filter(User.id == id).update({"indicators" : indicators})
    try:
        db.commit()
    except:
        return False
    return user

# Define the interval updating function
def update_interval(id:int, interval:str):
    user = db.query(User).filter(User.id == id).update({"interval" : interval})
    try:
        db.commit()
    except:
        return False
    return user

# Define the style updating function
def update_style(id:int, style:str):
    user = db.query(User).filter(User.id == id).update({"style" : style})
    try:
        db.commit()
    except:
        return False
    return user

# Define the timezone updating function
def update_timezone(id:int, timezone:str):
    user = db.query(User).filter(User.id == id).update({"timezone" : timezone})
    try:
        db.commit()
    except:
        return False
    return user

# Define the default chain updating function
def update_chain(id:int, chain:str):
    user = db.query(User).filter(User.id == id).update({"chain" : chain})
    try:
        db.commit()
    except:
        return False
    return user

def get_user_by_id(id:int):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        return False
    return user

def delete_user(id:int):
    try:
        db.query(User).filter(User.id == id).delete()
        db.commit()
        return True
    except:
        return False

def count_user():
    user = db.query(User).count()
    if not user:
        return False
    return user