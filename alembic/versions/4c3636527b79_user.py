"""user

Revision ID: 4c3636527b79
Revises: 
Create Date: 2024-05-30 22:12:33.158051

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import BIGINT


# revision identifiers, used by Alembic.
revision: str = '4c3636527b79'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'User',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(100), nullable=False),
        sa.Column('password', sa.String(100), nullable=False),
        sa.Column('is_admin', sa.Boolean, nullable=False, default=False),
        sa.Column('balance', sa.Float, nullable=False, default=0.0),
        sa.Column('PIN', sa.Integer, nullable=False),
        sa.Column('account_no', sa.Integer, nullable=False),
    )


def downgrade() -> None:
    op.drop_table('User')
    # op.drop_column('User', 'account_no')
