"""Move textract filename to unique image

Revision ID: e2ccbb9a53f4
Revises: 0a6d9eda457b
Create Date: 2024-05-02 12:33:29.599900

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e2ccbb9a53f4'
down_revision: Union[str, None] = '0a6d9eda457b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('unique_image_annotations', 'textract_filename')
    op.add_column('unique_images', sa.Column('textract_filename', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('unique_images', 'textract_filename')
    op.add_column('unique_image_annotations', sa.Column('textract_filename', sa.VARCHAR(length=200), autoincrement=False, nullable=True))
    # ### end Alembic commands ###