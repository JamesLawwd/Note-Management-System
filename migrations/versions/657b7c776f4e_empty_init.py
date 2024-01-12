"""Empty init

Revision ID: 657b7c776f4e
Revises: 5e6db21f62a1
Create Date: 2024-01-11 10:05:39.947665

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '657b7c776f4e'
down_revision: Union[str, None] = '5e6db21f62a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
