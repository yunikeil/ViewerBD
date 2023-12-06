from sqlalchemy import Column, Integer, String, Text, Enum, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship

from core.database import Base


class Endpoint(Base):
    __tablename__ = 'endpoint'

    id = Column(Integer, primary_key=True)
    api_id = Column(Integer, ForeignKey('api.id', ondelete='CASCADE'))
    request_schema_id = Column(Integer, ForeignKey('schema.id'))
    path = Column(String(255))
    method = Column(Enum('POST', 'GET', 'PUT', 'DELETE'))
    summary = Column(String(255))
    description = Column(Text)
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')

    api = relationship('Api', back_populates='endpoints')
    request_schema = relationship('Schema')
