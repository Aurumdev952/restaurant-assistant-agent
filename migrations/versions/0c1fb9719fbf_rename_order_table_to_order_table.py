"""rename order table to order_table

Revision ID: 0c1fb9719fbf
Revises: f817bbdd0a3e
Create Date: 2025-01-21 18:36:17.266990

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0c1fb9719fbf'
down_revision: Union[str, None] = 'f817bbdd0a3e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.rename_table('order', 'orders')

def downgrade():
    op.rename_table('orders', 'order')

