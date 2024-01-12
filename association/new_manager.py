from models.config import session
from associate.new_association import association_table
from sqlalchemy import insert,delete,select

def insert_association(note_id, tag_id):
    """Insert an association btwn note and tag"""
    try:
        insert_statement = association_table.insert().values(note_id=note_id, tag_id=tag_id)
        session.execute(insert_statement)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

def delete_association(note_id, tag_id):
    """Delete association between note and tag"""
    try:
        delete_statement = association_table.delete().where((association_table.c.note_id == note_id) & (association_table.c.tag_id == tag_id))
        session.execute(delete_statement)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

