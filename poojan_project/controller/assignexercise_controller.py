from dbconnect import exercise_collection, assign_collection
from bson import ObjectId

# Add single exercise
async def add_exercise(exercise):
    existing = await exercise_collection.find_one({"name": exercise.name})

    if existing:
        return {"message": "Exercise already exists"}

    await exercise_collection.insert_one({
        "name": exercise.name
    })

    return {"message": "Exercise added"}

# Add bulk exercises to master list
async def add_multiple_exercises():
    
    exercises = [
        {"name": "Lunges"},
        {"name": "Jump Rope"},
        {"name": "Deadlift"},
        {"name": "Bicep Curl"},
        {"name": "Push-up"},
        {"name": "Squat"},
        {"name": "Shoulder Press"},
        {"name": "Plank"},
        {"name": "Plank new exercise"},
    ]

    await exercise_collection.insert_many(exercises)

    return {"message": "All exercises inserted"}

# Get exercises NOT assigned (for dropdown)
async def get_available_exercises(user_id: str):
    assigned = await assign_collection.find({"user_id": user_id}).to_list(100)

    assigned_ids = [a["exercise_id"] for a in assigned]

    exercises = await exercise_collection.find({
        "_id": {"$nin": [ObjectId(eid) for eid in assigned_ids]}
    }).to_list(100)

    result = []
    for ex in exercises:
        result.append({
            "id": str(ex["_id"]),
            "name": ex["name"]
        })

    return result


# Assign exercise to user
async def assign_exercise(data):
    obj = {
        "user_id": data.user_id,
        "exercise_id": data.exercise_id,
        "sets": data.sets,
        "reps": data.reps
    }

    await assign_collection.insert_one(obj)

    return {"message": "Exercise Assigned Successfully"}


# Get assigned exercises (table)
async def get_assigned_exercises(user_id: str):
    assigned = await assign_collection.find({"user_id": user_id}).to_list(100)

    result = []

    for a in assigned:
        exercise = await exercise_collection.find_one(
            {"_id": ObjectId(a["exercise_id"])}
        )

        result.append({
            "id": str(a["_id"]),
            "exercise_name": exercise["name"],
            "sets": a["sets"],
            "reps": a["reps"]
        })

    return result


# Delete assigned exercise
async def delete_assigned_exercise(assign_id: str):
    await assign_collection.delete_one({"_id": ObjectId(assign_id)})
    return {"message": "Deleted successfully"}

