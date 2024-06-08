from pydantic import EmailStr, BaseModel, Field #настройка валидации
from datetime import date, datetime

class UserBase(BaseModel):
    id:int=Field(...,gt=0,example=228) 
    mail:EmailStr = Field(...,example="example@mail.ru")
    created_at:datetime=Field(...,example='2001-01-01 00:00:00')

    class Config:
        orm_mode=True #для соединения с бд

class TokenInfo(BaseModel):
    access_token:str
    token_type:str

class CourseBase(BaseModel):
    id:int=Field(...,gt=0,example=1)
    name:str=Field(...,example="Course Name")
    descr:str=Field(...,example="Course description")
    date_start:datetime=Field(...,example='2001-01-01 00:00:00')
    date_end:datetime=Field(...,example='20032-01-01 00:00:00')

    class Config:
        orm_mode=True 

class TaskBase(BaseModel):
    id: int = Field(...,gt=0, example=1)
    name: str = Field(..., example='Task Name')
    descr: str = Field(..., example='Task decsription here')
    class Config:
        orm_mode=True 

class MarkBase(BaseModel):
    id: int = Field(...,gt=0, example=1)
    mark: int = Field(..., example=1)
    class Config:
        orm_mode=True 
