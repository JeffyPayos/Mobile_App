from pydantic import BaseModel

class LoginRequest(BaseModel):
    email: str

class LoginResponse(BaseModel):
    token: str
    user_id: str
