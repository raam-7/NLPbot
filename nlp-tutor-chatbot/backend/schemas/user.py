from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserRegister(BaseModel):
    full_name: str = Field(
        min_length=3,
        max_length=100,
        description="Full name of the user",
    )

    email: EmailStr

    password: str = Field(
        min_length=6,
        max_length=100,
        description="User password",
    )


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    is_active: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"