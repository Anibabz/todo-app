"""create todos table

Revision ID: 73d5c6cd8f41
Revises: 
Create Date: 2025-05-30 12:29:38.060985

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '73d5c6cd8f41'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
     op.execute("""
     create table todos(
         id bigserial primary key,
         name text,
         completed boolean not null default false
     )
     """)

def downgrade():
     op.execute("drop table todos;")