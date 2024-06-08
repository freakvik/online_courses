from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import pyd
from typing import List
from routers import course_router, task_router, mark_router, user_router

app = FastAPI()

# подключение АпиРоутера
app.include_router(user_router)
app.include_router(course_router)
app.include_router(task_router)
app.include_router(mark_router)
