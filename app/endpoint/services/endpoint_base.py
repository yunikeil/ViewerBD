from sqlalchemy.orm import Session

from db_models.user import User as UserModelDB
from dto.user import User as UserDTO

def creater_user(data: UserDTO, db: Session):
    user = UserModelDB(name=data.name)
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)
    return user

def get_user(id: int, db: Session):
    return db.query(UserModelDB).filter(UserModelDB.id==id).first()

def update(data: UserDTO, db: Session, id: int):
    user = db.query(UserModelDB).filter(UserModelDB.id==id).first()
    user.name = data.name
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def remove(db: Session, id: int):
    user = db.query(UserModelDB).filter(UserModelDB.id==id).delete()
    db.commit()
    return user
