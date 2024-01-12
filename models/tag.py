from sqlalchemy import Column,Integer,String,ForeignKey,Table
from sqlalchemy.orm import relationship
from .config import Base
from associate.new_association import association_table



class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True )
    name = Column(String, unique=True, index=True)

    # define a relationship for the note and tag
    notes = relationship('Note', secondary= association_table, back_populates='tags')
