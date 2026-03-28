from dbconnect import exercise_collection
from model.exercisemaster_model import ExerciseMaster
from bson import ObjectId

async def add_exercise(exercise: ExerciseMaster):
    result = await exercise_collection.insert_one(exercise.dict())
    return {"message": "Exercise added successfully"}

async def get_exercises():
    exercises = []
    cursor = exercise_collection.find({})
    async for exercise in cursor:
        exercise["_id"] = str(exercise["_id"])
        exercises.append(exercise)
    return exercises

async def update_exercise(exercise_id: str, exercise: ExerciseMaster):
    result = await exercise_collection.update_one(
        {"_id": ObjectId(exercise_id)}, 
        {"$set": exercise.dict()})
    return {"message": "Exercise updated successfully"}
    
async def delete_exercise(exercise_id: str):
    result = await exercise_collection.delete_one(
        {"_id": ObjectId(exercise_id)})
    return {"message": "Exercise deleted successfully"}
    