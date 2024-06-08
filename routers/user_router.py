from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
from database import get_db
import pyd
import random, string
#модули для JWT токена
import auth_utils

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

def randomword(length): 
   letters = string.ascii_lowercase+string.digits
   return ''.join(random.choice(letters) for i in range(length))

#получение списка пользователей
@router.get('/', response_model=List[pyd.UserBase])
async def get_users(db:Session=Depends(get_db)):
    users=db.query(models.User).all()
    return users

#регистрация
@router.post("/reg", response_model=pyd.UserBase)
async def reg_user(user_input: pyd.UserCreate, db: Session = Depends(get_db)):
    user_db = db.query(models.User).filter(models.User.mail == user_input.mail).first()
    if user_db:
        raise HTTPException(400, 'Данная почта уже используется!')
    hash_pass = auth_utils.get_password_hash(user_input.password)
    user_db = models.User(
        mail=user_input.mail,
        password=hash_pass
    )
    db.add(user_db)
    db.commit()
    return user_db

#авторизация и выдача JWT токена
@router.post('/login')
async def user_login(user_input: pyd.UserCreate, db: Session = Depends(get_db)):
    user_db = db.query(models.User).filter(models.User.mail == user_input.mail).first()
    if not user_db:
        raise HTTPException(404, 'Вы не зарегестрированы!')
    if auth_utils.verify_password(user_input.password, user_db.password):
        token = auth_utils.encode_token(user_db.mail)
        return {'token': token}
    else:
        raise HTTPException(403, 'Пароль не верный!')