from fastapi import APIRouter
from ..schemas.auth import LoginRequest, LoginResponse
from ..services.auth_service import login

router = APIRouter()

@router.post("/login", response_model=LoginResponse)
def auth_login(req: LoginRequest):
    return login(req.email)

