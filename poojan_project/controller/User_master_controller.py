from model.User_master_model import UserMasterModel
from dbconnect import User_master
from bson import ObjectId

async def create_user_master(user_master: UserMasterModel):
    user_master_dict = user_master.dict()
    await User_master.insert_one(user_master_dict)
    return {"message": "User created successfully"}

async def get_user_masters():
    user_masters = []
    async for user_master in User_master.find():
        user_master["id"] = str(user_master["_id"])
        del user_master["_id"]
        user_masters.append(user_master)
    return user_masters

async def get_user_master(user_master_id: str):
    try:
        user_master = await User_master.find_one({"_id": ObjectId(user_master_id)})
        if user_master:
            user_master["id"] = str(user_master["_id"])
            del user_master["_id"]
            return user_master
        else:
            return {"message": "User not found"}
    except InvalidId:
        return {"message": "Invalid ID"}

async def update_user_master(user_master_id: str, user_master: UserMasterModel):
    try:
        result = await User_master.update_one(
            {"_id": ObjectId(user_master_id)}, 
            {"$set": user_master.dict()})
        if result.modified_count == 1:
            return {"message": "User updated successfully"}
        else:
            return {"message": "User not found"}
    except InvalidId:
        return {"message": "Invalid ID"}
    


async def delete_user_master(user_master_id:str):
    try:
        await User_master.delete_one({"_id": ObjectId(user_master_id)})
        return {"message": "User deleted successfully"}
    except InvalidId:
        return {"message": "Invalid ID"}