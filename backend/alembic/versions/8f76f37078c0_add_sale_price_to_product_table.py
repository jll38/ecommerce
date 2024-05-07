"""add sale_price to product table

Revision ID: 8f76f37078c0
Revises: 73a533f1f156
Create Date: 2024-05-07 18:43:35.647485

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy import Float
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '8f76f37078c0'
down_revision: Union[str, None] = '73a533f1f156'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('products', sa.Column('sale_price', Float, nullable=True))


def downgrade() -> None:
    op.drop_column('products', 'sale_price')
