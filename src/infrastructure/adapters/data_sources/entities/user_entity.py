import os
import sys
import uuid

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from sqlalchemy import Column, String
from infrastructure.adapters.data_sources.db_config import Base, db

class UserEntity(Base):
    __tablename__ = 'users'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), unique=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    name = Column(String(255))
    surname = Column(String(255))

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'name': self.name,
            'surname': self.surname
        }

Base.metadata.create_all(bind=db.get_bind())