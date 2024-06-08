from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
from database import get_db
import pyd
#модули для JWT токена
import auth_utils

router = APIRouter(
    prefix="/task",
    tags=["task"],
)

#получение списка плейлистов
@router.get('/', response_model=List[pyd.TaskBase])
async def get_tasks(db:Session=Depends(get_db)):
    tasks=db.query(models.Task).all()
    return tasks

#добавление плейлистов
@router.post('/', response_model=pyd.TaskBase)
async def create_tasks(task_input:pyd.TaskCreate, db:Session=Depends(get_db), payload:dict=Depends(auth_utils.auth_wrapper)):
    task_db=models.Task()
    task_db.name=task_input.name
    task_db.descr=task_input.descr
    db.add(task_db)
    db.commit()
    return task_db

#редактирование плейлистов
@router.put('/{task_id}', response_model=pyd.TaskBase)
async def update_tasks(task_id:int, task_input:pyd.TaskCreate, db:Session=Depends(get_db), payload:dict=Depends(auth_utils.auth_wrapper)):
    task_db=db.query(models.Task).filter(models.Task.id==task_id).first()
    if not task_db:
        raise HTTPException(status_code=404, detail="Задание не найдено!")
    task_db.name=task_input.name
    task_db.descr=task_input.descr

    db.commit()
    return task_db

#удаление плейлистов
@router.delete('/{task_id}')
async def delete_genres(task_id:int, db:Session=Depends(get_db), payload:dict=Depends(auth_utils.auth_wrapper)):
    task_db=db.query(models.Task).filter(models.Task.id==task_id).first()
    if not task_db:
        raise HTTPException(status_code=404, detail="Задание не найдено!")
    db.delete(task_db)
    db.commit()
    return "Плейлист успешно удалён!"