"""empty message

Revision ID: 3e9a98f716aa
Revises: cfbb29450cf1
Create Date: 2024-05-23 14:26:57.238685

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e9a98f716aa'
down_revision: Union[str, None] = 'cfbb29450cf1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('id', sa.String(length=255), nullable=False),
    sa.Column('home', sa.String(), nullable=True),
    sa.Column('odd_home', sa.String(), nullable=True),
    sa.Column('out', sa.String(), nullable=True),
    sa.Column('odd_out', sa.String(), nullable=True),
    sa.Column('tie', sa.String(), nullable=True),
    sa.Column('time', sa.String(), nullable=True),
    sa.Column('extract_date', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('jogos')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('jogos',
    sa.Column('id', sa.VARCHAR(), nullable=False),
    sa.Column('home', sa.VARCHAR(), nullable=True),
    sa.Column('odd_home', sa.VARCHAR(), nullable=True),
    sa.Column('out', sa.VARCHAR(), nullable=True),
    sa.Column('odd_out', sa.VARCHAR(), nullable=True),
    sa.Column('tie', sa.VARCHAR(), nullable=True),
    sa.Column('time', sa.VARCHAR(), nullable=True),
    sa.Column('extract_date', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('games')
    # ### end Alembic commands ###
