import models.model
from schemes.schemas import UserList
from fastapi import FastAPI, HTTPException, Depends, status
from db import engine, SessionLocal, Base
from sqlalchemy.orm import Session
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import Annotated

Base.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependecy = Annotated[Session, Depends(get_db)]


@app.post('/users/', status_code=status.HTTP_201_CREATED)
def create_user(user: UserList, db: db_dependecy):
    db_user = models.model.User(**user.dict())
    db.add(db_user)
    db.commit()


@app.get('/users/{user_id}', status_code=status.HTTP_200_OK)
def read_user(user_id: int, db: db_dependecy):
    user = db.query(models.model.User).filter(
        models.model.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail='Користувача не знайдено')
    return user


@app.delete('/user/{user_id}', status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: db_dependecy):
    db_user = db.query(models.model.User).filter(
        models.model.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail='Запис не знайдено')
    db.delete(db_user)
    db.commit()


@app.put('/user/{user_id}', status_code=status.HTTP_200_OK)
def update_user(user_id: int, user: UserList, db: db_dependecy):
    db_user = db.query(models.model.User).filter(
        models.model.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail='Запис не знайдено')
    db.query(models.model.User).filter(models.model.User.id == user_id).update(
        user.dict(), synchronize_session=False)
    db.commit()
