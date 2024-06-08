from sqlalchemy import Table, Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship #связь между таблицами
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy as sa
from sqlalchemy_utils import EmailType, URLType
from sqlalchemy.sql import func

from database import Base

category=Table('user_course', Base.metadata, #таблица, связывающая пользователя и курс
               Column('course_id', ForeignKey('courses.id')),
               Column('user_id', ForeignKey('users.id'))
               )

category=Table('user_task', Base.metadata, #таблица, связывающая оценки задания и студентов
               Column('user_id', ForeignKey('users.id')),
               Column('task_id', ForeignKey('tasks.id')),
               Column('mark_id', ForeignKey('marks.id'))
               )

class User(Base): 
    __tablename__ = "users"

    id = Column(Integer, primary_key=True) #первичный ключ
    mail = Column(EmailType, nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at=Column(TIMESTAMP(timezone=False), 
                        server_default=func.now())
    courses=relationship("Course", secondary='user_course', backref='users') #курс
    tasks=relationship("Task", secondary='user_task', backref='users') #задание
    marks=relationship("Mark", secondary='user_task', backref='users') #оценка

class Course(Base):
    __tablename__='courses'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    descr=Column(String(255), nullable=False)
    date_start=Column(DateTime(),nullable=False)
    date_end=Column(DateTime(),nullable=False)


class Task(Base):
    __tablename__='tasks'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    descr=Column(String(255), nullable=False)


class Mark(Base):
    __tablename__='marks'
    id = Column(Integer, primary_key=True)
    mark = Column(Integer, nullable=False)
