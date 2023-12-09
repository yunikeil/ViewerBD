from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, text
from sqlalchemy.orm import relationship

from core.database import Base
from app.api.models import Api


class Contact(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True)
    api_id = Column(Integer, ForeignKey('api.id', ondelete='CASCADE'), unique=False)
    name = Column(String(25))
    email = Column(String(50))
    url = Column(String(255))
    created_at = Column(Integer)
    updated_at = Column(Integer)

    api = relationship('Api', back_populates='contact')

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}