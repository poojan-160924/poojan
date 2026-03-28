# from fastapi import APIRouter
# from model.User_master_model import UserMasterModel
# from controller.User_master_controller import create_user_master, get_user_masters,get_user_master, update_user_master, delete_user_master

# user_master_router = APIRouter(prefix="/api", tags=["User Master"])

# @user_master_router.post("/user_master")
# async def create_user_master_endpoint(user_master: UserMasterModel):
#     return await create_user_master(user_master)

# @user_master_router.get("/user_master")
# async def get_user_master_endpoint():
#     return await get_user_masters()

# @user_master_router.get("/user_master/{user_master_id}")
# async def get_user_master_endpoint(user_master_id: str):
#     return await get_user_master(user_master_id)

# @user_master_router.put("/user_master/{user_master_id}")
# async def update_user_master_endpoint(user_master_id: str, user_master: UserMasterModel):
#     return await update_user_master(user_master_id, user_master)

# @user_master_router.delete("/user_master/{user_master_id}")
# async def delete_user_master_endpoint(user_master_id: str):
#     return await delete_user_master(user_master_id)



from fastapi import APIRouter
from model.User_master_model import UserMasterModel
from controller.User_master_controller import create_user_master,get_user_masters,get_user_master,update_user_master,delete_user_master

user_master_router = APIRouter(prefix="/api", tags=["User Master"])


@user_master_router.post("/user_master")
async def create_user_master_endpoint(user_master: UserMasterModel):
    return await create_user_master(user_master)


@user_master_router.get("/user_master")
async def get_user_master_endpoint():
    return await get_user_masters()


@user_master_router.get("/user_master/{user_master_id}")
async def get_single_user_master_endpoint(user_master_id: str):
    return await get_user_master(user_master_id)


@user_master_router.put("/user_master/{user_master_id}")
async def update_user_master_endpoint(user_master_id: str, user_master: UserMasterModel):
    return await update_user_master(user_master_id, user_master)


@user_master_router.delete("/user_master/{user_master_id}")
async def delete_user_master_endpoint(user_master_id: str):
    return await delete_user_master(user_master_id)