# from dbconnect import Admin_register_collection
# from model.login_model import AdminLogin
# from bcryptEx import hash_password,verify_password
# from bson import ObjectId

# async def Admin_login(login : AdminLogin):
#     try:
#         query= {"Adminname": login.Adminname}
#         result= await Admin_register_collection.find_one(query)
#         print(result)
#         if result:
#             print(result.get("password"),login.Password)
#             data = verify_password(login.Password, result.get("password"))
#             print(data)

#             if verify_password(login.Password, result.get("password")):
#                 return{"mess": "loged in successfully"}
#             else:
#                 return{"not found"}
#     except Exception as e:
#         return{"error":str(e)}

from dbconnect import Admin_register_collection
from model.admin_login_model import AdminLogin
from bcryptEx import verify_password

async def admin_login(login: AdminLogin):

    query = {"Adminname": login.Adminname}

    result = await Admin_register_collection.find_one(query)

    if not result:
        return {"message": "Admin not found"}

    if verify_password(login.Password, result["Password"]):
        return {"message": "Admin Login Successful"}

    return {"message": "Wrong Password"}
