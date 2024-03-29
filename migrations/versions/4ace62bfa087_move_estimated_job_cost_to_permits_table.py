"""Move estimated job cost to permits table

Revision ID: 4ace62bfa087
Revises: 136132577fdc
Create Date: 2024-03-06 15:39:04.276794

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4ace62bfa087'
down_revision: Union[str, None] = '136132577fdc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dob_approved_permits', sa.Column('estimated_job_costs', sa.DECIMAL(precision=12, scale=2), nullable=True))
    op.drop_column('dob_job_applications', 'estimated_job_costs')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dob_job_applications', sa.Column('estimated_job_costs', sa.NUMERIC(precision=12, scale=2), autoincrement=False, nullable=True))
    op.drop_column('dob_approved_permits', 'estimated_job_costs')
    # ### end Alembic commands ###
