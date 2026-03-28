
# from fastapi import APIRouter
# from model.user_login_model import userLogin
# from controller.userlogin_controller import *

# LoginRouter= APIRouter(prefix="/Login", tags=["Login"])

# @LoginRouter.post("/")
# async def User(login : userLogin):
#     return await User_login(login)
    

from fastapi import APIRouter
from model.user_login_model import UserLogin
from controller.user_login_controller import user_login

UserLoginRouter = APIRouter(
    prefix="/UserLogin",
    tags=["User Login"]
)

@UserLoginRouter.post("/")
async def login(data: UserLogin):
    return await user_login(data)