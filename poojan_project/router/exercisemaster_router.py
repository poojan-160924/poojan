from fastapi import APIRouter
from model.exercisemaster_model import ExerciseMaster
from controller.exercisemaster_controller import *

exerciseMasterRouter = APIRouter(prefix="/ExerciseMaster", tags=["ExerciseMaster"])


@exerciseMasterRouter.post("/AddExercise")
async def add_exercises(exercise: ExerciseMaster):
    return await add_exercise(exercise)

@exerciseMasterRouter.get("/GetExercises")
async def get_exercise():
    return await get_exercises()

@exerciseMasterRouter.put("/UpdateExercise/{exercise_id}")
async def update_exercises(exercise_id: str, exercise: ExerciseMaster):
    return await update_exercise(exercise_id, exercise)

@exerciseMasterRouter.delete("/DeleteExercise/{exercise_id}")
async def delete_exercises(exercise_id: str):
    return await delete_exercise(exercise_id)