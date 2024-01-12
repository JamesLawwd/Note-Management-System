
from sqlalchemy.orm import session
from  models.note import Note

# function that create a new note
def create_note(title,content, user_id):
    
        """
        Create a new note and add to database

        Args:
        title(str):title of the note
        content(str):content of the note
        user_id(int):the users id creating the note

        Returns:
        Note:The created Note object
        """
        try:
        # creating an instance
            new_note = Note(title=title, content=content, user_id=user_id)
            session.add(new_note)
            session.commit()
            return new_note
        except Exception as e:
            session.rollback()
            raise e
    
        finally:
            session.close()


# function to list the notes created
def list_notes(user_id):
    try:
        """
        List the notes for a specific user

        Args:
        user_id(int):The id of the user

        Returns:
        list[Notes]:A list of Note objects belonging to the user
        """
    

        notes = session.query(Note).filter_by(user_id=user_id).all()
        return notes
    finally:
        session.close()
   

# function to view a single note 
def view_note(note_id):
    try:
        """
        Retrieve a single note by its id

        Args:
        note_id(int):The id of the note

        Returns:
        Note: the note object if found or None if not found
        """
        note = session.query(Note).filter_by(id=note_id).first()
        return note
    finally:
        session.close()

# function to edit/update a note
def edit_note(note_id, title, content):
    try:
        """
        update the title,content of a note

        Args:
        note_id(int):The id of the note
        title(str):title of the note
        content(str):content of the note

        Returns:
        Note:the updated Note object
        """

        note = session.query(Note).filter_by(id=note_id).first()
        if note:
            note.title = title
            note.content = content
            session.commit()
        return note
    finally:
        session.close()

# function that deletes a note
def delete_note(note_id):
     try:
        """
        delete a note by its id

        Args:
        note_id(int):The id of the note

        Returns:
        bool:True if the note is deleted and False if not
        """
        note = session.query(Note).filter_by(id=note_id).first()
        if note:
            session.delete(note)
            session.commit()
            return True
        return False
     
     finally:
         session.close()
        
 

