# creating the cli commands
import click
from database.config import Base,engine
from notes.note_manager import(create_note,list_notes, view_note,edit_note,delete_note) 
from tags.tag_manager import (create_tag,list_tags,view_tag,edit_tag,delete_tag)
from Users.user_manager import(create_user, list_users_cmd)
from association.associate_manager import (insert_association,delete_association)

# Define custom colors
SUCCESS_COLOR = 'green'
ERROR_COLOR = 'red'
INFO_COLOR = 'blue'

# create a dictionary for users and notes
users = {}
notes ={}
tags ={}

@click.group
def menu():
    """Note Management Menu"""
    pass

# USER MANAGEMENT

@menu.command()
@click.option('--name', prompt='Enter your name', help='Your name')
def createuser(name):
    """Create a new user"""
    user_created = create_user(name)
    if user_created:
        click.echo(click.style(f'User {name} created', fg=SUCCESS_COLOR))
    else:
        click.echo(click.style(f'User {name} already exists', fg=ERROR_COLOR))

@menu.command()
def list():
    """List all users"""
    users_list = list_users_cmd()
    if users_list:
        users_str = "[" + ", ".join(users_list) + "]"
        click.echo(click.style(users_str, fg=INFO_COLOR))
         
    else:
         click.echo(click.style('User not found', fg=ERROR_COLOR))



#  MANAGEMENT
@menu.command()
@click.option('--title', prompt = 'Enter title of the note', help ='Title of the note')
@click.option('--content', prompt = 'Enter content of the note', help ='content of the note')
@click.option('--user_id', type=int, prompt = 'User ID', help ='User ID creating')
def createnote(title, content, user_id):
    """Create a new note"""
    # creating an instance
    new_notes = create_note(title, content, user_id)
    click.echo(click.style(f'Note created with ID: {new_notes.id}', fg=SUCCESS_COLOR))

@menu.command()
@click.option('--user_id', type=int, prompt='Enter User ID', help= 'User ID to list')
def listnotes(user_id):
    """List all notes for a specific user"""
    notes = list_notes(user_id)
    if notes:
        notes_dict = {f'ID: {note.id}': note.title for note in notes}
        notes_str = "{" + ", ".join([f"{key}: {value}" for key, value in notes_dict.items()]) + "}"
        click.echo(click.style(notes_str, fg=INFO_COLOR))
    else:
        click.echo(click.style('No notes found for this user', fg=ERROR_COLOR))

@menu.command()
@click.option('--note_id', type=int, prompt='Enter Note ID', help= 'Note ID to view')
def viewnote(note_id):
    """View a specific note by its id"""
    note = view_note(note_id)
    if note:
         note_tuple = (note.id, note.title, note.content)
         click.echo(click.style(str(note_tuple), fg=INFO_COLOR))
    else:
        click.echo(click.style('Note not found.', fg=ERROR_COLOR))

@menu.command()
@click.option('--note_id', type=int, prompt = 'Note Id', help ='Note ID to edit')
@click.option('--title', prompt = 'Enter title of the note', help ='Title of the note')
@click.option('--content', prompt = 'Enter content of the note', help ='content of the note')
def editnote(note_id, title, content):
    """Update a specific note by its id"""
    edited_note = edit_note(note_id, title, content)
    if edited_note:
        click.echo(click.style(f'Note Edited: ID:{edited_note.id}, Title: {edited_note.title}', fg=SUCCESS_COLOR))
    else:
        click.echo(click.style('Note not found.', fg=ERROR_COLOR))



@menu.command()
@click.option('--note_id', type=int, prompt = 'Note Id', help ='Note ID to edit')
def deletenote(note_id):
    """Delete note by its id"""
    if delete_note(note_id):
        click.echo(click.style('Note deleted', fg=SUCCESS_COLOR))
    else:
        click.echo(click.style('Note not found.', fg=ERROR_COLOR))


# TAG MANAGEMENT

@menu.command()
@click.option('--name', prompt='Tag name', help='Name of Tag')
def createtag(name):
    """Create a new tag"""
    new_tag = create_tag(name)
    click.echo(f'Tag created with id : {new_tag.id}', fg=SUCCESS_COLOR)

@menu.command()
@click.option('--tag_id', type=int, prompt = 'Tag Id', help ='Tag ID to view')
def viewtag(tag_id):
    """View a specific tag"""
    tag = view_tag(tag_id)
    if tag:
        click.echo(click.style(f'ID: {tag.id}, Name: {tag.name}', fg=INFO_COLOR))

    else:
        click.echo(click.style("Tag Not Found", fg=ERROR_COLOR))

@menu.command()
def listtag():
    """List all tags"""
    tags = list_tags()
    if tags:
        for tag in tags:
            click.echo(click.style(f'ID: {tag.id}, Name:{tag.name}', fg=INFO_COLOR))
    else:
        click.echo(click.style("Tag Not Found", fg=ERROR_COLOR))

@menu.command()
@click.option('--tag_id', type=int, prompt = 'Tag Id', help ='Tag ID to view')
@click.option('--name', prompt='Tag name', help='Name of Tag')
def edittag(tag_id, name):
    """Edit by its id"""
    edited_tag = edit_tag(tag_id, name)
    if edited_tag:
         click.echo(click.style(f'ID: {edited_tag.id}, Name:{edited_tag.name}', fg=SUCCESS_COLOR))
    else:
        click.echo(click.style("Tag Not Found", fg=ERROR_COLOR))

@menu.command()
@click.option('--tag_id', type=int, prompt = 'Tag Id', help ='Tag ID to view')

def deletetag(tag_id):
    """Delete a specific tag by id"""
    if delete_tag(tag_id):
           click.echo(click.style('Tag deleted', fg=SUCCESS_COLOR))
    else:
        click.echo(click.style('Tag not found.', fg=ERROR_COLOR))


# ASSOCIATION MANAGEMENT
@menu.command()
@click.option('--note_id', type=int, prompt = 'Note ID', help='Note Id to associate')
@click.option('--tag_id', type=int, prompt = 'Tag ID', help='Tag Id to associate')

def associate(note_id, tag_id):
    """Associationg a note with a tag(insert)"""
    insert_association(note_id, tag_id)
    click.echo(click.style('Association created successfully', fg=SUCCESS_COLOR))

@menu.command()
@click.option('--note_id', type=int, prompt = 'Note ID', help='Note Id to associate')
@click.option('--tag_id', type=int, prompt = 'Tag ID', help='Tag Id to associate')
def disassociate(note_id, tag_id):
    """Dissociates a note with a tag"""
    delete_association(note_id, tag_id)
    click.echo(click.style('Association deleted successfully', fg=SUCCESS_COLOR))


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    while True:
      menu()