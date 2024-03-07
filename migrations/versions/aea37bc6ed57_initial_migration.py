"""Initial migration

Revision ID: aea37bc6ed57
Revises: 
Create Date: 2024-03-01 13:15:28.834564

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aea37bc6ed57'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bc_companies',
    sa.Column('id', sa.CHAR(32), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('bc_id', sa.String(length=24), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('data', sa.JSON(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('bc_id')
    )
    op.create_table('companies',
    sa.Column('id', sa.CHAR(32), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('dob_companies',
    sa.Column('id', sa.CHAR(32), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('name', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('bc_bids',
    sa.Column('id', sa.CHAR(32), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('company_id', sa.CHAR(32), nullable=False),
    sa.Column('bc_id', sa.String(length=24), nullable=False),
    sa.Column('bc_company_id', sa.CHAR(32), nullable=False),
    sa.Column('name', sa.Text(), nullable=False),
    sa.Column('location', sa.Text(), nullable=True),
    sa.Column('date_invited', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('is_archived', sa.Boolean(), nullable=False),
    sa.Column('data', sa.JSON(), nullable=False),
    sa.ForeignKeyConstraint(['bc_company_id'], ['bc_companies.id'], name='fk_bc_bids_bc_companies_id_bc_company_id'),
    sa.ForeignKeyConstraint(['company_id'], ['companies.id'], name='fk_bc_bids_companies_id_company_id'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('company_id', 'bc_id', name='uc_bc_bids_company_id_bc_id')
    )
    op.create_table('dob_approved_permits',
    sa.Column('id', sa.CHAR(32), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('job_filing_number', sa.String(length=24), nullable=False),
    sa.Column('filing_reason', sa.String(length=100), nullable=False),
    sa.Column('work_on_floor', sa.Text(), nullable=False),
    sa.Column('work_type', sa.String(length=100), nullable=False),
    sa.Column('applicant_business_id', sa.CHAR(32), nullable=False),
    sa.Column('address', sa.Text(), nullable=False),
    sa.Column('data', sa.JSON(), nullable=False),
    sa.ForeignKeyConstraint(['applicant_business_id'], ['dob_companies.id'], name='fk_dob_approved_permits_dob_companies_id_applicant_business_id'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dob_approved_permits')
    op.drop_table('bc_bids')
    op.drop_table('dob_companies')
    op.drop_table('companies')
    op.drop_table('bc_companies')
    # ### end Alembic commands ###