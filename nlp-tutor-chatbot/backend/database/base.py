from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Import all models here
from models.user import User
from models.conversation import Conversation
from models.message import Message