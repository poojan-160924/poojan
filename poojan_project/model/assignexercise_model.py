from pydantic import BaseModel
from typing import Optional
from bson import ObjectId

class AssignExerciseModel(BaseModel):
    user_id: str
    exercise_id: str
    sets: int
    reps: int


class AssignedExerciseResponse(BaseModel):
    id: str
    exercise_name: str
    sets: int
    reps: int


class ExerciseModel(BaseModel):
    name: str