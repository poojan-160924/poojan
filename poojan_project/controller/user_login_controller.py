# from dbconnect import register_collection
# from model.user_login_model import userLogin
# from bcryptEx import hash_password,verify_password
# from bson import ObjectId

# async def user_login(user_login : userLogin):
#     try:
#         query= {"Username": user_login.Username}
#         result= await register_collection.find_one(query)
#         print(result)
#         if result:
#             print(result.get("password"),user_login.Password)
#             data = verify_password(user_login.Password, result.get("password"))
#             print(data)

#             if verify_password(user_login.Password, result.get("password")):
#                 return{"mess": "loged in successfully"}
#             else:
#                 return{"not found"}
#     except Exception as e:
#         return{"error":str(e)}

from dbconnect import User_register_collection
from model.user_login_model import UserLogin
from bcryptEx import verify_password

async def user_login(login: UserLogin):

    query = {"Username": login.Username}

    result = await User_register_collection.find_one(query)

    if not result:
        return {"message": "User not found"}

    if verify_password(login.Password, result["Password"]):
        return {"message": "User Login Successful"}

    return {"message": "Wrong Password"}