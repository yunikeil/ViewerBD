from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship

from core.database import Base


class Contact(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True)
    api_id = Column(Integer, ForeignKey('api.id', ondelete='CASCADE'), unique=True)
    name = Column(String(25))
    email = Column(String(50))
    url = Column(String(255))
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')

    api = relationship('Api', back_populates='contact')
