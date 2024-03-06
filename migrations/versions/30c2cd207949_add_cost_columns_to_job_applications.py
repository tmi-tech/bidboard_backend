"""Add cost columns to job applications

Revision ID: 30c2cd207949
Revises: 29898ada16d4
Create Date: 2024-03-06 14:20:13.446362

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30c2cd207949'
down_revision: Union[str, None] = '29898ada16d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dob_job_applications', sa.Column('initial_cost', sa.Integer(), nullable=True))
    op.add_column('dob_job_applications', sa.Column('estimated_job_costs', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dob_job_applications', 'estimated_job_costs')
    op.drop_column('dob_job_applications', 'initial_cost')
    # ### end Alembic commands ###
