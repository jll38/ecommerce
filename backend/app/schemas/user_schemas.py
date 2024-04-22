from builtins import ValueError, any, bool, str
from pydantic import BaseModel, EmailStr, Field, validator, root_validator
from typing import Optional, List
from datetime import datetime
from enum import Enum
import uuid

class UserBase(BaseModel):
    email: EmailStr = Field(..., example="john.doe@exmaple.com")
    first_name: Optional[str] = Field(None, example="John")
    last_name: Optional[str] = Field(None, example="Doe")
    is_active: Optional[bool] = Field(None, example = True)

    class Config:
        from_attributes = True

class UserCreate(UserBase):
    email: EmailStr = Field(..., example="john.doe@example.com")
    password: str = Field(..., example="SecurePassword&*1234")

class UserUpdate(UserBase):
    email: EmailStr = Field(..., example="john.doe@example.com")
    first_name: Optional[str] = Field(None, example="John")
    last_name: Optional[str] = Field(None, example="Doe")
    is_active: Optional[bool] = Field(None, example = True)

    @root_validator(pre=True)
    def check_at_least_one_value(cls, values):
        if not any(values.values()):
            raise ValueError("At least one field must be provided for update")
        return values
    
class UserResponse(UserBase):
    id: uuid.UUID = Field(..., example=uuid.uuid4())
    email: EmailStr = Field(..., example="john.doe@example.com")
    first_name: Optional[str] = Field(None, min_length=3, pattern=r'^[\w-]+$', example="John")    
    last_name: Optional[str] = Field(None, min_length=3, pattern=r'^[\w-]+$', example="Doe")    

class LoginRequest(BaseModel):
    email: str = Field(..., example="john.doe@example.com")
    password: str = Field(..., example="SecurePassword&*1234")

class ErrorResponse(BaseModel):
    error: str = Field(..., example="Not Found")
    details: Optional[str] = Field(None, example="The requested resource was not found.")