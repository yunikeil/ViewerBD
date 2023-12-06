from sqlalchemy import Boolean, Column, Integer, String
from core.database import Base


class Api(Base):
    __tablename__ = 'api'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
