from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from associate.new_association import association_table
from database.config import Base

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer,primary_key=True, index=True)
    title = Column(String,index=True)
    content = Column(String)

    # Define a relationship with the user
    user_id = Column(Integer, ForeignKey('users.id'))
    author = relationship('User', back_populates='notes')
    
    # Define a relationship with tag
    tags = relationship('Tag', secondary= association_table, back_populates='notes')

    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id