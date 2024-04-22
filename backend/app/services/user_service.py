from datetime import datetime, timedelta
from typing import Optional
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

from jose import jwt
from passlib.context import CryptContext

from app.models.sqlalchemy import User

# Initialize components
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class UserServices:
    @staticmethod
    async def register(user_data: dict) -> User:
        existing_user = await User.find_one({"email": user_data["email"]})
        if existing_user:
            raise ValueError("Email aready registered")

        hashed_password = pwd_context.hash(user_data["password"])
        user_obj = User(email=user_data["email"],
                        hashed_password=hashed_password)
        await user_obj.insert()
        return user_obj

    @staticmethod
    async def authenticate(email: str, password: str) -> Optional[User]:
        # Find user by email
        user = await User.find_one({"email": email})
        if not user:
            return None

        # Verify password
        if not pwd_context.verify(password, user.hashed_password):
            return None

        return user

    @staticmethod
    def create_access_token(user_id: str, expires_delta: timedelta) -> str:
        data = {"sub": user_id}
        expire = datetime.utcnow() + expires_delta
        data.update({"exp": expire})
        encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    async def get_current_user(token: str = Depends(oauth2_scheme)):
        try:
            payload = jwt.decode(
                token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id = payload.get("sub")
            if user_id is None:
                raise HTTPException(status_code=401, detail="Invalid token")
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid token")

        user = await User.find_one({"_id": user_id})
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return user
