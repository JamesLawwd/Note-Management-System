from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.user import User
from models.note import Note
from models.tag import Tag
from associate.new_association import association_table

# Database configuration
engine = create_engine('sqlite:///note.db')
Session = sessionmaker(bind=engine)
session = Session()

# Function to seed the database with sample data
def seed_data():
    # Create users
    user1 = User(name="John Doe")
    user2 = User(name="Jane Smith")
    session.add_all([user1, user2])
    session.commit()

    # Create tags
    tag1 = Tag(name="Personal")
    tag2 = Tag(name="Work")
    session.add([tag1, tag2]
                )
    session.commit()

    # Create notes and associate with users and tags
    note1 = Note(title="Note 1", content="Content for Note 1", user_id=user1.id)
    note2 = Note(title="Note 2", content="Content for Note 2", user_id=user2.id)

    note1.tags.extend([tag1, tag2])
    note2.tags.append(tag2)

    session.add_all([note1, note2])
    session.commit()

if __name__ == "__main__":
    # Calling the seed_data function to populate the database
    seed_data()
    print("Data seeding completed.")
