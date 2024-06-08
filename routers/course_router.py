from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
from database import get_db
import pyd
#модули для JWT токена
import auth_utils

router = APIRouter(
    prefix="/course",
    tags=["course"],
)

#получение списка курсов
@router.get('/', response_model=List[pyd.CourseBase])
async def get_courses(db:Session=Depends(get_db)):
    courses=db.query(models.Course).all()
    return courses

#добавление курса
@router.post('/', response_model=pyd.CourseBase)
async def create_courses(course_input:pyd.CourseCreate, db:Session=Depends(get_db), payload:dict=Depends(auth_utils.auth_wrapper)):
    course_db=models.Course()
    course_db.name=course_input.name
    course_db.descr=course_input.descr
    course_db.date_start=course_input.date_start
    course_db.date_end=course_input.date_end

    db.add(course_db)
    db.commit()
    return course_db

#редактирование курса
@router.put('/{course_id}', response_model=pyd.CourseBase)
async def update_courses(course_id:int, course_input:pyd.CourseCreate, db:Session=Depends(get_db), payload:dict=Depends(auth_utils.auth_wrapper)):
    course_db=db.query(models.Course).filter(models.Course.id==course_id).first()
    if not course_db:
        raise HTTPException(status_code=404, detail="Курс не найден!")
    course_db.name=course_input.name
    course_db.descr=course_input.descr
    course_db.date_start=course_input.date_start
    course_db.date_end=course_input.date_end
    db.add(course_db)
    db.commit()
    return course_db

#удаление курса
@router.delete('/{course_id}')
async def delete_courses(course_id:int, db:Session=Depends(get_db), payload:dict=Depends(auth_utils.auth_wrapper)):
    course_db=db.query(models.Course).filter(models.Course.id==course_id).first()
    if not course_db:
        raise HTTPException(status_code=404, detail="Курс не найден!")
    db.delete(course_db)
    db.commit()
    return "Удаление курса прошло успешно!"