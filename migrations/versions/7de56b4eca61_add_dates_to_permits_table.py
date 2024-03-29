"""Add dates to permits table

Revision ID: 7de56b4eca61
Revises: c76dd7e76281
Create Date: 2024-03-01 14:05:42.938579

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7de56b4eca61'
down_revision: Union[str, None] = 'c76dd7e76281'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dob_approved_permits', sa.Column('approved_date', sa.DateTime(), nullable=True))
    op.add_column('dob_approved_permits', sa.Column('issued_date', sa.DateTime(), nullable=True))
    op.drop_constraint('uc_dob_approved_permit_pk', 'dob_approved_permits', type_='unique')
    op.create_unique_constraint('uc_dob_approved_permit_pk', 'dob_approved_permits', ['job_filing_number', 'filing_reason', 'work_type', 'applicant_business_id', 'issued_date'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uc_dob_approved_permit_pk', 'dob_approved_permits', type_='unique')
    op.create_unique_constraint('uc_dob_approved_permit_pk', 'dob_approved_permits', ['job_filing_number', 'filing_reason', 'work_type', 'applicant_business_id'])
    op.drop_column('dob_approved_permits', 'issued_date')
    op.drop_column('dob_approved_permits', 'approved_date')
    # ### end Alembic commands ###
