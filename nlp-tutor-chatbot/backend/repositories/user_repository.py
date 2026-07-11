from sqlalchemy import select
from sqlalchemy.orm import Session

from models.user import User


class UserRepository:
    """
    Handles all database operations related to users.
    """

    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, email: str) -> User | None:
        """
        Get a user by email.
        """
        statement = select(User).where(User.email == email)

        return self.db.execute(statement).scalar_one_or_none()

    def create(
        self,
        full_name: str,
        email: str,
        password: str,
    ) -> User:
        """
        Create a new user.
        """

        user = User(
            full_name=full_name,
            email=email,
            password=password,
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user