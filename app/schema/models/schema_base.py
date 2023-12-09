from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

from core.database import Base
from app.api.models import Api


class Schema(Base):
    __tablename__ = 'schema'

    id = Column(Integer, primary_key=True)
    api_id = Column(Integer, ForeignKey('api.id', ondelete='CASCADE'))
    name = Column(String(25))
    description = Column(Text)
    file_path = Column(String(255))

    api = relationship('Api', back_populates='schemas')

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}