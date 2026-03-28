from dbconnect import gym_collection
from model.gymmaster_model import gymMaster
from bson import objectid

async def add_gym(gym: gymMaster):
    result = await gym_collection.insert_one(gym.dict())
    return {"message": "Gym added successfully"}

async def get_gyms():
    gyms = []
    cursor = gym_collection.find({})
    async for gym in cursor:
        gym["_id"] = str(gym["_id"])
        gyms.append(gym)
    return gyms

async def update_gym(gym_id: str, gym: gymMaster):
    result = await gym_collection.update_one(
        {"_id": objectid.ObjectId(gym_id)}, 
        {"$set": gym.dict()})
    if result.modified_count == 1:
        return {"message": "Gym updated successfully"}
    else:
        return {"message": "Gym not found"}
    
async def delete_gym(gym_id: str):
    result = await gym_collection.delete_one(
        {"_id": objectid.ObjectId(gym_id)})
    return {"message": "Gym deleted successfully"}
