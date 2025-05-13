from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import UserCreate, UserOut
from app.schemas.token import Token
from app.services.auth_service import AuthService

router = APIRouter()
service = AuthService()

@router.post('/register', response_model=UserOut)
async def register(user: UserCreate):
    return await service.register(user)

@router.post('/token', response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    token = await service.authenticate_user(form_data.username, form_data.password)
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')
    return token