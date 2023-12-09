from sqlalchemy import Column, Integer, Text, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship

from core.database import Base
from app.endpoint.models import Endpoint
from app.schema.models import Schema


class Response(Base):
    __tablename__ = 'response'

    id = Column(Integer, primary_key=True)
    endpoint_id = Column(Integer, ForeignKey('endpoint.id', ondelete='CASCADE'))
    response_schema_id = Column(Integer, ForeignKey('schema.id'))
    status_code = Column(Integer)
    description = Column(Text)
    created_at = Column(Integer)
    updated_at = Column(Integer)

    endpoint = relationship('Endpoint', back_populates='responses')
    response_schema = relationship('Schema')

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}