from pydantic import BaseModel

class UserRegister(BaseModel):
    Username: str
    Email: str
    Password: str