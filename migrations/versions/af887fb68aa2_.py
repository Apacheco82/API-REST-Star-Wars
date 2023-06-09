"""empty message

Revision ID: af887fb68aa2
Revises: f2f8d9194d47
Create Date: 2023-04-06 09:06:58.700888

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af887fb68aa2'
down_revision = 'f2f8d9194d47'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pilots', schema=None) as batch_op:
        batch_op.add_column(sa.Column('current', sa.Boolean(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pilots', schema=None) as batch_op:
        batch_op.drop_column('current')

    # ### end Alembic commands ###
