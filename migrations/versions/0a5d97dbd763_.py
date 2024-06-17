"""empty message

Revision ID: 0a5d97dbd763
Revises: 53e0e75eabeb
Create Date: 2024-06-12 12:42:00.893241

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0a5d97dbd763'
down_revision: Union[str, None] = '53e0e75eabeb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('reviews', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('reviews', 'salon_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('reviews', 'score',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('reviews', 'score',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('reviews', 'salon_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('reviews', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
