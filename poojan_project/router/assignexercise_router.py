from fastapi import APIRouter
from model.assignexercise_model import *
from controller.assignexercise_controller import *

assignrouter = APIRouter(prefix="/assignexercise", tags=["Assign Exercise"])


# Dropdown (only unassigned exercises)
@assignrouter.get("/available/{user_id}")
async def available_exercises(user_id: str):
    return await get_available_exercises(user_id)


# Add exercise
@assignrouter.post("/assign")
async def assign(data: AssignExerciseModel):
    return await assign_exercise(data)


# Show assigned list
@assignrouter.get("/list/{user_id}")
async def assigned_list(user_id: str):
    return await get_assigned_exercises(user_id)


# Delete
@assignrouter.delete("/delete/{assign_id}")
async def delete(assign_id: str):
    return await delete_assigned_exercise(assign_id)

# Add exercise to master list
@assignrouter.post("/add/exercise")
async def create_exercise(exercise: ExerciseModel):
    return await add_exercise(exercise)

# Add bulk exercises to master list
@assignrouter.post("/bulk/add/exercises")
async def seed_exercises():
    return await add_multiple_exercises()