from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
from database import get_db
import pyd
#модули для JWT токена
import auth_utils

router = APIRouter(
    prefix="/mark",
    tags=["mark"],
)

#получение списка оценок
@router.get('/', response_model=List[pyd.MarkBase])
async def get_marks(db:Session=Depends(get_db)):
    marks=db.query(models.Mark).all()
    return marks

#добавление оценок
@router.post('/', response_model=pyd.MarkBase)
async def create_marks(mark_input:pyd.MarkCreate, db:Session=Depends(get_db), payload:dict=Depends(auth_utils.auth_wrapper)):
    marks_db=models.Mark()
    marks_db.mark=mark_input.mark
    db.add(marks_db)
    db.commit()
    return marks_db

#редактирование оценок
@router.put('/{mark_id}', response_model=pyd.MarkBase)
async def update_marks(mark_id:int, mark_input:pyd.MarkCreate, db:Session=Depends(get_db), payload:dict=Depends(auth_utils.auth_wrapper)):
    mark_db=db.query(models.Mark).filter(models.Mark.id==mark_id).first()
    if not mark_db:
        raise HTTPException(status_code=404, detail="Оценка не найдена!")
    mark_db.mark=mark_input.mark
    db.commit()
    return mark_db

#удаление оценок
@router.delete('/{mark_id}')
async def delete_marks(mark_id:int, db:Session=Depends(get_db), payload:dict=Depends(auth_utils.auth_wrapper)):
    mark_db=db.query(models.Mark).filter(models.Mark.id==mark_id).first()
    if not mark_db:
        raise HTTPException(status_code=404, detail="Оценка не найдена!")
    db.delete(mark_db)
    db.commit()
    return "Оценка успешно удалена!"