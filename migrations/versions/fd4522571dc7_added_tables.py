"""Added tables

Revision ID: fd4522571dc7
Revises: 657b7c776f4e
Create Date: 2024-01-11 10:06:38.753290

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fd4522571dc7'
down_revision: Union[str, None] = '657b7c776f4e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tags_name'), 'tags', ['name'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_name'), 'users', ['name'], unique=True)
    op.create_table('notes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_notes_user_id_users')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_notes_title'), 'notes', ['title'], unique=False)
    op.create_table('new_association',
    sa.Column('note_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['note_id'], ['notes.id'], name=op.f('fk_new_association_note_id_notes')),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], name=op.f('fk_new_association_tag_id_tags'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('new_association')
    op.drop_index(op.f('ix_notes_title'), table_name='notes')
    op.drop_table('notes')
    op.drop_index(op.f('ix_users_name'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_tags_name'), table_name='tags')
    op.drop_table('tags')
    # ### end Alembic commands ###