"""rename department

Revision ID: 619a6c6fbbe3
Revises: 992a43a2898e
Create Date: 2024-01-16 10:36:54.615653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '619a6c6fbbe3'
down_revision = '992a43a2898e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=False),
    sa.Column('address', sa.VARCHAR(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('departments')
    # ### end Alembic commands ###