from pydantic import BaseModel

class AdminLogin(BaseModel):
    Adminname: str
    Password: str