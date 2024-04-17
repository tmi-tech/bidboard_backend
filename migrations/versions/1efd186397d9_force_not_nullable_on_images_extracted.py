"""Force not nullable on images extracted

Revision ID: 1efd186397d9
Revises: 3da186e738ab
Create Date: 2024-04-17 12:45:21.106213

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1efd186397d9'
down_revision: Union[str, None] = '3da186e738ab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bc_bid_files', 'images_extracted',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('bc_bid_files', 'images_extracted',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###