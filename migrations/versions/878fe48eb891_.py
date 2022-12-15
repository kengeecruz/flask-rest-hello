"""empty message

Revision ID: 878fe48eb891
Revises: ba335436195f
Create Date: 2022-12-10 13:55:25.200343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '878fe48eb891'
down_revision = 'ba335436195f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=80), nullable=False))
        batch_op.add_column(sa.Column('age', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('age')
        batch_op.drop_column('name')

    # ### end Alembic commands ###