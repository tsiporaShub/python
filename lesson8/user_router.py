from pip._internal.network.session import user_agent
from pydantic import BaseModel, field_validator, ValidationError, constr
from fastapi import FastAPI, Depends, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware

user_router = APIRouter()



class User(BaseModel):
    id: int
    name: constr(pattern=r"^[a-zA-Z]+$")
    age: int

    @field_validator('id')
    def check_id(cls, id):
        if id <= 0:
            raise ValueError('error')
        return id

    # @field_validator('age')
    # def check_id(cls, id):
    #     if id <= 0:
    #         raise ValueError('error')
    #     return id


users = {1:User(**{'id': 1, 'name': 'aaa', 'age':12}),
         2:User(**{'id': 2, 'name': 'bbb', 'age':10})}

def if_not_1(t_id: int):
    if t_id!=1:
        return True
    else:
        return False

@user_router.get("/")
async def getUsers():
    return users


@user_router.get("/{t_id}")
async def getUser(t_id,if_not_1:bool=Depends(if_not_1)):
    if if_not_1:
        return users[int(t_id)]
    raise HTTPException(status_code=404, detail="oops... you can not get the details")

@user_router.post("/user/")
async def add_user(user: User):
    try:
        users[user.id]=user
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return user


@user_router.put("/{t_id}/")
async def update_user(t_id, user: User):
    try:
        users[int(t_id)]=user
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return users[int(t_id)]


@user_router.delete("/{t_id}/")
async def delete_user(t_id):
    try:
        del users[int(t_id)]
    except ValidationError:
        raise HTTPException(status_code=400, detail="oops... an error occurred")
    return t_id