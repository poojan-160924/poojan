from dbconnect import User_register_collection
from model.user_register_model import UserRegister
from bcryptEx import hash_password

async def user_register(data: UserRegister):

    hashed = hash_password(data.Password)

    user = {
        "Username": data.Username,
        "Email": data.Email,
        "Password": hashed
    }

    await User_register_collection.insert_one(user)

    return {"message": "User Registered Successfully"}