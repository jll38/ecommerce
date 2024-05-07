"""add created_at to product

Revision ID: 73a533f1f156
Revises: aeabc792fec0
Create Date: 2024-05-06 22:35:15.444429

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = '73a533f1f156'
down_revision: Union[str, None] = 'aeabc792fec0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('products', sa.Column('created_at', sa.DateTime(timezone=True), server_default=func.now()))


def downgrade() -> None:
    op.drop_column('products', 'created_at')
