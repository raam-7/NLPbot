from sqlalchemy.orm import Session

from core.security import hash_password
from repositories.user_repository import UserRepository
from schemas.user import UserRegister
from models.user import User


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

        existing_user = self.user_repository.get_by_email(
            user_data.email
        )

        if existing_user:
            raise ValueError(
                "Email is already registered."
            )

        hashed_password = hash_password(
            user_data.password
        )

        user = self.user_repository.create(
            full_name=user_data.full_name,
            email=user_data.email,
            password=hashed_password,
        )

        return user