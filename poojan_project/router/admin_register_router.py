
# from fastapi import APIRouter
# from model.register_model import Register
# from controller.register_controller import register_user

# registerRouter = APIRouter(prefix="/Register",tags=["Register"])

# @registerRouter.post("/UserRegister")
# async def create(register : Register):
#     return await register_user(register)

from fastapi import APIRouter
from model.admin_register_model import AdminRegister
from controller.admin_register_controller import admin_register

AdminRegisterRouter = APIRouter(
    prefix="/AdminRegister",
    tags=["Admin Register"]
)

@AdminRegisterRouter.post("/")
async def register(data: AdminRegister):
    return await admin_register(data)