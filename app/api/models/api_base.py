from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, text
from sqlalchemy.orm import relationship

from core.database import Base


class Api(Base):
    __tablename__ = 'api'

    id = Column(Integer, primary_key=True)
    title = Column(String(25))
    version = Column(String(8))
    description = Column(Text)
    base_url = Column(String(25))
    created_at = Column(Integer)
    updated_at = Column(Integer)
    
    contact = relationship('Contact', back_populates='api')
    license = relationship('License', back_populates='api')
    endpoints = relationship("Endpoint", back_populates="api")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}