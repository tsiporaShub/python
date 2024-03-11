from http.client import HTTPException
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, field_validator, ValidationError, constr

app = FastAPI()


class Task(BaseModel):
    id: int
    name: constr(pattern=r"^[a-zA-Z]+$")
    description: constr(min_length=3, max_length=15)
    if_done: bool

    @field_validator('id')
    def check_id(cls, id):
        if id <= 0:
            raise ValueError('error')
        return id


tasks = {1:Task(**{'id': 1, 'name': 'a', 'description': 'aaa', 'if_done': True}),
         2:Task(**{'id': 2, 'name': 'b', 'description': 'bbb', 'if_done': False})}


@app.get("/")
async def getTasks():
    return tasks


@app.get("/{id}")
async def getTask(t_id):
    return tasks[int(t_id)]


@app.post("/task/")
async def add_task(task: Task):
    try:
        tasks[task.id]=task
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return task


@app.put("/{t_id}/")
async def update_task(t_id, task: Task):
    try:
        tasks[int(t_id)]=task
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return tasks[int(t_id)]


@app.delete("/{t_id}/")
async def delete_task(t_id):
    try:
        del tasks[int(t_id)]
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return t_id


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8080)

    # t1 = {'id': 1, 'name': 'a', 'description': 'aaa', 'if_done': True}
    # try:
    #     t2 = Task(**t1)
    #     print(t1)
    # except ValidationError as e:
    #     print(e)
