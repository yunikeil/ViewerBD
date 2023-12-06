from sqlalchemy import Column, Integer, String, Text, TIMESTAMP

from core.database import Base


class Api(Base):
    __tablename__ = 'api'

    id = Column(Integer, primary_key=True)
    title = Column(String(25))
    version = Column(String(8))
    description = Column(Text)
    base_url = Column(String(25))
    created_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP')
    updated_at = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP', onupdate='CURRENT_TIMESTAMP')
