from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship

from core.database import Base


class Response(Base):
    __tablename__ = 'response'

    id = Column(Integer, primary_key=True)
    endpoint_id = Column(Integer, ForeignKey('endpoint.id', ondelete='CASCADE'))
    response_schema_id = Column(Integer, ForeignKey('schema.id'))
    status_code = Column(Integer)
    description = Column(Text)
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'))

    endpoint = relationship('Endpoint', back_populates='responses')
    response_schema = relationship('Schema')
