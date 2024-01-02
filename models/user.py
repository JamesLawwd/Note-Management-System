
# create a user table..
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from database.config import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    # define a relationship with notes
    notes = relationship('Note', back_populates='author')

    def __init__(self, name):
        self.name = name
