# Разработать API для управления списком задач с использованием базы данных MongoDB.
# Для этого создайте модель Task со следующими полями:
# ○ id: str (идентификатор задачи, генерируется автоматически)
# ○ title: str (название задачи)
# ○ description: str (описание задачи)
# ○ done: bool (статус выполнения задачи)
# API должно поддерживать следующие операции:
# ○ Получение списка всех задач: GET /tasks/
# ○ Получение информации о конкретной задаче: GET /tasks/{task_id}/
# ○ Создание новой задачи: POST /tasks/
# ○ Обновление информации о задаче: PUT /tasks/{task_id}/
# ○ Удаление задачи: DELETE /tasks/{task_id}/
# Для валидации данных используйте параметры Field модели Task.
# Для работы с базой данных используйте PyMongo.

from random import randint
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel, Field
import pymongo

db_client = pymongo.MongoClient("mongodb://localhost:27017")
current_db = db_client["task_5"]
collection = current_db["tasks"]

app = FastAPI()


class TaskIn(BaseModel):
    title: str = Field(max_length=32, title="Title")
    description: str = Field(max_length=128, title="Description")
    done: bool = Field(default=0, title="Status")


class Task(TaskIn):
    id: int


@app.get("/tasks/", response_model=List[Task])
async def read_tasks():
    return collection.find({})


@app.get('/tasks/{task_id}', response_model=Task)
async def read_task(task_id: int):
    return collection.find_one({'id': task_id})


@app.post("/tasks/", response_model=Task)
async def create_task(task: Task):
    create = {"id": task.id, "title": task.title, "description": task.description, "done": task.done}
    collection.insert_one(create)
    return create


@app.put('/tasks/{task_id}', response_model=TaskIn)
async def update_task(task_id: int, new_task: TaskIn):
    collection.update_one({"id": task_id}, {'$set': {"title": new_task.title,
                                                     "description": new_task.description, "done": new_task.done}})
    res = collection.find_one({'id': task_id})
    return res


@app.delete('/tasks/{task_id}')
async def delete_task(task_id: int):
    collection.delete_one({'id': task_id})
    return {"message": 'Task deleted'}


@app.get("/fake_tasks/{count}")
async def create_note(count: int):
    for i in range(1, count + 1):
        query = {'id': i,
                 'title': f'Title {i}',
                 'description': f'Description {i}',
                 'done': randint(0, 1)}
        collection.insert_one(query)
    return {'message': f'{count} fake tasks create'}
