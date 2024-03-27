from http.client import HTTPException

import pkg_resources
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, field_validator, ValidationError, constr
from starlette.responses import HTMLResponse

from task_router import task_router
from user_router import user_router
from fastapi.staticfiles import StaticFiles



app = FastAPI()


app.include_router(task_router, prefix='/task_cont')
app.include_router(user_router, prefix='/user_router')
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/static",include_in_schema=False)
def root():
    return HTMLResponse(pkg_resources.resource_string(__name__, "static/a.html"))

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8080)

    # t1 = {'id': 1, 'name': 'a', 'description': 'aaa', 'if_done': True}
    # try:
    #     t2 = Task(**t1)
    #     print(t1)
    # except ValidationError as e:
    #     print(e)