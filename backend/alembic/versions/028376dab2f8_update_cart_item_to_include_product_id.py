"""update cart_item to include product_id

Revision ID: 028376dab2f8
Revises: 8f76f37078c0
Create Date: 2024-05-10 20:42:15.559468

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func

# revision identifiers, used by Alembic.
revision: str = '028376dab2f8'
down_revision: Union[str, None] = '8f76f37078c0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add a new column 'product_id' to the 'cart_items' table
    op.add_column('cart_items', sa.Column('product_id', sa.Integer, sa.ForeignKey('products.id'), nullable=False))

    # Include default value for existing rows if applicable
    op.execute('UPDATE cart_items SET product_id = 1')


def downgrade() -> None:
    # Drop the 'product_id' column from the 'cart_items' table in the downgrade process
    op.drop_column('cart_items', 'product_id')
