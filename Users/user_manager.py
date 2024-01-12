#  Defining user methods
from models.user import User #  Import user model
from sqlalchemy.orm import session

def create_user(name):
    try:
        """
         Create a new user and add to the database

         Args:
         username(str):username to vreate

         Returns:
         User:Created user object
         """
        # create an instance
        user = User(name=name)
        session.add(user)
        session.commit()
        return user
    
    finally:
        session.close()

# list all the customers
def list_users_cmd():
     try:
          users = session.query(User).all()
          user_list = [user.name for user in users]
          return user_list
     finally:
          session.close()