from pydantic import BaseModel

class Auth_Model(BaseModel):
    username: str
    password: str
    is_admin: bool