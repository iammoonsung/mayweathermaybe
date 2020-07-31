"""empty message

Revision ID: ef65d47cb1ba
Revises: 23c8c954bd87
Create Date: 2020-07-23 12:58:22.741088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef65d47cb1ba'
down_revision = '23c8c954bd87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', '자유시간')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('자유시간', sa.FLOAT(), nullable=True))
    # ### end Alembic commands ###
