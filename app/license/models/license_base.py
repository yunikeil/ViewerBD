from sqlalchemy import Column, Integer, String, ForeignKey, text
from sqlalchemy.orm import relationship

from core.database import Base
from app.api.models.api_base import Api

class License(Base):
    __tablename__ = 'license'

    id = Column(Integer, primary_key=True)
    api_id = Column(Integer, ForeignKey('api.id', ondelete='CASCADE'), unique=True)
    name = Column(String(255))
    url = Column(String(255))
    created_at = Column(Integer)
    updated_at = Column(Integer)

    api = relationship('Api', back_populates='license')

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}