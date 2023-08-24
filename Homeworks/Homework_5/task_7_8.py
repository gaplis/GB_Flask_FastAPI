# Создать RESTful API для управления списком задач.
# Приложение должно использовать FastAPI и поддерживать следующие функции:
# ○ Получение списка всех задач.
# ○ Получение информации о задаче по её ID.
# ○ Добавление новой задачи.
# ○ Обновление информации о задаче по её ID.
# ○ Удаление задачи по её ID.
# Каждая задача должна содержать следующие поля:
# ID (целое число), Название (строка), Описание (строка), Статус (строка): "todo", "in progress", "done".
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Task с полями id, title, description и status.
# Создайте список tasks для хранения задач.
# Создайте функцию get_tasks для получения списка всех задач (метод GET).
# Создайте функцию get_task для получения информации о задаче по её ID (метод GET).
# Создайте функцию create_task для добавления новой задачи (метод POST).
# Создайте функцию update_task для обновления информации о задаче по её ID (метод PUT).
# Создайте функцию delete_task для удаления задачи по её ID (метод DELETE)

# Необходимо создать API для управления списком задач.
# Каждая задача должна содержать заголовок и описание.
# Для каждой задачи должна быть возможность указать статус (выполнена/не выполнена).
# API должен содержать следующие конечные точки:
# ○ GET /tasks - возвращает список всех задач.
# ○ GET /tasks/{id} - возвращает задачу с указанным идентификатором.
# ○ POST /tasks - добавляет новую задачу.
# ○ PUT /tasks/{id} - обновляет задачу с указанным идентификатором.
# ○ DELETE /tasks/{id} - удаляет задачу с указанным идентификатором.
# Для каждой конечной точки необходимо проводить валидацию данных запроса
# и ответа. Для этого использовать библиотеку Pydantic.


import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

TASKS = []


class Task(BaseModel):
    id_: int
    title: str
    description: str
    status: str


@app.get('/tasks/')
async def get_tasks():
    return {'tasks': TASKS}


@app.get('/tasks/{task_id}')
async def get_task(task_id: int):
    for task in TASKS:
        if task.id_ == task_id:
            return {'task': task}
    return HTTPException(404, 'Task not found')


@app.post('/task/add')
async def create_task(task: Task):
    TASKS.append(task)
    return {"task": task, "status": "added"}


@app.put('/task/update/{task_id}')
async def update_task(task_id: int, task: Task):
    for t in TASKS:
        if t.id_ == task_id:
            t.title = task.title
            t.description = task.description
            t.status = task.status
            return {"task": task, "status": "updated"}
    return HTTPException(404, 'Task not found')


@app.delete('/task/delete/{task_id}')
async def delete_task(task_id: int):
    for t in TASKS:
        if t.id_ == task_id:
            TASKS.remove(t)
            return {"status": "success"}
    return HTTPException(404, 'Task not found')


if __name__ == "__main__":
    uvicorn.run("task_7_8:app", port=8000)
