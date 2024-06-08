"""add transaction_id column in transaction table

Revision ID: 93ddca302639
Revises: de1fc729b7a5
Create Date: 2024-05-31 14:49:13.322047

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93ddca302639'
down_revision: Union[str, None] = 'de1fc729b7a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add the transaction_id column as a STRING(10)
    op.add_column('transaction', sa.Column('transaction_id', sa.String(length=10), unique=True, nullable=True))



def downgrade() -> None:
     # Remove the transaction_id column
    op.drop_column('transaction', 'transaction_id')



   