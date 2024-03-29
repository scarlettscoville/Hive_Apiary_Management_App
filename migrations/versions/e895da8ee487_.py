"""empty message

Revision ID: e895da8ee487
Revises: f79a6b9c3991
Create Date: 2023-07-03 23:08:44.583850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e895da8ee487'
down_revision = 'f79a6b9c3991'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hive', sa.Column('numOfDeeps', sa.String(), nullable=True))
    op.add_column('hive', sa.Column('numOfMediums', sa.String(), nullable=True))
    op.add_column('hive', sa.Column('numOfShallows', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('hive', 'numOfShallows')
    op.drop_column('hive', 'numOfMediums')
    op.drop_column('hive', 'numOfDeeps')
    # ### end Alembic commands ###
