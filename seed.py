from sqlalchemy.orm import Session
from models.user import User
from models.note import Note
from models.tag import Tag
from associate.new_association import association_table
from models.config import engine, Base

# Function to seed the database with initial data
def seed_data():
    # Create database tables
    Base.metadata.create_all(bind=engine)

    # Create a session bound to the engine
    with Session(bind=engine) as session:
        try:
            # Clear existing data
            session.query(User).delete()
            session.query(Note).delete()
            session.query(Tag).delete()
            session.execute(association_table.delete())

            # Seed users
            user1 = User(name="John Doe")
            user2 = User(name="Jane Doe")
            session.add_all([user1, user2])
            session.commit()

            # Seed notes
            note1 = Note(title="First Note", content="This is the content of the first note.", user_id=user1.id)
            note2 = Note(title="Second Note", content="This is the content of the second note.", user_id=user2.id)
            session.add_all([note1, note2])
            session.commit()

            # Seed tags
            tag1 = Tag(name="Important")
            tag2 = Tag(name="Personal")
            tag3 = Tag(name="Work")
            session.add_all([tag1, tag2, tag3])
            session.commit()

            # Associate notes with tags
            session.execute(association_table.insert().values(note_id=note1.id, tag_id=tag1.id))
            session.execute(association_table.insert().values(note_id=note1.id, tag_id=tag2.id))
            session.execute(association_table.insert().values(note_id=note2.id, tag_id=tag3.id))
            session.commit()

        except Exception as e:
            print(f"Error: {e}")
            session.rollback()

if __name__ == "__main__":
    seed_data()
