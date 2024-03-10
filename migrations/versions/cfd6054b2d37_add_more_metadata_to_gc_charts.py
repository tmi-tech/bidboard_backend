"""Add more metadata to gc_charts

Revision ID: cfd6054b2d37
Revises: c8f16be92636
Create Date: 2024-03-07 22:06:39.555576

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cfd6054b2d37'
down_revision: Union[str, None] = 'c8f16be92636'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('gc_charts', sa.Column('path', sa.String(length=500), nullable=True))
    op.add_column('gc_charts', sa.Column('parent_gc_chart_id', sa.CHAR(32), nullable=True))
    op.add_column('gc_charts', sa.Column('previous_gc_chart_id', sa.CHAR(32), nullable=True))
    op.create_unique_constraint(None, 'gc_charts', ['path'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'gc_charts', type_='unique')
    op.drop_column('gc_charts', 'previous_gc_chart_id')
    op.drop_column('gc_charts', 'parent_gc_chart_id')
    op.drop_column('gc_charts', 'path')
    # ### end Alembic commands ###