
# from fastapi import APIRouter
# from model.login_model import AdminLogin
# from controller.login_controller import *

# LoginRouter= APIRouter(prefix="/Login", tags=["Login"])

# @LoginRouter.post("/")
# async def Admin(login : AdminLogin):
#     return await Admin_login(login)
    
from fastapi import APIRouter
from model.admin_login_model import AdminLogin
from controller.admin_login_controller import admin_login

AdminLoginRouter = APIRouter(
    prefix="/AdminLogin",
    tags=["Admin Login"]
)

@AdminLoginRouter.post("/")
async def login(data: AdminLogin):
    return await admin_login(data)