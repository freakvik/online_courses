from pydantic import BaseModel, Field, EmailStr #какой формат данных хотим от пользователя
from typing import List
from datetime import date, datetime

class UserCreate(BaseModel):
    mail:EmailStr = Field(...,example="example@mail.ru")
    password:str=Field(...,max_length=255, min_length=6,example="qwertyuiop")

class CourseCreate(BaseModel):
    name: str = Field(..., max_length=255,
                          min_length=3, example='Course Name')
    descr: str = Field(..., max_length=255, min_length=6, example='Course description')
    date_start: datetime = Field(..., example='2001-01-01 00:00:00')
    date_end: datetime = Field(..., example='2032-01-01 00:00:00')

class TaskCreate(BaseModel):
    name: str = Field(..., max_length=255,
                          min_length=3, example='Task Name')
    descr: str = Field(..., max_length=255, min_length=6, example='Task description')

class MarkCreate(BaseModel):
    mark: int = Field(..., example=1)
