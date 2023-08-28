# Создать веб-приложение на FastAPI, которое будет предоставлять API для работы с базой данных пользователей.
# Пользователь должен иметь следующие поля:
# ○ ID (автоматически генерируется при создании пользователя)
# ○ Имя (строка, не менее 2 символов)
# ○ Фамилия (строка, не менее 2 символов)
# ○ Дата рождения (строка в формате "YYYY-MM-DD")
# ○ Email (строка, валидный email)
# ○ Адрес (строка, не менее 5 символов)
# API должен поддерживать следующие операции:
# ○ Добавление пользователя в базу данных
# ○ Получение списка всех пользователей в базе данных
# ○ Получение пользователя по ID
# ○ Обновление пользователя по ID
# ○ Удаление пользователя по ID
# Приложение должно использовать базу данных SQLite3 для хранения пользователей.

from typing import List
import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from datetime import date

DATABASE_URL = "sqlite:///Homeworks/Homework_6/task_2.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(20)),
    sqlalchemy.Column("last_name", sqlalchemy.String(20)),
    sqlalchemy.Column("birth", sqlalchemy.String(15)),
    sqlalchemy.Column("email", sqlalchemy.String(50)),
    sqlalchemy.Column("address", sqlalchemy.String(64)),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)

app = FastAPI()


class UserIn(BaseModel):
    name: str = Field(min_length=2, max_length=20)
    last_name: str = Field(min_length=2, max_length=20)
    birth: date
    email: EmailStr = Field(max_length=50)
    address: str = Field(min_length=5, max_length=64)


class User(UserIn):
    id: int


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/users/", response_model=List[User])
async def read_users():
    query = users.select()
    return await database.fetch_all(query)


@app.get('/users/{user_id}', response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)


@app.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(**user.model_dump())
    last_record_id = await database.execute(query)
    return {**user.model_dump(), "id": last_record_id}


@app.put('/users/{user_id}', response_model=User)
async def update_user(user_id: int, new_user: UserIn):
    query = users.update().where(users.c.id == user_id).values(**new_user.model_dump())
    await database.execute(query)
    return {**new_user.model_dump(), "id": user_id}


@app.delete('/users/{user_id}')
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {"message": 'User deleted'}


@app.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(name=f'Name{i}', last_name=f'Last Name {i}', birth=f'2023-08-0{i}',
                                      email=f'mail{i}@mail.ru', address=f'Address{i}')
        await database.execute(query)
    return {'message': f'{count} fake users create'}
