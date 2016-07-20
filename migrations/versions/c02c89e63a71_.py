"""empty message

Revision ID: c02c89e63a71
Revises: 8e75c327e44f
Create Date: 2016-07-19 21:32:57.003930

"""

# revision identifiers, used by Alembic.
revision = 'c02c89e63a71'
down_revision = '8e75c327e44f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('deleted', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'deleted')
    ### end Alembic commands ###
