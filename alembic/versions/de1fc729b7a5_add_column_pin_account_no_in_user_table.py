"""add column PIN/Account_no in  user table

Revision ID: de1fc729b7a5
Revises: 7d2c52e91696
Create Date: 2024-05-31 12:23:42.457793

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'de1fc729b7a5'
down_revision: Union[str, None] = '7d2c52e91696'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add the PIN column as an INTEGER
    op.add_column('User', sa.Column('PIN', sa.Integer(), nullable=False))
    # Add the Account_no column as a STRING (VARCHAR(20))
    op.add_column('User', sa.Column('account_no', sa.String(length=14), nullable=False))


def downgrade() -> None:
    # Remove the PIN column
    op.drop_column('User', 'PIN')
    # Remove the Account_no column
    op.drop_column('User', 'account_no')
