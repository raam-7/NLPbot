from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

# Import models so SQLAlchemy registers relationships before first query.
from models.conversation import Conversation
from models.message import Message
from models.user import User

# Create the SQLAlchemy engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.SQL_ECHO,
)

# Create a session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_db():
    """
    Dependency that provides a database session.
    Automatically closes the session after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
