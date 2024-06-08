from sqlalchemy.orm import Session
from database import engine
import models
from datetime import date

models.Base.metadata.drop_all(bind=engine) #пересоздание таблиц
models.Base.metadata.create_all(bind=engine) #пересоздание таблиц

with Session(bind=engine) as session:
    c1=models.Course(name="Информационные технологии", descr="44004400", date_start='2024-05-05 00:00:00', date_end='2025-05-05 00:00:00')
    c2=models.Course(name="Инфобизнес", descr="44004400", date_start='2024-05-05 00:00:00', date_end='2025-05-05 00:00:00')
    c3=models.Course(name="Конструкторские технологии", descr="44004400", date_start='2024-05-05 00:00:00', date_end='2025-05-05 00:00:00')
    c4=models.Course(name="Робототехника и машиностроение", descr="44004400", date_start='2024-05-05 00:00:00', date_end='2025-05-05 00:00:00')
    c5=models.Course(name="Карты таро и нумерология", descr="44004400", date_start='2024-05-05 00:00:00', date_end='2025-05-05 00:00:00')
    c6=models.Course(name="Автоматизация и управление", descr="44004400", date_start='2024-05-05 00:00:00', date_end='2025-05-05 00:00:00')

    m1=models.Mark(mark=1)
    m2=models.Mark(mark=2)
    m3=models.Mark(mark=3)
    m4=models.Mark(mark=4)
    m5=models.Mark(mark=5)

    t1=models.Task(name="Cоздать базу данных", descr="44004400")
    t2=models.Task(name="Написать реферат", descr="44004400")
    t3=models.Task(name="Оформить отчёт", descr="44004400")
    t4=models.Task(name="Сделать курсовой проект", descr="44004400")

    session.add_all([c1,c2,c3,c4,c5,c6,
                     m1,m2,m3,m4,m5,
                     t1,t2,t3,t4])
    session.commit()

