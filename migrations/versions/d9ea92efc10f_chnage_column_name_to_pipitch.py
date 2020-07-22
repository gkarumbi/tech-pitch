"""Chnage column name to pipitch

Revision ID: d9ea92efc10f
Revises: 0150aadf4854
Create Date: 2020-07-23 00:05:32.102916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9ea92efc10f'
down_revision = '0150aadf4854'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('pitch', sa.String(), nullable=True))
    op.drop_column('pitches', 'content')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('content', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('pitches', 'pitch')
    # ### end Alembic commands ###