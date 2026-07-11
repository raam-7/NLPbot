from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from database.session import get_db
from schemas.user import (
    UserRegister,
    UserResponse,
    UserLogin,
    Token,
)
from services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    user: UserRegister,
    db: Session = Depends(get_db),
):
    """
    Register a new user.
    """
    auth_service = AuthService(db)

    try:
        return auth_service.register(user)

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.post(
    "/login",
    response_model=Token,
)
def login(
    user: UserLogin,
    db: Session = Depends(get_db),
):
    """
    Login user and return JWT token.
    """
    auth_service = AuthService(db)

    try:
        token = auth_service.login(
            email=user.email,
            password=user.password,
        )

        return Token(
            access_token=token,
            token_type="bearer",
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
        )