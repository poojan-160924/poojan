from fastapi import APIRouter
from model.gymmaster_model import gymMaster
from controller.gymmaster_controller import *

gymMasterRouter = APIRouter(prefix="/GymMaster", tags=["GymMaster"])

@gymMasterRouter.post("/AddGym")
async def add_gyms(gym: gymMaster):
    return await add_gym(gym)

@gymMasterRouter.get("/GetGyms")
async def get_gym():
    return await get_gyms()

@gymMasterRouter.put("/UpdateGym/{gym_id}")
async def update_gyms(gym_id: str, gym: gymMaster):
    return await update_gym(gym_id, gym)

@gymMasterRouter.delete("/DeleteGym/{gym_id}")
async def delete_gyms(gym_id: str):
    return await delete_gym(gym_id)

