"""transaction

Revision ID: 7d2c52e91696
Revises: 4c3636527b79
Create Date: 2024-05-30 22:24:30.054164

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d2c52e91696'
down_revision: Union[str, None] = '4c3636527b79'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'transactions',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('User.id', ondelete='CASCADE'), nullable=False),
        sa.Column('credit', sa.Float, nullable=True),
        sa.Column('debit', sa.Float, nullable=True),
        sa.Column('date', sa.Date, nullable=False, server_default=sa.func.current_date()),
        sa.Column('time', sa.Time, nullable=False, server_default=sa.func.current_time()),
        sa.Column('account_balance', sa.Float, nullable=False),
    )
   


def downgrade() -> None:
    op.drop_table('transactions')
    # pass

