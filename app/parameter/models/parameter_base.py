from sqlalchemy import Column, Integer, String, Enum, Boolean, Text, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship

from core.database import Base


class Parameter(Base):
    __tablename__ = 'parameter'

    id = Column(Integer, primary_key=True)
    endpoint_id = Column(Integer, ForeignKey('endpoint.id', ondelete='CASCADE'))
    name = Column(String(25))
    location = Column(Enum('COOKIE', 'HEADER', 'PAYLOAD'))
    type = Column(Enum('STR', 'INT', 'BOOL', 'FLOAT'))
    required = Column(Boolean)
    description = Column(Text)
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'))

    endpoint = relationship('Endpoint', back_populates='parameters')
