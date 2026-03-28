from pydantic import BaseModel

class UserMasterModel(BaseModel):
    Userid: str
    Name: str
    Email: str
    Password: str
    Mobile: int
    Age: int
    Gender: str
    Weight: int
    Height: int
    Exercise: str