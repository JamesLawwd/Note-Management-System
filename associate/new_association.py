from sqlalchemy import Column,Integer,ForeignKey,Table
from database.config import Base

# create an association table between note and tag
association_table = Table(
    'new_association', # Table name
    Base.metadata,
    Column('note_id', Integer, ForeignKey('notes.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)
