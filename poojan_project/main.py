from fastapi import FastAPI
from router.admin_register_router import AdminRegisterRouter
from router.admin_login_router import AdminLoginRouter
from router.user_register_router import UserRegisterRouter
from router.user_login_router import UserLoginRouter
from router.exercisemaster_router import exerciseMasterRouter
from router.gymmaster_router import gymMasterRouter
from router.User_master_router import user_master_router
from router.assignexercise_router import assignrouter


app = FastAPI(title="GYM Management API", description="Welcome to the GYM Management API")
app.include_router(AdminRegisterRouter)
app.include_router(AdminLoginRouter)
app.include_router(UserRegisterRouter)
app.include_router(UserLoginRouter)
app.include_router(exerciseMasterRouter)
app.include_router(gymMasterRouter)
app.include_router(user_master_router)
app.include_router(assignrouter)

async def root():
    return {"message": "Welcome to the GYM Management API"}
