# from motor.motor_asyncio import AsyncIOMotorClient

# client = AsyncIOMotorClient(
#    "mongodb+srv://poojan:poojan6868@cluster0.cdae9ym.mongodb.net/"
#  )
# db = client["GYM_db"]
# Admin_register_collection = db["admin_register"]
# User_register_collection = db["user_register"]
# Admin_login_collection = db["admin_login"]
# login_collection = db["login"]
# exercise_collection = db["exercise_master"]
# gym_collection = db["gym_master"]

from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(
    "mongodb+srv://poojan:poojan6868@cluster0.cdae9ym.mongodb.net/"
)

# Database
db = client["GYM_db"]

# Collections
Admin_register_collection = db["admin_register"]
User_register_collection = db["user_register"]
Admin_login_collection = db["admin_login"]
login_collection = db["login"]
exercise_collection = db["exercise_master"]
gym_collection = db["gym_master"]
User_master = db["user_master"]
# Assign_exercise = db["assign_exercise"]

exercise_collection = db["exercise"]   # master exercises
assign_collection = db["assign_exercise"]  # assigned exercises