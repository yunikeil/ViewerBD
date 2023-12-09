from sqlalchemy import Column, Integer, String, Enum, Boolean, Text, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship

from core.database import Base


class Parameter(Base):
    __tablename__ = 'parameter'

    id = Column(Integer, primary_key=True)
    endpoint_id = Column(Integer, ForeignKey('endpoint.id', ondelete='CASCADE'))
    name = Column(String(25))
    location = Column(Enum('COOCKIE', 'HEADER', 'PAYLOAD', name="parameter_locatioin"))
    type = Column(Enum('STR', 'INT', 'BOOL', 'FLOAT', name="parameter_type"))
    required = Column(Boolean)
    description = Column(Text)
    created_at = Column(Integer)
    updated_at = Column(Integer)

    endpoint = relationship('Endpoint', back_populates='parameters')

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}