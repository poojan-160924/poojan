
# from dbconnect import register_collection
# from model.register_model import Register
# # from bson import ObjectID
# from bcryptEx import *

# async def register_user(register: Register):
#     try:
#         hashed_password = hash_password(register.password)
#         register.password = hashed_password

#         result = await register_collection.insert_one(register.dict())

#         if result.inserted_id:
#             return {"message": "User registered successfully",
#                     "register_id" : str(result.inserted_id)}
#         else:
#             return {"message": "User registration failed"}
#     except Exception as e:
#         return {"error": str(e)}


from dbconnect import Admin_register_collection
from model.admin_register_model import AdminRegister
from bcryptEx import hash_password

async def admin_register(data: AdminRegister):
    try:

        hashed_password = hash_password(data.Password)

        admin = {
            "Adminname": data.Adminname,
            "Email": data.Email,
            "Password": hashed_password
        }

        result = await Admin_register_collection.insert_one(admin)

        return {
            "message": "Admin registered successfully",
            "id": str(result.inserted_id)
        }

    except Exception as e:
        return {"error": str(e)}