# Создать API для добавления нового пользователя в базу данных.
# Приложение должно иметь возможность принимать POST запросы с данными нового пользователя и сохранять их в базу данных.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте маршрут для добавления нового пользователя (метод POST).
# Реализуйте валидацию данных запроса и ответа.
#
# Создать API для обновления информации о пользователе в базе данных.
# Приложение должно иметь возможность принимать PUT запросы с данными пользователей и обновлять их в базе данных.
# Создайте маршрут для обновления информации о пользователе (метод PUT).
#
# Создать API для удаления информации о пользователе из базы данных.
# Приложение должно иметь возможность принимать DELETE запросы и удалять информацию о пользователе из базы данных.
# Создайте маршрут для удаления информации о пользователе (метод DELETE).

# Создать веб-страницу для отображения списка пользователей.
# Приложение должно использовать шаблонизатор Jinja для динамического формирования HTML страницы.
# Создайте HTML шаблон для отображения списка пользователей.
# Шаблон должен содержать заголовок страницы, таблицу со списком пользователей
# и кнопку для добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.


import pydantic
import uvicorn
from fastapi import FastAPI, HTTPException, Form
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='./templates')

users = []


class User(BaseModel):
    id_: int
    name: str
    email: pydantic.EmailStr
    password: pydantic.SecretStr


@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})


@app.get('/form/')
async def add_user_form(request: Request):
    return templates.TemplateResponse('form.html', {'request': request})


@app.get('/users/')
async def all_users():
    return {'users': users}


@app.post('/users/add')
async def add_users(user: User):
    users.append(user)
    return {"user": user, "status": "added"}


@app.post('/user/add')
async def add_user(id_=Form(), name=Form(), email=Form(), password=Form()):
    users.append(User(id_=id_, name=name, email=email, password=password))
    return RedirectResponse('/', status_code=302)


@app.put('/users/update/{user_id}')
async def update_user(user_id: int, new_user_data: User):
    for user in users:
        if user.id_ == user_id:
            user.id_ = new_user_data.id_
            user.name = new_user_data.name
            user.email = new_user_data.email
            user.password = new_user_data.password
            return {"user": user, "status": "updated"}
    return HTTPException(404, 'User not found')


@app.delete('/users/delete/{user_id}')
async def delete_user(user_id: int):
    for user in users:
        if user.id_ == user_id:
            users.remove(user)
            return {"status": "success"}
    return HTTPException(404, 'User not found')


if __name__ == "__main__":
    uvicorn.run("task_3_4_5_6:app", port=8000)