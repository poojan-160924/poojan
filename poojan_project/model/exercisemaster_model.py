from pydantic import BaseModel

class ExerciseMaster(BaseModel):
    ExerciseName: str
    caloriesBurned: int
    category: str
    difficulty: str
    equipment: str
    muscleGroup: str
    reps: int
    sets: int
    Action: str
