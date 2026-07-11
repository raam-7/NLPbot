from sqlalchemy.orm import Session

from core.security import (
    hash_password,
    verify_password,
    create_access_token,
)
from models.user import User
from repositories.user_repository import UserRepository
from schemas.user import UserRegister


class AuthService:
    """
    Business logic for authentication.
    """

    def __init__(self, db: Session):
        self.user_repository = UserRepository(db)

    def register(self, user_data: UserRegister) -> User:
        """
        Register a new user.
        """

        # Check if email already exists
        existing_user = self.user_repository.get_by_email(
            user_data.email
        )

        if existing_user:
            raise ValueError("Email is already registered.")

        # Hash the password
        hashed_password = hash_password(user_data.password)

        # Create the user
        user = self.user_repository.create(
            full_name=user_data.full_name,
            email=user_data.email,
            password=hashed_password,
        )

        return user

    def login(self, email: str, password: str) -> str:
        """
        Authenticate a user and return a JWT access token.
        """

        # Find user by email
        user = self.user_repository.get_by_email(email)

        if not user:
            raise ValueError("Invalid email or password.")

        # Verify password
        if not verify_password(password, user.password):
            raise ValueError("Invalid email or password.")

        # Generate JWT token
        token = create_access_token(
            {
                "sub": str(user.id),
                "email": user.email,
            }
        )

        return token