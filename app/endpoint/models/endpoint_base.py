from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey
from sqlalchemy.orm import relationship

from core.database import Base
from app.api.models import Api
from app.schema.models import Schema


class Endpoint(Base):
    __tablename__ = 'endpoint'

    id = Column(Integer, primary_key=True)
    api_id = Column(Integer, ForeignKey('api.id', ondelete='CASCADE'))
    request_schema_id = Column(Integer, ForeignKey('schema.id'))
    path = Column(String(255))
    method = Column(Enum('POST', 'GET', 'PUT', 'DELETE', name="endpoint_methods"))
    summary = Column(String(255))
    description = Column(Text)
    created_at = Column(Integer)
    updated_at = Column(Integer)

    api = relationship('Api', back_populates='endpoints')
    request_schema = relationship('Schema')
    
    parameters = relationship("Parameter", back_populates="endpoint")

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}