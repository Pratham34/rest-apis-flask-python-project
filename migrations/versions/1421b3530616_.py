"""empty message

Revision ID: 1421b3530616
Revises: 3bae155b8d3b
Create Date: 2023-01-02 10:30:56.278610

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1421b3530616'
down_revision = '3bae155b8d3b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
   

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(), nullable=False))
        batch_op.create_unique_constraint(None, ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('email')

   

    # ### end Alembic commands ###