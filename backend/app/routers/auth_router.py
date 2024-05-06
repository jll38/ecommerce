from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

from app.schemas.user_schemas import UserBase, UserCreate, UserUpdate, UserResponse, LoginRequest, ErrorResponse
from app.services.user_service import UserServices



router = APIRouter()

# Registration route
@router.post("/register")
async def register(user: UserCreate):
    try:
        user_obj = await UserServices.register(user.dict())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return user_obj

# Login route
@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await UserServices.authenticate(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    access_token = UserServices.create_access_token(str(user.id), timedelta(minutes=UserServices.ACCESS_TOKEN_EXPIRE_MINUTES))
    return {"access_token": access_token, "token_type": "bearer"}

# Protected route (Reference for later)
@router.get("/protected")
async def protected_route(token: str = Depends(UserServices.get_current_user)):
    # Access protected data or perform protected actions
    return {"message": "This is a protected route"}

