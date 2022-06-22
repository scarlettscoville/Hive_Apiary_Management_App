"""empty message

Revision ID: 284d3480ac63
Revises: f799a033fc04
Create Date: 2022-06-21 22:58:57.920833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '284d3480ac63'
down_revision = 'f799a033fc04'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'icon')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('icon', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###