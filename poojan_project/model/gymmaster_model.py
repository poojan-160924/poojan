from pydantic import BaseModel

class gymMaster(BaseModel):
    Srno: str
    Name: str
    Email: str
    mobile: int
    PTC: int
    Address: str
    Password: str