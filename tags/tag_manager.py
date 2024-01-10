from database.config import session
from models.tag import Tag

def create_tag(name):
    try:
        """
        Create a new tag and add to the database

        Args:
        name(str):Name of the tag

        Return:
        Tag:Tag object
        
        """
        # create an instance
        new_tag = Tag(name=name)
        session.add(new_tag)
        session.commit()
        return new_tag
    
    finally:
        session.close()

def list_tags():
    try:
        """
        List all the tags in the database

        Returns:
        list[Tag]:A list of tag objects

        """
        tags = session.query(Tag).all()
        return tags
    
    finally:
        session.close()

def view_tag(tag_id):
    try:
        """
        Retrieve a specific tag by id

        Args:
        tag_id(id):Id of the tag

        Return:
        Tag:Tag object if found, none if not found
        
        """
        tag = session.query(Tag).filter_by(id=tag_id).first
        return tag
    
    finally:
        session.close()

def edit_tag(tag_id, name):
     try:
        """
        Update the name of a tag by its ID.

        Args:
        tag_id (int): The ID of the tag.
        name (str): New name for the tag.

        Returns:
        Tag: The updated Tag object.
        """
        tag = session.query(Tag).filter_by(id=tag_id).first()
        if tag:
            tag.name = name
            session.commit()
        return tag
     
     finally:
         session.close()

def delete_tag(tag_id):
     try:
        """
        Delete a tag by its ID.

        Args:
        tag_id (int): The ID of the tag.
        

        Returns:
        bool: True/False.
        """
        tag = session.query(Tag).filter_by(id=tag_id).first()
        if tag:
            session.delete(tag)
            session.commit()
            return True
        return False
     
     finally:
         session.commit()
