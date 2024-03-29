"""empty message

Revision ID: 5d3de377eae4
Revises: e983fbf23557
Create Date: 2020-07-23 12:52:50.415267

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d3de377eae4'
down_revision = 'e983fbf23557'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('자유시간', sa.Float(), nullable=True))
    op.drop_column('user', 'freetime')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('freetime', sa.FLOAT(), nullable=True))
    op.drop_column('user', '자유시간')
    # ### end Alembic commands ###
