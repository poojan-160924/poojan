from fastapi import APIRouter
from model.user_register_model import UserRegister
from controller.user_register_controller import user_register

UserRegisterRouter = APIRouter(
    prefix="/UserRegister",
    tags=["User Register"]
)

@UserRegisterRouter.post("/")
async def register(data: UserRegister):
    return await user_register(data)