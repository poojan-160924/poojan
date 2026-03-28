from pydantic import BaseModel

class AdminRegister(BaseModel):
    Adminname: str
    Email: str
    Password: str