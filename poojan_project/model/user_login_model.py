from pydantic import BaseModel

class UserLogin(BaseModel):
    Username: str
    Password: str

    # pnnncnb c